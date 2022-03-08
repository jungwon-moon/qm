import requests
import datetime

def dt2str(Dd, type='day'):
    '''
    day->yyyymmdd
    hhmm
    '''
    if type =='day':
        return''.join(filter(str.isalnum, str(Dd)))[:8]
    if type =='time':
        return''.join(filter(str.isalnum,str(Dd)))[:12]


def str2dt(Dd):

    return datetime.datetime.strptime(Dd, "%Y%m%d")


def check_trading_day(Dd, Type="API"):
    '''
    Return 
    False: non trading day
    Dd: trading day
    '''
    Dd = dt2str(Dd)
    diff = datetime.timedelta(days=1)

    # 주말 확인
    if datetime.date(int(Dd[:4]), int(Dd[4:6]), int(Dd[6:])).weekday() > 4:
        return check_trading_day(str2dt(Dd) - diff, Type)

    # 휴장일 확인
    if Type == "API":
        req_url = 'http://quantmag.net/api/kr/holiday'
        holiday = [row['calnd_dd'] for row in requests.get(req_url).json()]
        if Dd in holiday:
            return check_trading_day(str2dt(Dd) - diff, Type)
    else:
        holiday = [k[0] for k in Type.readDB('holiday', 'calnd_dd')]
        if Dd in holiday:
            return check_trading_day(str2dt(Dd) - diff, Type)

    return Dd
