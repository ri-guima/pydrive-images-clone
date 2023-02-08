from flask import url_for
from pydrive.auth import GoogleAuth
from dotenv import load_dotenv
import os
from pathlib import Path
from pydrive.drive import GoogleDrive


def is_image(file):
    allowed_extensions = ['jpg', 'jpeg', 'png']
    return file.get('fileExtension') in allowed_extensions


def to_dict(file):
    return {'id': file['id'], 'url': url_for_image(file)}


def url_for_image(image):
    return url_for('.static', filename=f'uploads/{get_filename(image)}')


def save_image(file):
    load_dotenv('.env')
    file.GetContentFile(Path(os.getenv('UPLOAD_FOLDER')) / get_filename(file))


def get_filename(file):
    return f'{file["id"]}.{file["fileExtension"]}'


def get_drive_files(drive):
    return drive.ListFile({'q': '"root" in parents and trashed=false'}).GetList()


def create_drive():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    gauth.LoadCredentialsFile('credentials.json')
    return GoogleDrive(gauth)
