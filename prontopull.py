# -*- coding: utf-8 -*-

from urllib2 import Request, urlopen
import json
from pandas.io.json import json_normalize
import time
#from datetime import datetime

url = "https://secure.prontocycleshare.com/data/stations.json"
request = Request(url)
response = urlopen(request)
data = json.loads(response.read())
df=json_normalize(data['stations'])


timestring = time.strftime("%Y%m%d-%H%M%S")
SAVE_PATH = "../Desktop/pronto/pronto%s.csv" %timestring


df.to_csv(SAVE_PATH, sep = ",")
