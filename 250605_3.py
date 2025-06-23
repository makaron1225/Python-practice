# カート内の合計金額を返す処理を作成してください
def calculate_total_price(cart_items):
    total_price = 0  # 注文金額の初期値を決定
    for item in cart_items:  # （cartの中の商品を取り出す）
        if item["type"] == "clothes":  # 商品タイプが衣服か確認
            total_price = total_price + item["price"] - 1000
        elif item["type"] == "food":  # 商品タイプが衣服か確認
            total_price = total_price + item["price"] * 0.9
        else:  # 　商品タイプがそれ以外
            total_price = total_price + item["price"]
    return round(total_price)


# ここから下は触らないでください
# 利用するデータ
cart_items = [
    {"name": "Tシャツ", "type": "clothes", "price": 2000},
    {"name": "キャップ", "type": "cap", "price": 8000},
    {"name": "ランニングシューズ", "type": "shoes", "price": 15000},
    {"name": "アンダーウェア", "type": "clothes", "price": 4500},
    {"name": "テニスラケット", "type": "sports goods", "price": 8000},
    {"name": "スポーツドリンク", "type": "food", "price": 150},
]
# 関数の呼び出し
total_price = calculate_total_price(cart_items)
print(total_price)
