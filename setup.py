#! /usr/bin/python

from setuptools import setup, find_packages
import os.path
    
setup(
    name = "docetl-speaker",
    description = "",
    install_requires = [
        "tts-wrapper @ git+https://github.com/redhog/tts-wrapper.git"
    ],
    version = "0.0.1",
    author = "Egil Moeller",
    author_email = "redhog@redhog.org",
    license = "GPL",
    url = "https://github.com/redhog/docetl-speaker",
    packages = find_packages(),
    entry_points = {
        "docetl.operation": [
            "speaker = docetl_speaker.operation:SpeakerOperation"
        ]

    }
)
