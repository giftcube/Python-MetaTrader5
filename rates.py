import MetaTrader5 as mt5
from datetime import datetime
import pandas as pd

# MetaTrader 5に接続
if not mt5.initialize():
    print("MetaTrader5 initialize failed")
    mt5.shutdown()
    exit()

# 銘柄、時間軸、期間を指定
symbol = "BTCJPYm"
timeframe = mt5.TIMEFRAME_H1
start_date = datetime(2024, 12, 21)  # 開始日時を設定
end_date = datetime.now()  # 今日の日時を終了日時として設定

# 銘柄の情報を取得し、存在するか確認
symbol_info = mt5.symbol_info(symbol)
if symbol_info is None:
    print(f"Symbol {symbol} not found, check the symbol name")
    mt5.shutdown()
    exit()

if not symbol_info.visible:
    if not mt5.symbol_select(symbol, True):
        print(f"Failed to select {symbol}, exiting")
        mt5.shutdown()
        exit()

# レート情報を取得
rates = mt5.copy_rates_range(symbol, timeframe, start_date, end_date)
if rates is None:
    print(f"Failed to retrieve rates for {symbol}")
else:
    # Pandasのデータフレームに変換
    rates_df = pd.DataFrame(rates)
    rates_df['time'] = pd.to_datetime(rates_df['time'], unit='s')  # タイムスタンプを日時に変換
    print(rates_df.head())  # 最初の数件を表示
    print(rates_df.tail())  # 最後の数件を表示

# MetaTrader 5との接続を切断
mt5.shutdown()
