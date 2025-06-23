import utils250602
import random

print("じゃんけんをはじめます")
player_name = input("名前を入力してください：")
print("何を出しますか？（0: グー, 1: チョキ, 2: パー）")
player_hand = int(input("数字で入力してください："))

if utils250602.validate(player_hand):
    computer_hand = random.randint(0, 2)

    if player_name == "":
        utils250602.print_hand(player_hand)
    else:
        utils250602.print_hand(player_hand, player_name)

    utils250602.print_hand(computer_hand, "コンピューター")

    # 変数 result に関数 judge の戻り値を代入してください
    utils250602.result = utils250602.judge(player_hand, computer_hand)
    # 変数 result を出力してください
    print("結果は" + utils250602.result + "でした")
else:
    print("正しい数値を入力してください")
