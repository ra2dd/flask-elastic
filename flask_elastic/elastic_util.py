import os

from elasticsearch import Elasticsearch
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
es = Elasticsearch(
    "https://localhost:9200",
    basic_auth=("elastic", str(os.getenv("ELASTIC_PASSWORD"))),
    verify_certs=False,
)


def create_es_user_index():
    es.indices.create(index="users", ignore=400)
    es.index(
        index="users",
        id=1,
        document={"name": "User1", "language": "Python"},
    )


def search_es_document(index: str = "users", id: int = 1):
    result = es.get(index=index, id=id)
    return result
