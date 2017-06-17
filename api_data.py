import requests
import pandas as pd
import simplejson as json
from datetime import datetime

def getdatetime(unidate):
    # input is a unicode format date
    # return a datetime object
    strpdate = datetime.strptime(unidate, '%Y-%m-%d')
    return strpdate

def get_data(ticker):
    #ticker: string, stock ticker
    para = {'qopts.columns':'date,open',
            'api_key':'uAAPYoy-nzBK3fcmXFAZ',
            'ticker':ticker}
    r1 = requests.get('https://www.quandl.com/api/v3/datatables/WIKI/PRICES.json', params=para)
    j1 = r1.json()['datatable']

    data1 = {k:[v0,v1] for k,[v0,v1] in zip(range(len(j1['data'])), j1['data'])}
    df1 = pd.DataFrame.from_dict(data1, orient='index')
    df1 = df1.rename(columns={0:'date', 1:'open'})
    df1['datetime'] = [getdatetime(i) for i in df1['date']]
    return df1

if __name__ == "__main__":
    get_data('GOOG')
