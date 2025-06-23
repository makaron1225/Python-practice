# 購入金額に対する付与ポイントを返す処理を作成してください
def calculate_points(total_price, user):
    point_rate = 0.01
    points = total_price * point_rate
    if user['status'] == 'premium':
        points = points + total_price * point_rate
    else:
        points = total_price * point_rate
    return round(points)

# ここから下は触らないでください
# 利用するデータ
total_price = 20000

user = {'user_id': 1, 'status': 'basic'}
# 関数の呼び出し
points = calculate_points(total_price, user)
print('入力1：会員ステータスがbasicの場合')
print(points)

print('-----------------------------')

# 利用するデータ
user = {'user_id': 2, 'status': 'premium'}
# 関数の呼び出し
points = calculate_points(total_price, user)
print('入力1：会員ステータスがpremiumの場合')
print(points)