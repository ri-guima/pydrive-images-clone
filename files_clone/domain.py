from pathlib import Path
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class File:
    filename: str
    content: bytes


def save(path: Path, file: File) -> None:
    with open(path, 'wb') as f:
        f.write(file.content)


class IDrive(ABC):

    @abstractmethod
    def get_files(self) -> list[File]:
        raise NotImplementedError()
