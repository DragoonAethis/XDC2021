#!/usr/bin/env python3
import os
import sys
import tempfile
import subprocess
import multiprocessing

import slugify

template_name = "Template.svg"

blocks = [
    { "title": "Raspberry Pi Vulkan driver update", "speaker": "Iago Toral, Igalia" },
    { "title": "Lima driver status update 2021", "speaker": "Erico Nunes" },
    { "title": "The Occult and the Apple GPU", "speaker": "Alyssa Rosenzweig, Collabora" },
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


def generate(block):
    temp_svg_file = tempfile.mkstemp(suffix=".svg")[1]
    generated_file = slugify.slugify(block['title']) + ".png"
    svg_contents = template.replace("$SPEAKERS", block['speaker']).replace('$TITLE', block['title'])

    with open(temp_svg_file, 'w') as f:
        f.write(svg_contents)

    os.sync()
    subprocess.run(['inkscape', '-o', generated_file, temp_svg_file])
    os.unlink(temp_svg_file)
    return generated_file


# Behold! The world's worst preroll generator!
if __name__ == "__main__":
    with open(template_name) as f:
        template = f.read()

    with multiprocessing.Pool(16) as p:
        print(p.map(generate, blocks))
