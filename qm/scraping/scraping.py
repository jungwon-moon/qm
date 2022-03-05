from qm.scraping.website import web_krx
import pandas as pd


# # # # #
def uncomma(str):
    return str.replace(',', '')


# # # # #
def get_kospi(Type=None):
    data = web_krx.stock_index(indIdx='1', strtDd='20100101', Type=Type)
    data = pd.DataFrame(data)
    data = data[['TRD_DD', 'OPNPRC_IDX', 'HGPRC_IDX', 'LWPRC_IDX', 'CLSPRC_IDX', 'ACC_TRDVOL', 'UPDN_RATE', 'ACC_TRDVAL']]
    data.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'rate', 'amount']
    data = data[::-1].reset_index(drop=True)
    data = data.applymap(uncomma)
    return data


def get_kosdaq(Type=None):
    '''
    Type: db
    '''
    data =  web_krx.stock_index(indIdx='2', strtDd='20100101', Type=Type)
    data = pd.DataFrame(data)
    data = data[['TRD_DD', 'OPNPRC_IDX', 'HGPRC_IDX', 'LWPRC_IDX', 'CLSPRC_IDX', 'ACC_TRDVOL', 'UPDN_RATE', 'ACC_TRDVAL']]
    data.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'rate', 'amount']
    data = data[::-1].reset_index(drop=True)
    data = data.applymap(uncomma)
    return data


def get_holiday(yy=None):
    return web_krx.holiday_json(yy)


def get_fundamentalv1(Dd=None):
    return web_krx.fundamentalv1_json(Dd)
    

def get_all_stock_price(Dd=None):
    return web_krx.all_stock_price(Dd)