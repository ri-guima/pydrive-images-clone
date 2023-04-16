from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from dotenv import load_dotenv
import os

from domain import IDrive, File


class Drive(IDrive):

    def __init__(self) -> None:
        gauth = GoogleAuth()
        gauth.LocalWebserverAuth()
        self._drive = GoogleDrive(gauth)

    def get_files(self) -> list[File]:
        load_dotenv()
        folders_titles = os.getenv('FOLDERS', 'root').split(';')
        query = {
            'q': 'mimeType="application/vnd.google-apps.folder" and trashed=false'
        }
        folders = self._drive.ListFile(query).GetList()
        result = []
        for folder in folders:
            if folder['title'] in folders_titles:
                query = {'q': f'"{folder["id"]}" in parents and trashed=false'}
                result.extend([self._create_file(f) for f in
                               self._drive.ListFile(query).getList()])
        return result

    def _create_file(self, file) -> File:
        file.GetContentFile(file['originalFilename'])
        with open(file['originalFilename'], 'rb') as f:
            content = f.read()
        os.remove(file['originalFilename'])
        return File(filename=file['originalFilename'], content=content)
