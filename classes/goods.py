from enum_type.goods_type import GoodsType


class Goods:
    def __init__(self, price: float, weight_in_grams: float, producing_country: str,
                 goods_type: GoodsType, brand: str, goods_name: str):
        self.price = price
        self.weight_in_grams = weight_in_grams
        self.producing_country = producing_country
        self.goods_type = goods_type
        self.brand = brand
        self.goods_name = goods_name

    def __str__(self):
        return f'Price: {self.price}\n' \
               f'Weight in grams: {self.weight_in_grams}\n' \
               f'Made in: {self.producing_country}\n' \
               f'Brand: {self.brand}\n' \
               f'Goods name: {self.goods_name}\n'
