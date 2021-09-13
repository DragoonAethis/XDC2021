#!/usr/bin/env python3
import sys

day1 = [
    { "title": "Opening Session", "speaker": "Radosław Szwichtenberg, Intel" },
    { "title": "Raspberry Pi Vulkan driver update", "speaker": "Iago Toral, Igalia" },
    { "title": "Lima driver status update 2021", "speaker": "Erico Nunes" },
    { "title": "The Occult and the Apple GPU", "speaker": "Alyssa Rosenzweig, Collabora" },
    { "title": "ChromeOS + freedreno update", "speaker": "Rob Clark, Google" },
    { "title": "SSA-based Register Allocation\nfor GPU Architectures", "speaker": "Connor Abbott and Daniel Schürmann, Valve" },
    { "title": "etnativ: status update", "speaker": "Christian Gmeiner" },
    { "title": "Fast Checkpoint Restore\nfor AMD GPUs with CRIU", "speaker": "Rajneesh Bhardwaj and Felix Kuehling, AMD" },
    { "title": "Emulating Virtual Hardware in VKMS", "speaker": "Sumera Priyadarsini" },
    { "title": "Lightning Talks", "speaker": "Ricardo Garcia, Alyssa Rosenzweig and Roman Gilg" }
]

day2 = [
    { "title": "Opening Session", "speaker": "Radosław Szwichtenberg, Intel" },
    { "title": "Addressing Wayland robustness", "speaker": "David Edmundson, KDE" },
    { "title": "Compiling Vulkan shaders in the browser:\nA tale of control flow graphs and WebAssembly", "speaker": "Tony Wasserka" },
    { "title": "Dissecting and fixing Vulkan rendering\nissues in drivers with RenderDoc", "speaker": "Danylo Piliaiev, Igalia" },
    { "title": "Ray-tracing in Vulkan, Part 2: Implementation", "speaker": "Jason Ekstrand, Intel" },
    { "title": "Enabling Level Zero Sysman APIs for\ntool developers to control the GPUs", "speaker": "Saikishore Konda, Ravindra Babu Ganapathi,\nJitendra Sharma and T J Vivek Vilvaraj, Intel" },
    { "title": "Redefining the Future of\nAccelerator Computing with Level Zero", "speaker": "Jaime Arteaga, Ravindra Babu Ganapathi, Aravind Gopalakrishnan,\nMichal Mrozek, Brandon Fliflet and Ben Ashbaugh, Intel" },
    { "title": "X.Org Security", "speaker": "Matthieu Herrb" },
    { "title": "X.Org Foundation Board of Directors Meeting", "speaker": "Emma Anholt, Samuel Iglesias Gonsálvez, Mark Filion, Manasi D Navare,\nKeith Packard, Lyude Paul, Daniel Vetter and Harry Wentland" }
]

day3 = [
    { "title": "Opening Session", "speaker": "Radosław Szwichtenberg, Intel" },
    { "title": "Improving the Linux display stack reliability", "speaker": "Maxime Ripard" },
    { "title": "KWinFT's wlroots backend", "speaker": "Roman Gilg" },
    { "title": "TTM conversion in i915", "speaker": "Thomas Hellstrom, Intel" },
    { "title": "Status of freedesktop.org GitLab/cloud hosting", "speaker": "Benjamin Tissoires, Red Hat" },
    { "title": "Making bare-metal testing accessible\nto every developer", "speaker": "Martin Peres, X.Org" },
    { "title": "A new CPU performance scaling proposal\nfor tuning VKD3D-Proton", "speaker": "Ray Huang" },
    { "title": "Video decoding in Vulkan: A brief overview of the\nVK_KHR_video_queue & VK_KHR_video_decode APIs", "speaker": "Victor Manuel Jáquez Leal, Igalia" },
    { "title": "State of the X.Org", "speaker": "Lyude Paul, Red Hat" },
    { "title": "Closing Session", "speaker": "Everyone!" },
]

use_day = day1

if len(sys.argv) == 1:
    new_line = '\n'
    for index in range(len(use_day)):
        print(f"{index}: {use_day[index]['title'].replace(new_line, ' ')}")
else:
    try:
        index = int(sys.argv[1])
        details = use_day[index]
    except:
        print(f"First argument should be an index from 0 to {len(use_day)}")
        exit()

    with open('TalkName.txt', 'w') as f:
        print(details['title'])
        f.write(details['title'])

    with open('Speaker.txt', 'w') as f:
        print(details['speaker'])
        f.write(details['speaker'])
