# Author: bibberzz
# Created: 2026/5/30 10:37
# Project: day5
# File: furniture_house.py
# Description:

class HouseItem:
    """
    Furniture class
    """

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'{self.name} 占地 {self.area} 平方米。'


class House:
    """
    House class
    """

    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area  # 剩余面积
        self.item_list = []  # 存家具对象

    def __str__(self):
        return f'户型：{self.house_type}\n' \
               f'总面积：{self.area}\n' \
               f'剩余面积：{self.free_area}\n' \
               f'家具：{self.item_list}\n'

    def add_item(self, item: HouseItem) -> None:
        """
        : 后是入参类型注解
        ->None是返回值注解
        :param item:
        :return:
        """
        if self.free_area >= item.area:
            self.item_list.append(item.name)
            self.free_area -= item.area
        else:
            print('房子满了，放不下')


if __name__ == '__main__':
    bed = HouseItem("席梦思", 4)
    chest = HouseItem("衣柜", 2)
    table = HouseItem("餐桌", 1.5)
    print(bed)
    print(chest)
    print(table)
    house = House("三室一厅", 80)
    print(house)
    house.add_item(bed)
    print(house)
