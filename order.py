import MetaTrader5 as mt5

# MetaTrader 5に接続
if not mt5.initialize():
    print("MetaTrader5 initialize failed")
    mt5.shutdown()

# 注文のシンボル、数量（ロット）、注文タイプを設定
symbol = "BTCJPYm"
lot = 0.001
order_type = mt5.ORDER_TYPE_SELL
price = mt5.symbol_info_tick(symbol).bid

# 成行注文用のトレードリクエストを作成
trade_request = {
    "action": mt5.TRADE_ACTION_DEAL,
    "symbol": symbol,
    "volume": lot,
    "type": order_type,
    "price": price,
    "deviation": 20,
    "magic": 234000,
    "comment": "Python MT5 sell order",
    "type_time": mt5.ORDER_TIME_GTC,
    "type_filling": mt5.ORDER_FILLING_FOK,
}

# 注文を送信
result = mt5.order_send(trade_request)

if result.retcode != mt5.TRADE_RETCODE_DONE:
    print("Order failed, retcode =", result.retcode)
else:
    print("Order successfully placed with ticket #", result.order)

# MetaTrader 5との接続を切断
mt5.shutdown()
