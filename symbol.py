import MetaTrader5 as mt5

# MetaTrader 5に接続
if not mt5.initialize():
    print("MetaTrader5 initialize failed")
    mt5.shutdown()

# 銘柄コードのリストを取得と表示
symbols = mt5.symbols_get()

for symbol in symbols:
    print(symbol.name)

# MetaTrader 5との接続を切断
mt5.shutdown()
