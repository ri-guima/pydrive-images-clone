from pathlib import Path
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class File:
    filename: str
    content: bytes


def is_image(file: File) -> bool:
    return file.filename.split('.')[-1].lower() in ['jpg', 'jpeg', 'png']


def save(path: Path, file: File) -> None:
    with open(path, 'wb') as f:
        f.write(file.content)


class IDrive(ABC):

    @abstractmethod
    def get_images(self) -> list[File]:
        raise NotImplementedError()
