import qm
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


def check_trading_day(Dd):
    '''
    Return 
    False: non trading day
    Dd: trading day
    '''
    # db = qm.connect.pymongo_connect().qmdb
    Dd = dt2str(Dd)
    diff = datetime.timedelta(days=1)

    # 과거 확인

    # 주말 확인
    if datetime.date(int(Dd[:4]), int(Dd[4:6]), int(Dd[6:])).weekday() > 4:
        return check_trading_day(str2dt(Dd) - diff)
    
    # 공휴일 확인
    
    return Dd
