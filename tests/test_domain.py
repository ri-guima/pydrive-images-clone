import pytest
from pathlib import Path
import os

from images_clone.domain import save_image, is_image, Image


def test_is_image():
    assert is_image('filename.jpg')
    assert is_image('filename.jpeg')
    assert is_image('filename.png')
    assert not is_image('filename.py')


def test_save_image():
    image = Image(id='12345', extension='jpg', content=bytes('Hello World', 'utf-8'))
    dir = 'tests/uploads'
    save_image(Path(dir), image)
    assert '12345.jpg' in os.listdir(dir)
    os.remove(Path(dir) / f'{image.id}.{image.extension}')
