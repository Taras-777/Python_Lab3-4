from manager.device_manager import DeviceManager
from classes.fishing_rod import FishingRod
from classes.bait import Bait
from classes.cord import Cord
from enum_type.materials_type import MaterialsType
from enum_type.type_rod import TypeRod
from enum_type.appointment_type import AppointmentType

if __name__ == '__main__':
    goods = [
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

    manager = DeviceManager(goods)

    add_rod = FishingRod(277, 2.55, "Ukraine", "Favorite", "Vigor Spin", "Wood", 16, "Spining", MaterialsType.WOOD,
                         TypeRod.SPINING)
    manager.add_goods(add_rod)

    add_bait = Bait(115, 2.39, "Chine", "Nike", "Number1", "Roach", AppointmentType.ROACH)
    manager.add_goods(add_bait)

    print("\n====================Сортування ціни за спаданням====================\n")

    goods_sort_by_descending_price = manager.sort_by_price(reverse=True)
    for goods in goods_sort_by_descending_price:
        print(goods)

    print("====================Сортування ціни за зростанням====================\n")

    goods_sort_by_price_increase = manager.sort_by_price(reverse=False)
    for goods in goods_sort_by_price_increase:
        print(goods)
    print("====================Додані товари====================")
    print(add_rod)
    print(add_bait)

    print("====================Сортування за вагою====================")
    devices_sorted_by_weight = manager.sort_by_weight(reverse=False)
    for goods in devices_sorted_by_weight:
        print(goods)
