from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os

from domain import IDrive, File, is_image


class Drive(IDrive):

    def __init__(self) -> None:
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        gauth.LoadCredentialsFile('credentials.json')
        self.__drive = GoogleDrive(gauth)
    
    def get_images(self) -> list[File]:
        images = list(filter(lambda i: is_image(i.get('originalFilename', '')), self.__drive.ListFile(
            {'q': 'mimeType="application/vnd.google-apps.folder" and trashed=false and title="IMAGENS"'}).GetList()
        ))
        return [self.__create_image(i) for i in images]

    def __create_image(self, image) -> File:
        filename = f'{image["originalFilename"]}.{image["fileExtension"]}'
        image.GetContentFile(filename)
        with open(filename, 'rb') as f:
            content = f.read()
        os.remove(filename)
        return File(filename=image['originalFilename'], content=content)


class FakeDrive(IDrive):

    def get_images(self) -> list[File]:
        return [File(filename='12345.jpg', content=bytes('Hello World', 'utf-8'))]
