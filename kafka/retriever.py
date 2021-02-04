# pip install datapackage
from datapackage import Package
import pandas as pd
import quandl
import pandas_datareader as pdr
from pandas_datareader import data
from datetime import datetime
import os
import functools


def get_tiingo(symbol='pnqi'):
    os.environ['TIINGO_API_KEY'] = '4f0ef79d635f50b78281480f44ff160d4ef68064'
    TIINGO_API_KEY = os.getenv('TIINGO_API_KEY')
    # df = pdr.get_data_tiingo(symbol, api_key=os.getenv('TIINGO_API_KEY'), start = '1/2/2004', end = '9/23/2020')
    # pnqi, ixn, vgt
    df = pdr.get_data_tiingo('ixn', api_key=os.getenv('TIINGO_API_KEY'), start = '1/2/2004', end = '9/23/2020')
    print(df.columns)
    df.reset_index(drop=False, inplace=True)
    df.columns = ['symbol', 'Date', 'close', 'high', 'low', 'open', 'volume', 'adjClose', 'adjHigh', 'adjLow', 'adjOpen', 'adjVolume', 'divCash', 'splitFactor']
    df.set_index('Date', inplace=True)
    print('after:', df.columns)
    print(df.head(5))
    return df


def yahoo(symbol, start='2010-01-01', end='2020-12-31'):
    df = data.DataReader(symbol, start=start, end=end, data_source='yahoo')
    columnsmap = {c:(symbol+'_'+c).replace(' ', '_').replace('^', '') for c in df.columns}
    if df.any:
        df.rename(columns=columnsmap, inplace=True)

    return df


def get_ndxt():
    # ndxt = quandl.get("NASDAQOMX/NDXT", authtoken="uxrgtFT8B7R2XsJ4hSuV")
    ndxt = quandl.get("AMEX/IXN", authtoken="uxrgtFT8B7R2XsJ4hSuV")
    print(ndxt.columns)
    ndxt.index.name = 'Date'
    #ndxt.columns = ['ndxt_Open','ndxt_High','ndxt_Low','ndxt_Close','ndxt_Adj_Close']
    # ndxt.columns = ['ndxt_Open','ndxt_High','ndxt_Low','ndxt_Close','ndxt_Adj_Close','ndxt_Volume']
    print(ndxt.head(5))
    return ndxt


def get_vix(pkg='https://datahub.io/core/finance-vix/datapackage.json'):
    package = Package(pkg)
    # print list of all resources:
    # print(package.resource_names)
    # print processed tabular data (if exists any)
    df = pd.DataFrame.empty
    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/csv':
            df = pd.DataFrame(data=resource.read())
            break

    if df.any:
        df.columns = ['Date', 'vix_Open', 'vix_High', 'vix_Low', 'vix_Close']
        df.set_index('Date', inplace=True)
    return df

# https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/ftp/F-F_Research_Data_5_Factors_2x3_daily_CSV.zip
def famafrench(infile='F-F_Research_Data_5_Factors_2x3_daily.CSV'):
    ff = pd.read_csv(infile, dtype={0: str})
    ff.rename(columns={ff.columns[0]: 'Date'}, inplace=True)
    #df['DATE'] = pd.to_datetime(df['DATE'], format='%Y%m%d').dt.strftime('%d.%m.%Y')
    ff['Date'] = pd.to_datetime(ff['Date'], format='%Y%m%d')
    ff.set_index('Date', inplace=True)
    # print(ff.head(5))
    # print(ff.columns)
    # print(ff.info())
    return ff

def test():
    print(yahoo('VIX'))

def main():
    # PNQI, IXN, VGT, ^VIX, ^NDX, ^RUT, ^VXN
    symbols = ['PNQI', 'IXN', 'VGT', '^VIX', '^NDX', '^RUT', '^VXN']
    dfs = list(map(yahoo, symbols))
    ff = famafrench()
    dfs.append(ff)
    df = functools.reduce(lambda a, b: a.join(b), dfs)
    print(df.head(5))
    print(df.columns)
    print(df.index.dtype)
    df.to_csv('df_all.csv')


if __name__ == '__main__':
    main()
    # test()
