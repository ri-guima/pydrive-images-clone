from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

from domain import IDrive, Image, is_image


class Drive(IDrive):

    def __init__(self) -> None:
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        gauth.LoadCredentialsFile('credentials.json')
        self.__drive = GoogleDrive(gauth)
    
    def get_images(self) -> list[Image]:
        images = list(filter(is_image, self.__drive.ListFile(
            {'q': '"root" in parents and trashed=false'}).GetList()
        ))
        return [self.__create_image(i) for i in images]

    def __create_image(self, image) -> Image:
        content = image.GetContentString()
        return Image(id=image['id'], extension=image['fileExtension'],
                     content=content)
