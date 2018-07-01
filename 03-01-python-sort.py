import csv

f = open('../03-01-python-sort.csv', 'r')
# この段階ではファイルをコード内で扱える状態にしただけ

reader = csv.reader(f)
# csvファイルからReaderオブジェクトを生成
# ここでprint(reader)をすると　<_csv.reader object at 0x1103c49e8>と表示されることからもわかる
# 各行はリストとして読み込まれている。ので以下の処理をして取り出す
for row in reader:
    #　１行ずつリストとしての取り出す
    for item in row:
        # リスト内の要素を取り出す
        print(item, end=" ")
    print()

f.close()
# ファイルを使い終わったら明示的にcloseする方が良いと言われている

"""
openメソッドの引数encodingを補足。第３引数に当たる。CSVファイルの文字コードを指定することができる。例）ms932, utf_8
これによって文字化けなどが起きた場合対処する。

CSVにおいてはheaderという、このファイルに付属するラベルやタイトルのような意味合いを一行目に書くことが多い。
そのためヘッダーを読み飛ばし、データの部分のみを読み込みたい場合 next(reader)を利用する
"""
