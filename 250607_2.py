# 対象商品の在庫数を更新する処理を作成してください
def restock_item(item_id, add_stock_count, items):
    for item in items:
        if item["id"] == item_id:
            item["stock"] = item["stock"] + add_stock_count
            return f"商品の在庫を更新しました（在庫数：{item['stock']}）"
    return "エラー：在庫を更新できませんでした"


# ここから下は触らないでください
# 利用するデータ
items = [
    {"id": 1, "name": "ゲームソフト", "stock": 15},
    {"id": 2, "name": "ヘッドホン", "stock": 30},
    {"id": 3, "name": "スマートフォン", "stock": 10},
]

# コンソールから入力を受け取る
item_id_input = input("補充したい商品のIDを入力してください：")
add_stock_input = input("追加する在庫数を入力してください：")

# 数値に変換（エラーハンドリングは省略中）
item_id = int(item_id_input)
add_stock_count = int(add_stock_input)

# 関数を呼び出して結果を表示
result = restock_item(item_id, add_stock_count, items)
print(result)

# item_id = 3
# add_stock_count = 5
# # 関数の呼び出し
# result = restock_item(item_id, add_stock_count, items)
# print("入力1：スマートフォンの在庫を更新する場合")
# print(result)

# print("-----------------------------")
# # 利用するデータ
# item_id = 4
# add_stock_count = 5
# # 関数の呼び出し
# result = restock_item(item_id, add_stock_count, items)
# print("入力2：該当する商品idが存在しなかった場合")
# print(result)
