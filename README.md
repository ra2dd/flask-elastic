Docker command for running Elasticsearch

```sh
docker run --name es01 --net elastic -p 9200:9200 -it -m 1GB elasticsearch:8.16.4
```

Activating virtual env with poetry 2.x
```sh
eval $(poetry env activate)
```