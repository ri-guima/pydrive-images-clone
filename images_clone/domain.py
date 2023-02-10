from pathlib import Path
from dataclasses import dataclass
from abc import ABC, abstractmethod


def is_image(filename: str) -> bool:
    return filename.split('.')[-1] in ['jpg', 'jpeg', 'png']


@dataclass
class Image:
    id: str
    extension: str
    content: bytes


def save_image(dir: Path, filename: str, content: bytes) -> None:
    with open(dir / filename, 'wb') as f:
        f.write(content)


class IDrive(ABC):

    @abstractmethod
    def get_images(self) -> list[Image]:
        raise NotImplementedError()
