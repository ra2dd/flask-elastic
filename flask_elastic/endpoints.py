from http import HTTPStatus
from flask import jsonify

from flask_elastic.app import app
from flask_elastic.elastic_util import search_es_document, create_services_index


@app.route("/search_document/")
def search_document():
    response = search_es_document()
    return jsonify(response.body), HTTPStatus.OK


@app.route("/create_services/")
def create_services():
    result = create_services_index()
    return jsonify(result)
