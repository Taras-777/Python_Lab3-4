from classes.goods import Goods
from enum_type.goods_type import GoodsType
from enum_type.type_rod import TypeRod
from enum_type.materials_type import MaterialsType


class FishingRod(Goods):
    def __init__(self, price: float, weight_in_grams: float, producing_country: str,
                 model_name: str, brand: str, materials: str, length: int, type: str, materials_type: MaterialsType,
                 type_rod: TypeRod):
        super().__init__(price, weight_in_grams, producing_country,
                         GoodsType.ROD, model_name, brand)
        self.materials = materials
        self.length = length
        self.type = type
        self.materials_type = materials_type
        self.type_type = type_rod

    def __str__(self):
        return super(FishingRod, self).__str__() + f'Materials: {self.materials}\n' \
                                                   f'Length: {self.length}\n' \
                                                   f'Type: {self.type}\n'
