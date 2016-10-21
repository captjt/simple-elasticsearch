# Elasticsearch with Python

### Must Haves
[Elasticsearch](https://www.elastic.co/downloads/elasticsearch)

[Python](https://www.python.org/download/releases/3.5.2/)

### Standing up Elasticsearch

```
bin/elasticsearch -Des.node.name=Skywalker
bin/elasticsearch -Des.node.name=Kenobi
```

In your browser go to `localhost:9200` and `localhost:9201` to test the servers are running

Once you have those servers running clone the repository locally

```
pyvenv env
. env/bin/activate
pip install -r requirements
python init.py
python search.py
```

`init.py` script will load swapi.co Star Wars character data.
`search.py` script will do some small queries on the character dataset we ingested.

Enjoy!