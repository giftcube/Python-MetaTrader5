import MetaTrader5 as mt5
import pandas as pd
from datetime import datetime, timedelta

# MetaTrader 5に接続
if not mt5.initialize():
    print("MetaTrader5 initialize failed")
    mt5.shutdown()
    exit()

# 銘柄、期間を指定
symbol = "BTCJPYm"
end_date = datetime.now()  # 今日の日時
start_date = end_date - timedelta(days=3)  # 今日から3日前の日時

# ティックデータを取得
ticks = mt5.copy_ticks_range(symbol, start_date, end_date, mt5.COPY_TICKS_ALL)

# 取得したティックデータをPandasデータフレームに変換
ticks_df = pd.DataFrame(ticks, columns=["time", "bid", "ask", "last", "volume", "flags"])
ticks_df['time'] = pd.to_datetime(ticks_df['time'], unit='s')

# データの確認
if not ticks_df.empty:
    print("取得したティックデータの先頭5行:")
    print(ticks_df.head())
    print("\n取得したティックデータの最後5行:")
    print(ticks_df.tail())
else:
    print("指定された期間にティックデータはありません。")

# MetaTrader 5との接続を切断
mt5.shutdown()
