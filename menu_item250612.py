class MenuItem:
    # 引数 name と price を受け取るようにしてください
    def __init__(self, name, price):
        # 「 サンドイッチ 」の代わりに引数 name の値を代入してください
        self.name = name

        # 500 の代わりに引数 price の値を代入してください
        self.price = price

    def info(self):
        return self.name + ": ¥" + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        if count >= 3:
            total_price *= 0.9

        return round(total_price)
