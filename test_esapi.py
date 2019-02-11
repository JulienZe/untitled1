# coding:utf8
import os
from elasticsearch import Elasticsearch
import eigen_config

from datetime import datetime
from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch(hosts="http://10.10.11.181:9200/", timeout=240, max_retries=10, retry_on_timeout=True)
for index, value in es.indices.get(index='_all').items():
    print(index)
    print(value)
