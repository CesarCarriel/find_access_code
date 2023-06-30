from flask import request, jsonify, Blueprint

from src.controllers import FindAccessCodeWithKeyLogsController

app = Blueprint('routes', __name__)


@app.route('/upload/<string:filename>', methods=['PUT'])
def update(filename: str):
    if not request.get_data():
        return 'No files sent.', 400

    try:
        access_code = FindAccessCodeWithKeyLogsController().execute(file_content=request.get_data())

        return jsonify(access_code=access_code)

    except Exception as e:
        return f'Error processing the file: {str(e)}', 500
