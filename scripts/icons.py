#!/usr/bin/env python3
import os
import shutil
from pathlib import Path
from subprocess import run
from typing import List, Any, Union


class ExportImage(object):
    @staticmethod
    def __inkscape() -> str:
        return '/Applications/Inkscape.app/Contents/Resources/bin/inkscape'

    def __init__(self, side_length: int, densities: List[int], source_file: Path, directory: Path):
        assert (len(densities) > 0)
        self.__side_length = side_length
        self.__densities = densities
        self.__source_file = source_file
        self.__directory = directory

    def __paths(self):
        def name(density: int):
            if density == 1:
                return 'icon-' + str(self.__side_length) + '.png'
            return 'icon-' + str(int(self.__side_length / density)) + '@' + str(density) + 'x.png'

        for density in self.__densities:
            yield self.__directory.joinpath(name(density))

    def __image_path(self) -> str:
        return str(self.__directory.joinpath('gen-' + str(self.__side_length) + '.png'))

    def generate(self) -> None:
        run([self.__inkscape(), '-f', str(self.__source_file), '--export-width=' + str(self.__side_length),
             '--export-height=' + str(self.__side_length), '--export-png=' + self.__image_path()], check=True)

    def move(self) -> None:
        full_image_path = self.__image_path()
        paths = list(self.__paths())
        for path in paths[:-1]:
            shutil.copyfile(full_image_path, path)
        os.rename(full_image_path, str(paths[-1]))


def generate_icons(source_file: Path, destination: Path):
    images_to_generate = [
        [20, [1]],
        [29, [1]],
        [40, [1, 2]],
        [58, [2]],
        [60, [3]],
        [76, [1]],
        [80, [2]],
        [87, [3]],
        [120, [2, 3]],
        [152, [2]],
        [167, [2]],
        [180, [3]],
        [1024, [1]]
    ]
    for export_image in images_to_generate:
        export_image = ExportImage(export_image[0], export_image[1], source_file, destination)
        export_image.generate()
        export_image.move()


if __name__ == "__main__":
    generate_icons(Path.cwd().joinpath('icon.svg'), Path.cwd())
