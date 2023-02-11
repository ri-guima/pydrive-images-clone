import pytest
from pathlib import Path
import os

from images_clone.domain import save, is_image, File


def test_is_image():
    assert is_image(File('filename.jpg', bytes('Hello World', 'utf-8')))
    assert not is_image(File('filename.py', bytes('Hello World', 'utf-8')))


def test_save_image():
    image = File(filename='12345.jpg', content=bytes('Hello World', 'utf-8'))
    dir = 'tests/uploads'
    save(Path(dir) / image.filename, image)
    assert '12345.jpg' in os.listdir(dir)
    os.remove(Path(dir) / image.filename)
