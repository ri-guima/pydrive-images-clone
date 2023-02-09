import pytest
from pathlib import Path

from images_copy.main import save_image, is_image, Image


def test_is_image():
    assert is_image('filename.jpg')
    assert is_image('filename.jpeg')
    assert is_image('filename.png')
    assert not is_image('filename.py')


def test_save_image(drive):
    image = Image(id='12345', extension='jpg')
    dir = Path('tests/uploads')
    save_image(dir, image)
    assert '12345.jpg' in dir.glob('*')
