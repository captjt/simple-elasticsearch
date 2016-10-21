"""
Script to query the initial dataset from swapi.co
This dataset that is queried is mapped off of Star Wars characters
"""

import sys
from elasticsearch import Elasticsearch


def run_queries():
    es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    # match query "Darth"
    darth_search = es.search(index="sw", body={
        "query": {
            "match": {
                'name':'Darth Vader'
            }
        }
    })

    # prefix query "Lu"
    lu_search = es.search(index="sw", body={
        "query": {
            "prefix" : {
                "name" : "lu"
            }
        }
    })

    # fuzzy query on 'Jaba'
    jaba_search = es.search(index="sw", body={
        "query": {
            "fuzzy": {
                "name": "jaba",
            }
        }
    })

    print('===> Match "Darth" \n', darth_search)
    print('===> Prefix "Lu" \n', lu_search)
    print('===> Fuzzy "Jaba" \n', jaba_search)


def main(argv):
    print ('Running Queries')
    run_queries()

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
