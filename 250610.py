from menu_item250612 import MenuItem

# 引数を「 サンドイッチ 」と 500 としてください
menu_item1 = MenuItem("サンドイッチ", 500)

print(menu_item1.info())

result1 = menu_item1.get_total_price(4)
print("合計は" + str(result1) + "円です")


# 引数を「 雑炊 」と 1200 としてください
menu_item2 = MenuItem("雑炊", 1200)

print(menu_item2.info())

result2 = menu_item2.get_total_price(10)
print("合計は" + str(result2) + "円です")

# 総計
result_all = result1 + result2
print("総計は" + str(result_all) + "円です。")
