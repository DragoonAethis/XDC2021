#!/usr/bin/env python3
import os
import sys
import base64
import argparse
import tempfile
import subprocess
import multiprocessing

import slugify

EPILOG = """
In default mode, the script loads a template SVG file and replaces $SPEAKERS and $TITLE lines with
the talk block contents. In Eyecatch Mode, it does the same, but also loads a PNG image from the
"eyecatch" directory and replaces $EYECATCH in the template file with the Base64-encoded embed. The
source file name must match the output file. The SVG template must have a xlink:href value set to
"$EYECATCH" for the image to be replaced (instead of the base64 blob in its place). This is useful
for generating video thumbs.
"""

blocks = [
    { "title": "Raspberry Pi Vulkan driver update", "speaker": "Iago Toral, Igalia" },
    { "title": "Lima driver status update 2021", "speaker": "Erico Nunes" },
    { "title": "The Occult and the Apple GPU", "speaker": "Alyssa Rosenzweig" },
    { "title": "ChromeOS + freedreno update", "speaker": "Rob Clark, Google" },
    { "title": "SSA-based Register Allocation for GPU Architectures", "speaker": "Connor Abbott and Daniel Schürmann, Valve" },
    { "title": "etnaviv: status update", "speaker": "Christian Gmeiner" },
    { "title": "Fast Checkpoint Restore for AMD GPUs with CRIU", "speaker": "Felix Kuehling, Rajneesh Bhardwaj and David Yat Sin, AMD" },
    { "title": "Emulating Virtual Hardware in VKMS", "speaker": "Sumera Priyadarsini" },
    { "title": "Lightning Talks I", "speaker": "Everyone!" },

    { "title": "Addressing Wayland robustness", "speaker": "David Edmundson, KDE" },
    { "title": "Compiling Vulkan shaders in the browser: A tale of control flow graphs and WebAssembly", "speaker": "Tony Wasserka, Valve" },
    { "title": "Dissecting and fixing Vulkan rendering issues in drivers with RenderDoc", "speaker": "Danylo Piliaiev, Igalia" },
    { "title": "Ray-tracing in Vulkan, Part 2: Implementation", "speaker": "Jason Ekstrand, Intel" },
    { "title": "KWinFT in 2021: Latest Development, Next Steps", "speaker": "Roman Gilg" },
    { "title": "Enabling Level Zero Sysman APIs for tool developers to control the GPUs", "speaker": "Saikishore Konda and Ravindra Babu Ganapathi, Intel" },
    { "title": "Redefining the Future of Accelerator Computing with Level Zero", "speaker": "Jaime Arteaga and Michal Mrozek, Intel" },
    { "title": "X.Org Security", "speaker": "Matthieu Herrb" },

    { "title": "Improving the Linux display stack reliability", "speaker": "Maxime Ripard" },
    { "title": "KWinFT's wlroots backend", "speaker": "Roman Gilg" },
    { "title": "TTM conversion in i915", "speaker": "Thomas Hellstrom, Intel" },
    { "title": "Status of freedesktop.org GitLab/cloud hosting", "speaker": "Benjamin Tissoires, Red Hat" },
    { "title": "Making bare-metal testing accessible to every developer", "speaker": "Martin Roukala, Valve" },
    { "title": "A new CPU performance scaling proposal for tuning VKD3D-Proton", "speaker": "Ray Huang, AMD" },
    { "title": "Video decoding in Vulkan: A brief overview of the VK_KHR_video_queue and VK_KHR_video_decode APIs", "speaker": "Victor Manuel Jáquez Leal, Igalia" },
    { "title": "State of the X.Org", "speaker": "Lyude Paul, Red Hat" },
    { "title": "Lightning Talks II", "speaker": "Everyone!" },

    { "title": "Coordinating the CI efforts for Linux + userspace", "speaker": "Martin Roukala, Valve" },
    { "title": "SSA-based Register Allocation", "speaker": "Connor Abbott and Daniel Schürmann, Valve" },
    { "title": "Hostile Multi-Tenancy on a Single Commodity GPU: Can it be secure?", "speaker": "Demi Obenour" },
    { "title": "X.Org Security BoF", "speaker": "Matthieu Herrb" },
]


def generate(block, template, eyecatch=False):
    temp_svg_file = tempfile.mkstemp(suffix=".svg")[1]
    generated_file = slugify.slugify(block['title']) + ".png"
    svg_contents = template.replace("$SPEAKERS", block['speaker']).replace('$TITLE', block['title'])

    if eyecatch:
        with open(f"eyecatch/{generated_file}", 'rb') as f:
            eyecatch_png = f.read()

        eyecatch_embed_b64 = "data:image/png;base64," + str(base64.b64encode(eyecatch_png), encoding='utf-8')
        svg_contents = svg_contents.replace("$EYECATCH", eyecatch_embed_b64)

    with open(temp_svg_file, 'w') as f:
        f.write(svg_contents)

    os.sync()
    subprocess.run(['inkscape', '-o', generated_file, temp_svg_file])
    os.unlink(temp_svg_file)
    return generated_file


# Behold! The world's worst preroll generator!
def run_app():
    parser = argparse.ArgumentParser(description="Generate video thumbnails and preroll screens.",
                                     epilog=EPILOG)
    parser.add_argument('--template', default='Template.svg',
                        help="SVG template to load and transform (default: Template.svg)")
    parser.add_argument('--eyecatch', action='store_true',
                        help="enable Eyecatch Mode (read more below)")
    parser.add_argument('--single-thread', action='store_true',
                        help="disable multiprocessing (useful for debugging)")
    args = parser.parse_args()

    try:
        with open(args.template) as f:
            template = f.read()
    except IOError:
        print(f"Could not open/read the template file ({args.template}).")
        exit(1)

    jobs = [(block, template, args.eyecatch) for block in blocks]
    if args.single_thread:
        for job in jobs:
            generate(*job)
    else:
        with multiprocessing.Pool(16) as p:
            print(p.starmap(generate, jobs))


if __name__ == "__main__":
    run_app()
