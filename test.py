import unittest
from main import *


class TestDeviceManager(unittest.TestCase):
    def setUp(self):
        self.test_goods_list = [
            FishingRod(499, 1000, "USA", "Brain", "Warrior WRR-895", "Wood", 16, "Spining", MaterialsType.WOOD,
                       TypeRod.SPINING),
            FishingRod(249, 1250, "Ukraine", "Favorite", "Free Carp-89", "Carbon", 16, "Winter fishing rod",
                       MaterialsType.CARBON, TypeRod.WINTER_FISHING_ROD),
            FishingRod(300, 2000, "Chine", "Salmo", "Warrior WRR-888", "Metal", 16, "Dropshot", MaterialsType.METAL,
                       TypeRod.DROPSHOT),

            Cord(230, 500, "USA", "Salmo", "Vigor Spin777", 25, 16, "Red"),
            Cord(220, 300, "Chine", "Brain", "Free Carp-777", 40, 16, "Black"),
            Cord(210, 400, "Ukraine", "Select", "Gladiator Ranger", 80, 16, "White"),

            Bait(430, 2.66, "USA", "Salmo", "Vigor Spin", "Amur", AppointmentType.AMUR),
            Bait(435, 2.77, "Ukraine", "Brain", "Warrior WRR-874", "Carp", AppointmentType.CARP),
            Bait(215, 2.88, "Chine", "Favorite", "Gladiator Ranger-001", "Shark", AppointmentType.SHARK)]

        self.goods_manager = DeviceManager(self.test_goods_list)

    def test_sort_by_descending_price(self):
        actual = self.goods_manager.sort_by_price(reverse=False)
        expected = sorted(self.test_goods_list, key=lambda goods: goods.price, reverse=False)
        self.assertEqual(actual, expected)

    def test_sort_by_price_increase(self):
        actual = self.goods_manager.sort_by_price(reverse=False)
        expected = sorted(self.test_goods_list, key=lambda goods: goods.price, reverse=False)
        self.assertEqual(actual, expected)

    def test_sort_by_weight(self):
        actual = self.goods_manager.sort_by_weight(reverse=False)
        expected = sorted(self.test_goods_list, key=lambda goods: goods.weight_in_grams, reverse=False)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
