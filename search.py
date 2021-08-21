import os
import pandas as pd
import eel
import shutil

### デスクトップアプリ作成課題
def kimetsu_search(word, csv_path):

     # 検索対象取得
    df = pd.read_csv("./source.csv")
    source = list(df["name"])
	
    # 検索
    if word in source:
        eel.view_log_js("『{}』はあります".format(word))

    else:
        eel.view_log_js("『{}』はありません".format(word))
        

        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        source.append(word)


    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    df.to_csv("./source.csv", encoding="utf_8-sig")
    print(source)

    if not os.path.exists(csv_path):
        os.mkdir(csv_path)
        shutil.copy2("./source.csv", "./" + csv_path + "/source.csv")
