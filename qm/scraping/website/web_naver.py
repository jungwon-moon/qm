from qm import utils
import warnings
import requests
from dateutil.relativedelta import relativedelta
from datetime import datetime
from io import BytesIO
from bs4 import BeautifulSoup as bs
import pandas as pd


# 공통 헤더
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
    }

def naver_board(stock_code:str='005930', sep='hour'):
    '''
    네이버 종목토론방 크롤링
    일단 제목까지만
    '''
    now = int(utils.change_Dd(datetime.now(), 'time')[:10])
    title = []
    date = []
    page = 1
    while(True):
        url = f'https://finance.naver.com/item/board.naver?code={stock_code}&page={page}'
        page += 1

        r = requests.get(url, headers=headers)
        soup = bs(r.text, 'html.parser')
        date += [k.text for i, k in enumerate(soup.find_all('span', {'class':'tah p10 gray03'})) if i%2 == 0]
        title += [k.get('title') for k in soup.select('#content > div.section.inner_sub > table.type2 > tbody > tr > td.title > a')]
        if int(utils.change_Dd(date[-1], 'time')[:10]) < int(now)-1:
            break
    return date, title