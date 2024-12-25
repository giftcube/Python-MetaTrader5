import MetaTrader5 as mt5

# MetaTrader 5に接続
if not mt5.initialize():
    print("MetaTrader5 initialize failed")
    mt5.shutdown()

# MetaTrader 5バージョンについてのデータを表示する
print(f'MetaTrader5 version : {mt5.version()}')
 
terminal_info_dict = mt5.terminal_info()._asdict() # ターミナルの設定とステータスに関する情報を取得
account_info_dict = mt5.account_info()._asdict() # アカウント情報を取得

# MetaTrader 5との接続を切断
mt5.shutdown()

print(f'\nターミナルの設定とステータスに関する情報\n{terminal_info_dict}')
print(f'\nアカウント情報\n{account_info_dict}')
