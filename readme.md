# QANotify 微信推送


[ 本工具为运维工具, 需要先关注 QAPRO 公共号来获取你自己的ID]

[本公共号为 QUANTAXIS/yutiansut 维护, 请勿过量推送占用带宽]

获取 id 方法:

微信搜索公共号 QAPRO, 回复 trade 即可获取


提供以下三个推送模板


1. 策略下单推送

    run_order_notify

    参数:
    ```
    user_id, 
    strategy_id='测试策略', 
    accountname="账户名", 
    code='测试品种 A', 
    order_direction='BUY', 
    order_offset="OPEN", 
    price=20, 
    volume=100, 
    ordertime=None
    ```
2. 策略运维状态推送

    run_strategy_notify

    参数
    ```
    user_id,
    strategyname='测试策略',
    title='策略状态运行推送',
    message='数据正常',
    frequence='日'
    ```


3. 行情到价推送

    run_price_notify


    参数
    ```
    user_id ,
    title='策略x',
    code='自定义品种  X_DIFF',
    currentprice=20,
    limitprice=22,
    order_id='N'
    ```