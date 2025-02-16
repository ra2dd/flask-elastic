import os

from elasticsearch import Elasticsearch
from elastic_transport import ObjectApiResponse
import urllib3

from flask_elastic.data import SERVICES_INDEX_NAME, SERVICES_DOCS

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", str(os.getenv("ELASTIC_PASSWORD"))),
    verify_certs=False,
)


def create_user_index():
    es.indices.create(index="users", ignore=400)
    es.index(
        index="users",
        id=1,
        document={"name": "User1", "language": "Python"},
    )


def create_services_index() -> list:
    result = []
    for i, doc in enumerate(SERVICES_DOCS):
        response = es.index(index=SERVICES_INDEX_NAME, id=i + 1, document=doc)
        result.append(f"doc {i} - {response['result']}")
    return result


def search_es_document(index: str = "users", id: int = 1) -> ObjectApiResponse:
    result = es.get(index=index, id=id)
    return result
