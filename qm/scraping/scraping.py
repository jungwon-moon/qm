from qm.scraping.website import web_krx
import pandas as pd


def get_kospi(Type=''):
    data = web_krx.stock_index(indIdx='1', strtDd='20100101', Type=Type)

    data = pd.DataFrame(data)
    data = data[['TRD_DD', 'OPNPRC_IDX', 'HGPRC_IDX', 'LWPRC_IDX', 'CLSPRC_IDX', 'ACC_TRDVOL', 'UPDN_RATE', 'ACC_TRDVAL']]
    data.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'rate', 'amount']
    data = data[::-1].reset_index(drop=True)
    
    def uncomma(str):
        return str.replace(',', '')
    data = data.applymap(uncomma)
    
    return data


def get_kosdaq(Type=''):
    data =  web_krx.stock_index(indIdx='2', strtDd='20100101', Type=Type)

    data = pd.DataFrame(data)
    data = data[['TRD_DD', 'OPNPRC_IDX', 'HGPRC_IDX', 'LWPRC_IDX', 'CLSPRC_IDX', 'ACC_TRDVOL', 'UPDN_RATE', 'ACC_TRDVAL']]
    data.columns = ['date', 'open', 'high', 'low', 'close', 'volume', 'rate', 'amount']
    data = data[::-1].reset_index(drop=True)
    
    def uncomma(str):
        return str.replace(',', '')
    data = data.applymap(uncomma)

    return data


def get_non_trading_days(yy=''):

    return web_krx.non_trading_days_json(yy)
