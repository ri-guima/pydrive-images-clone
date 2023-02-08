from flask import Blueprint, jsonify, abort
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


bp = Blueprint('image_api', __name__, url_prefix='/image-api')


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
drive = GoogleDrive(gauth)


@bp.get('/<int:code>')
def get_image(code):
    files = drive.ListFile({'q': '"root" in parents and trashed=false'}).GetList()
    image = list(filter(lambda f: f['id'] == code, files))
    if image:
        return jsonify({'image': image[0]})
    abort(404)