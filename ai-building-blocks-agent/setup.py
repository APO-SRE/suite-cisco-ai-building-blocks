# ai-building-blocks-agent/setup.py
#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="ai-building-blocks-agent",
    version="0.1.0",
    python_requires=">=3.12",
    install_requires=[
        "rich>=14.0.0",
        "colorama",
    ],
    # Only include our tools package and its submodules:
    packages=find_packages(include=["tools", "tools.*"]),
    entry_points={
        "console_scripts": [
            "create-platform=tools.create_platform:main",
            "create-index=tools.create_index:main",
        ],
    },
)
