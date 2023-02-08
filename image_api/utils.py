from flask import url_for
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def is_image(file):
    allowed_extensions = ['jpg', 'jpeg', 'png']
    return file.get('extensions') in allowed_extensions


def to_dict(file):
    return {'id': file['id'], 'url': url_for_image(file)}


def save_image(file):
    pass


def url_for_image(image):
    filename = f'uploads/{image["id"]}.{image["extension"]}'
    return url_for('.static', filename=filename)


def get_drive_files():
    drive = get_drive()
    return drive.ListFile({'q': '"root" in parents and trashed=false'}).GetList()


def get_drive():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile('credentials.txt')
    if gauth.credentials is None:
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        gauth.Refresh()
    else:
        gauth.Authorize()
    gauth.SaveCredentialsFile('credentials.txt')
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)
