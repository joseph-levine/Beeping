#!/usr/bin/env python3
from pathlib import Path

from icons import generate_icons, generate_pdf


def project_root() -> Path:
    return Path.cwd().parent


def assets_root() -> Path:
    return project_root().joinpath('Beeping').joinpath('Assets.xcassets')


def main():
    generate_icons(project_root().joinpath('icon.svg'), assets_root().joinpath('AppIcon.appiconset'))
    generate_pdf(project_root().joinpath('icon.svg'), assets_root().joinpath('AppIconVector.imageset'))


if __name__ == "__main__":
    main()
