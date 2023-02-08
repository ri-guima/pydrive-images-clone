from flask import Blueprint, jsonify, abort

from image_api import utils


bp = Blueprint('image_api', __name__, url_prefix='/image-api')


@bp.get('/')
def get_images():
    result = []
    for file in utils.get_drive_files()
        if utils.is_image(file):
            utils.save_image(file)
            result.append(utils.to_dict(file))
    return jsonify(result)


@bp.get('/<string:code>')
def get_image_item(code):
    file = list(filter(lambda f: f['id'] == code, utils.get_driver_files()))
    if file:
        return jsonify(utils.to_dict(file[0]))
    abort(404)
