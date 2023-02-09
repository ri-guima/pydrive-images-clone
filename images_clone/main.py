from argparse import ArgumentParser

from adapters import Drive
from domain import save_image


if __name__ == '__main__':
    parser = ArgumentParser(description='Google Drive images clone')
    parser.add_argument('-d', '--dir', type=str, help='Clone directory')
    args = parser.parse_args()
    drive = Drive()
    for image in drive.get_images():
        save_image(args.dir, image)
