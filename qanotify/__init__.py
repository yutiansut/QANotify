
import pandas as pd
import numpy as np
import datetime
import requests
import traceback
import os

__version__ = '0.0.1'
__author__ = 'yutiansut'


def run_order_notify(user_id, 
    strategy_id='测试策略', 
    accountname="账户名", 
    code='测试品种 A', 
    order_direction='BUY', 
    order_offset="OPEN", 
    price=20, 
    volume=100, 
    ordertime=None):
    if ordertime is None:
        ordertime = str(datetime.datetime.now())

    try:
        requests.post("http://101.132.37.31/signal?user_id={}&template=xiadan_report&strategy_id={}&realaccount={}&code={}&order_direction={}&order_offset={}&price={}&volume={}&order_time={}".format(
            user_id, strategy_id, accountname, code, order_direction, order_offset, price, volume, ordertime
        ))

    except:
        traceback.print_exc()
def run_strategy_notify(
        user_id,
        strategyname='测试策略',
        title='策略状态运行推送',
        message='数据正常',
        frequence='日'):

    currenttime = str(datetime.datetime.now())
    remark = "来自 QAPRO || 当前时间 {}".format(currenttime)

    try:
        requests.post("http://101.132.37.31/signal?user_id={}&template=strategy_status&first={}&name={}&stype={}&frequence={}&remark={}".format(
            user_id, title, strategyname, message, frequence, remark))
    except:
        traceback.print_exc()
def run_price_notify(
        user_id ,
        title='策略x',
        code='自定义品种  X_DIFF',
        currentprice=20,
        limitprice=22,
        order_id='N'):
    currenttime = str(datetime.datetime.now())
    remark = "来自 QAPRO || 当前时间 {}".format(currenttime)
    try:
        requests.post("http://101.132.37.31/signal?user_id={}&template=price_notify&first={}&name={}&curprice={}&limitprice={}&orderid={}&remark={}".format(
        user_id, title, code, currentprice, limitprice, order_id, remark))
    except:
        traceback.print_exc()

if __name__ == '__main__':
    run_order_notify()
    run_strategy_notify()
    run_price_notify()
