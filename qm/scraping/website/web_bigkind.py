from qm import utils
import requests
from dateutil.relativedelta import relativedelta
from datetime import datetime


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}


def category_keywords_json():
  req_url = 'https://www.bigkinds.or.kr/api/categoryKeywords.do'
  headers['Referer'] = 'https://www.bigkinds.or.kr/'
  params = {

  }
  r = requests.get(req_url, params, headers=headers)
  result = r.json()

  return result
