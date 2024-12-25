import MetaTrader5 as mt5
import pandas as pd

# MetaTrader 5 に接続
if not mt5.initialize():
    print("MetaTrader 5の初期化に失敗しました。エラーコード：", mt5.last_error())
    quit()

# 保有ポジションを取得
positions = mt5.positions_get()

# ポジションのデバッグと確認
if positions is None:
    print("positions_get() の結果が None です。現在保有しているポジションがないか、エラーが発生しています。")
    mt5.shutdown()
    quit()
elif len(positions) == 0:
    print("ポジションが存在しません。")
    mt5.shutdown()
    quit()
else:
    print(f"{len(positions)} 件のポジションを取得しました。")

# ポジション情報をPandas DataFrameに変換
positions_dict = []
for position in positions:
    positions_dict.append({
        'ticket': position.ticket,
        'time': pd.to_datetime(position.time, unit='s'),
        'symbol': position.symbol,
        'type': 'Buy' if position.type == 0 else 'Sell',  # 'type' を Buy または Sell に変換
        'volume': position.volume,
        'price_open': position.price_open,
        'sl': position.sl,
        'tp': position.tp,
        'price_current': position.price_current,
        'profit': position.profit,
        'swap': position.swap,
        'comment': position.comment,
        'magic': position.magic
    })

positions_df = pd.DataFrame(positions_dict)

# データの確認
if not positions_df.empty:
    print("取得したポジション情報の先頭5行:")
    print(positions_df.head())
else:
    print("ポジション情報をDataFrameに変換できませんでした。")

# MetaTrader 5 の終了
mt5.shutdown()
