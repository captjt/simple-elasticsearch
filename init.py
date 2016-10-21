"""
Script to load the initial dataset from swapi.co
This dataset will be mapped off of Star Wars characters
Turn on your two es nodes at ports 9200 & 9201
"""

import sys
import json
import requests


def setup_data():
    from elasticsearch import Elasticsearch
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    # connect to the first cluster
    r = requests.get('http://localhost:9200')

    # Breaks at 17 api endpoint error
    i = 1
    while r.status_code == 200:
        r = requests.get('http://swapi.co/api/people/'+ str(i))
        es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content.decode('utf-8')))
        i=i+1


def finish_data():
    from elasticsearch import Elasticsearch
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    # connect to the second cluster
    r = requests.get('http://localhost:9201')

    i = 18
    while r.status_code == 200:
        r = requests.get('http://swapi.co/api/people/'+ str(i))
        es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content.decode('utf-8')))
        i=i+1

    print('===> Data Import - total records: ', i)


def main(argv):
    print('Setup Data')
    setup_data()

    print('Finish Data')
    finish_data()

    return 0

# After data loads look at mapping localhost:9200/sw/ or localhost:9200/_mapping
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
