import requests
import pandas as pd
import simplejson as json
data = {#'date':'20160912', 
        'qopts.columns':['date','open'],
        'api_key':'uAAPYoy-nzBK3fcmXFAZ', 
        'ticker':'FB'}
r = requests.get('https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json', params=data)

df = pd.read_json(r.text)
print df.head()
print df.shape
#print r.url
#print r.text
