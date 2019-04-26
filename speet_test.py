import speedtest
import json
import requests
import time
from elasticsearch import Elasticsearch
import os

while True:
    print("starting")
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server()
    s.download()
    s.upload()
    speedtest_res = s.results.dict()

    res = requests.get('http://localhost:9200')
    print(res)
    es = Elasticsearch([{'host': 'localhost', 'port': '9200'}])

    # print(speedtest_res)
    # print(json.dumps(speedtest_res))

    es.index(index='speedtest', ignore=400, doc_type='json', body=json.dumps(speedtest_res))
    print(res["download"], res["upload"], res["ping"])
    time.sleep(os.environ.get("TEST_INTERVAL", 600))