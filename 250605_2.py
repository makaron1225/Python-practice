# 各商品と各色の組み合わせを全て出力する処理を作成してください
def display_product_and_color(items, colors):
    for item in items: # 商品を1つずつ取り出す
        for color in colors: #色を1つずつ取り出す
            print(item['name'] + ':' + color) #商品名：色　を出力する


# ここから下は触らないでください
# 利用するデータ
items = [
    {"name": "Tシャツ", "type": "clothes", "price": 2000},
    {"name": "キャップ", "type": "cap", "price": 8000},
]
colors = ["Red", "Blue", "Black"]
# 関数の呼び出し
display_product_and_color(items, colors)
