import os
from pathlib import Path


def test_main():
    dir = 'tests/uploads'
    os.system(f'python images_clone/main.py --testing -d {dir}')
    assert '12345.jpg' in os.listdir(dir)
    os.remove(Path(dir) / '12345.jpg')
