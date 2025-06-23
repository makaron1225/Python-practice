# 購入数に応じた割引計算をする処理を作成してください
# def calculate_large_discounts(price, quantity):
#     total_price = 0 #初期値の設定
#     if quantity >= 20:
#         total_price = round(total_price + price * quantity * 0.9)
#     elif 10 <= quantity < 20:
#         total_price = round(total_price + price * quantity * 0.95)
#     else:
#         total_price = price * quantity
#     return total_price


def calculate_large_discounts(price, quantity):
    # 購入数に応じた条件分岐をする
    if quantity >= 20:
        # 購入数が20個以上の場合は、1つあたり10%の割引率にする
        discount_rate = 0.10
    elif quantity >= 10:
        # 購入数が10個以上の場合は、1つあたり5%の割引率にする
        discount_rate = 0.05
    else:
        # 購入数が10個未満の場合は、割引率は0にする
        discount_rate = 0.0
    # 単価を割引計算をする
    discounted_price = price * (1 - discount_rate)
    # 割引後の単価を使って合計金額を計算する
    total_price = discounted_price * quantity
    # 小数点以下を四捨五入して合計金額を返す
    return round(total_price)


# ここから下は触らないでください
# 利用するデータ
price = 100
quantity = 20
# 関数の呼び出し
total_price = calculate_large_discounts(price, quantity)
print("入力1：購入数が20個の場合")
print(total_price)

print("-----------------------------")

# 利用するデータ
quantity = 10
# 関数の呼び出し
total_price = calculate_large_discounts(price, quantity)
print("入力2：購入数が10個の場合")
print(total_price)

print("-----------------------------")

# 利用するデータ
quantity = 9
# 関数の呼び出し
total_price = calculate_large_discounts(price, quantity)
print("入力3：購入数が9個の場合")
print(total_price)
