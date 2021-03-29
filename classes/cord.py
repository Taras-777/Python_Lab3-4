from classes.goods import Goods
from enum_type.goods_type import GoodsType


class Cord(Goods):
    def __init__(self, price: float, weight_in_grams: float, producing_country: str,
                 model_name: str, brand: str, long: int, diameter: int, color: str):
        super().__init__(price, weight_in_grams, producing_country,
                         GoodsType.CORD, model_name, brand)
        self.long = long
        self.diameter = diameter
        self.color = color

    def __str__(self):
        return super(Cord, self).__str__() + f'Long: {self.long}\n' \
                                             f'Diameter: {self.diameter}\n' \
                                             f'Color: {self.color}\n'
