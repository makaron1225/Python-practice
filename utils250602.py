def validate(hand):
    if hand < 0 or hand > 2:
        return False
    return True


def print_hand(hand, name="ゲスト"):
    hands = ["グー", "チョキ", "パー"]
    print(name + "は" + hands[hand] + "を出しました")


# 関数 judge を定義してください
def judge(player, computer):
    # player と computer の比較結果によって条件を分岐してください
    if player == computer:
        return "引き分け"
    elif player == 0 and computer == 1:
        return "勝ち"
    elif player == 1 and computer == 2:
        return "勝ち"
    elif player == 2 and computer == 0:
        return "勝ち"
    else:
        return "負け"