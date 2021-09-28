from qanotify import run_order_notify, run_price_notify, run_strategy_notify

user_id = ''
"""
关注 QAPRO 公共号回复 trade 获取 id 填在这里

下面的参数可以看 readme

"""

run_strategy_notify(user_id)
run_order_notify(user_id)
run_price_notify(user_id)