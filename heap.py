# heap library of python
from heapq import heapify, heappush, heappop



# wifi pizza get query

# !/bin/python3

import sys
import os
import urllib.request
import json

# Complete the function below.
# https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=[topic]
import requests
from collections import Counter


def count(word, text):
    for item in text.items():
        print(item.count(word))
        return 150


def getTopicCount(topic):
    response = requests.get(
        "https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&page=" + topic)
    if response.status_code == 200:
        resJson = response.json()
        return count(topic, resJson['parse']['text'])
    return


f = open(os.environ['OUTPUT_PATH'], 'w')