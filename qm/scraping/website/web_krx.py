from qm import utils
import warnings
import requests
from dateutil.relativedelta import relativedelta
from datetime import datetime
from io import BytesIO
from bs4 import BeautifulSoup as bs
import pandas as pd


now = datetime.now()
ago_1mon = utils.dt2str(now - relativedelta(months=1))
ago_3mon = utils.dt2str(now - relativedelta(months=3))
ago_6mon = utils.dt2str(now - relativedelta(months=6))

# 공통 헤더
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}


def fundamentalv1_df(Dd=None):
    '''
    '''  # 펀더멘탈 excel로 스크래핑
    if Dd == None:
        Dd = utils.dt2str(now)[:8]
        Dd = utils.check_trading_day(Dd)

    headers['Referer'] = 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201'
    req_url = 'http://data.krx.co.kr/comm/fileDn/GenerateOTP/generate.cmd'
    params = {
        'searchType': '1',
        'mktId': 'ALL',
        'trdDd': str(Dd),
        'isuCd': 'KR7005930003',
        'isuCd2': 'KR7005930003',
        'param1isuCd_finder_stkisu0_0': 'ALL',
        'csvxls_isNo': 'false',
        'name': 'fileDown',
        'url': 'dbms/MDC/STAT/standard/MDCSTAT03501',
    }
    r = requests.get(req_url, params, headers=headers)

    req_url = 'http://data.krx.co.kr/comm/fileDn/download_excel/download.cmd'
    form_data = {'code': r.content}
    r = requests.get(req_url, form_data, headers=headers)
    with warnings.catch_warnings(record=True):
        warnings.simplefilter('always')
        df = pd.read_excel(BytesIO(r.content), engine='openpyxl')

    return df


def fundamentalv1_json(Dd=None):
    '''

    '''
    if Dd == None:
        Dd = utils.dt2str(now)[:8]
    Dd = utils.check_trading_day(Dd)

    headers['Referer'] = 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201'
    req_url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
    params = {
        'bld': 'dbms/MDC/STAT/standard/MDCSTAT03501',
        'searchType': '1',
        'mktId': 'ALL',
        'trdDd': str(Dd),
    }
    r = requests.get(req_url, params=params, headers=headers)
    result = r.json()

    return result['output']


def holiday_json(yy=None):
    '''
    휴장일 데이터를 json으로 반환
    yy: 해당연도
    Return

    '''
    if yy == None:
        yy = utils.dt2str(now)[:4]

    req_url = 'https://open.krx.co.kr/contents/OPN/99/OPN99000001.jspx'
    params = {
        'search_bas_yy': yy,
        'gridTp': 'KRX',
        'pagePath': '/contents/MKD/01/0110/01100305/MKD01100305.jsp',
        'code': 'JwqlNosVVtCXa7sc5spaVOEA1htzXlH2x9wOa34CWCMdk0SsTxu0w811j9T6paVtRuwRBShCPN9M9smK1s2Tx2DmoC2+E9KJ7ThLD+Z1eepP07eP9j9j8AojpkvULQ07jLt02MKabSy7E7lEbxmTiNaUlYtYKrL1K0TbXUyQoiNSxQv0LKol5HBRIxz26/hr'
    }
    r = requests.get(req_url, params=params, headers=headers)

    return r.json()['block1']


def ipo(strtDd=ago_6mon, endDd=utils.dt2str(now)):
    '''
    ipo 관련통계 공시일전후 등락률
    
    '''
    headers['Referer'] = 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0202'
    headers['Origin'] = 'http://data.krx.co.kr'
    req_url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
    params = {
        'bld': 'dbms/MDC/STAT/issue/MDCSTAT20201',
        'mktId': 'ALL',
        'isuCd': 'ALL',
        'strtDd': strtDd,
        'endDd': endDd,
        'isuCd2': 'ALL',
        'KNX': 'KNX',
        'tboxisuCd_finder_stkisu0_2': '전체',
        'param1isuCd_finder_stkisu0_2': 'ALL',
        'inqCondTpCd': 'Y',
        'share': '1',
        'money': '1',
        'csvxls_isNo': 'true',
    }
    r = requests.get(req_url, params=params, headers=headers)
    return r.json()['output']


def stock_index(indIdx, strtDd=ago_1mon, Type=None, endDd=None):
    '''
    indIdx='1' : kospi
    indIdx='2' : kosdaq
    시세 추이
    '''
    if Type == None:
        strtDd = now
    
    if endDd == None:
        endDd = now

    strtDd = utils.check_trading_day(strtDd)
    endDd = utils.check_trading_day(now)

    headers['Referer'] = 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201010103'
    headers['Origin'] = 'http://data.krx.co.kr'
    req_url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
    params = {
        'bld': 'dbms/MDC/STAT/standard/MDCSTAT00301',
        'locale': 'ko_KR',
        'indIdx': indIdx,
        'indIdx2': '001',
        'strtDd': strtDd,
        'endDd': endDd,
        'share': '1',
        'money': '1',
        'csvxls_isNo': 'false',
    }
    r = requests.get(req_url, params=params, headers=headers)
    return r.json()['output']


def all_stock_price(Dd=None):
    if Dd == None:
        Dd = utils.dt2str(now)[:8]
    Dd = utils.check_trading_day(Dd)

    headers['Origin'] = 'http://data.krx.co.kr'
    headers['Referer'] = 'http://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201'
    req_url = 'http://data.krx.co.kr/comm/bldAttendant/getJsonData.cmd'
    params = {
        'bld': 'dbms/MDC/STAT/standard/MDCSTAT01501',
        'locale': 'ko_KR',
        'mktId': 'ALL',
        'trdDd': Dd,
        'share': '1',
        'money': '1',
        'csvxls_isNo': 'false',
    }
    r = requests.get(req_url, params=params, headers=headers)
    return r.json()['OutBlock_1']