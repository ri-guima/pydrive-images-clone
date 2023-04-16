from argparse import ArgumentParser
from pathlib import Path

from adapters import Drive
from domain import save


if __name__ == '__main__':
    parser = ArgumentParser(description='Google Drive images clone')
    parser.add_argument('-d', '--dir', type=str, help='Clone directory')
    args = parser.parse_args()
    for image in Drive().get_images():
        save(Path(args.dir) / image.filename, image)
