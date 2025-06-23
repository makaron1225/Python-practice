# 会員割引の計算をする処理を作成してください（上は自分のコード）
# def calculate_member_discount(total_price, user):
#     discount_price = 0  # 初期値の設定
#     if user["status"] == "basic":
#         discount_price = total_price
#     elif user["status"] == "premium":
#         discount_price = total_price - 500
#     return discount_price

def calculate_member_discount(total_price, user):
    if user['status'] == 'premium':
        return total_price - 500
    else:
        return total_price


# ここから下は触らないでください
# 利用するデータ
total_price = 5000
user = {"user_id": 1, "name": "Ken", "status": "basic"}
# 関数の呼び出し
discount_price = calculate_member_discount(total_price, user)
print("入力1：会員情報がbasicの場合")
print(discount_price)

print("-----------------------------")

# 利用するデータ
total_price = 5000
user = {"user_id": 2, "name": "John", "status": "premium"}
# 関数の呼び出し
discount_price = calculate_member_discount(total_price, user)
print("入力2：会員情報がpremiumの場合")
print(discount_price)
