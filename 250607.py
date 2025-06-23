# クーポンコードの割引を適用する処理を作成してください
# def apply_coupon(coupon_code, total_price, coupons):
#     if coupons['code'] == 'SAVE10':
#         total_price = total_price * (1 - 0.1)
#     elif coupons['code'] == 'SAVE20':
#         total_price = total_price * (1 - 0.2)
#     elif coupons['code'] == 'SAVE30':
#         total_price = total_price * (1 - 0.3)
#     else:
#         total_price = total_price
#     return total_price


def apply_coupon(coupon_code, total_price, coupons):
    for coupon in coupons:
        if coupon["code"] == coupon_code:
            discount = coupon["discount_percentage"]
            return round(total_price * (1 - discount))
    # 該当クーポンがなければ割引なし
    return round(total_price)


# ここから下は触らないでください
# 利用するデータ
coupons = [
    {"code": "SAVE10", "discount_percentage": 0.1},
    {"code": "SAVE20", "discount_percentage": 0.2},
    {"code": "SAVE30", "discount_percentage": 0.3},
]
total_price = 12000
coupon_code = "SAVE10"
# 関数の呼び出し
discount_total_price = apply_coupon(coupon_code, total_price, coupons)
print("入力1：10%割引になる場合")
print(discount_total_price)

print("-----------------------------")

# 利用するデータ
coupon_code = "SAVE40"
# 関数の呼び出し
discount_total_price = apply_coupon(coupon_code, total_price, coupons)
print("入力2：クーポンコードが該当しない場合")
print(discount_total_price)
