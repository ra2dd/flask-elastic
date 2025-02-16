from http import HTTPStatus
from flask import jsonify

from flask_elastic.app import app
from flask_elastic.elastic_util import search_es_document


@app.route("/search_document/")
def search_document():
    response = search_es_document()
    return jsonify(response.body), HTTPStatus.OK
