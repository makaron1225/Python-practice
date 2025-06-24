class MenuItem:
    # 引数 name と price を受け取るようにしてください
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        return self.name + ": ¥" + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        if count >= 3:
            total_price *= 0.9

        return round(total_price)
