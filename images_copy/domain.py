from pathlib import Path
from dataclasses import dataclass
from abc import ABC, abstractmethod


def is_image(filename: str) -> bool:
    return filename.split('.')[-1] in ['jpg', 'jpeg', 'png']


@dataclass
class Image:
    id: str
    extension: str
    content: str


def save_image(dir: Path, image: Image) -> None:
    with open(dir / f'{image.id}.{image.extension}', 'wb') as f:
        f.write(image.content)


class IDrive(ABC):

    @abstractmethod
    def get_images(self) -> list[Image]:
        raise NotImplementedError()
