from classes.goods import Goods
from enum_type.goods_type import GoodsType
from enum_type.appointment_type import AppointmentType


class Bait(Goods):
    def __init__(self, price: float, weight_in_grams: float, producing_country: str,
                 model_name: str, brand: str, appointment: str, appointment_type: AppointmentType):

        super().__init__(price, weight_in_grams, producing_country,
                         GoodsType.BAIT, model_name, brand)
        self.appointment_type = appointment_type
        self.appointment = appointment

    def __str__(self):
        return super(Bait, self).__str__()
