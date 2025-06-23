# カート内の商品の税込合計金額を返す処理を作成してください
def calculate_total_with_tax(cart_items, tax_rate):
    total_price = 0  # 合計金額の初期値を設定
    for item in cart_items:  # カート内の各商品を1つずつ取り出す
        total_price = total_price + item["price"]  # 金額を合計する
    total_with_tax = total_price * (1 + tax_rate)  # 税率を加算して計算
    return round(total_with_tax)  # 税込合計金額を返す


# ここから下は触らないでください
# 利用するデータ
cart_items = [
    {"name": "Tシャツ", "type": "clothes", "price": 2000},
    {"name": "キャップ", "type": "cap", "price": 8000},
]
tax_rate = 0.1
# 関数の呼び出し
total_with_tax = calculate_total_with_tax(cart_items, tax_rate)
print(total_with_tax)
