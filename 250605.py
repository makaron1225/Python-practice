# 対象ユーザーの注文履歴を返す処理を作成してください
def get_order_history(user_id, orders):
    user_orders = []  # 対象ユーザーの注文履歴を入れるリスト

    for order in orders:  # 注文を1件ずつ確認
        if order["user_id"] == user_id:  # ユーザーIDが一致しているか判定
            user_orders.append(order)  # 一致していればリストに追加

    return user_orders  # 最終的なリストを返す


# --- ここからは使うときの処理 ---

# 入力を受け取って数値に変換する
input_id = int(input("ユーザーIDを入力してください："))

# 利用するデータ
orders = [
    {
        "order_id": 1,
        "user_id": 1,
        "items": [
            {"name": "キャップ", "type": "cap", "price": 8000},
            {"name": "Tシャツ", "type": "clothes", "price": 2000},
        ],
    },
    {
        "order_id": 2,
        "user_id": 2,
        "items": [
            {"name": "ランニングシューズ", "type": "shoes", "price": 15000},
        ],
    },
    {
        "order_id": 3,
        "user_id": 1,
        "items": [{"name": "スポーツドリンク", "type": "food", "price": 150}],
    },
    {
        "order_id": 4,
        "user_id": 3,
        "items": [
            {"name": "アンダーウェア", "type": "clothes", "price": 4500},
            {"name": "テニスラケット", "type": "sports goods", "price": 8000},
        ],
    },
]

user_orders = get_order_history(input_id, orders)

if user_orders:
    for order in user_orders:
        print(order)
else:
    print("このユーザーIDには注文履歴がありません。")
