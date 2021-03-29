
class DeviceManager:
    def __init__(self, goods=[]):
        self.goods = goods

    def add_goods(self, goods):
        self.goods.append(goods)

    def sort_by_price(self, reverse=False):
        sorted_goods = sorted(self.goods, key=lambda goods: goods.price, reverse=reverse)
        return sorted_goods

    def sort_by_weight(self, reverse=False):
        x = lambda a: a+10
        sorted_goods_by_weight = sorted(self.goods, key=lambda goods: goods.weight_in_grams, reverse=reverse)
        return sorted_goods_by_weight





