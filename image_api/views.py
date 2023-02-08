from flask import Blueprint, jsonify, abort

from image_api import utils


bp = Blueprint('image_api', __name__, url_prefix='/image-api', static_folder='static')


drive = utils.create_drive()


@bp.get('/')
def get_images():
    result = []
    for file in utils.get_drive_files(drive):
        if utils.is_image(file):
            utils.save_image(file)
            result.append(utils.to_dict(file))
    return jsonify(result)


@bp.get('/<string:id>')
def get_image_item(id):
    file = list(filter(lambda f: f['id'] == id, utils.get_drive_files(drive)))
    if file:
        utils.save_image(file[0])
        return jsonify(utils.to_dict(file[0]))
    abort(404)
