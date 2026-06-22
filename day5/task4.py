# Author: bibberzz
# Created: 2026/5/30 11:16
# Project: day5
# File: task4.py
# Description: HouseItem and House

class HouseItem:
    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return f'{self.name} 占地 {self.area} 平方米'


class House:
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return (f'房型：{self.house_type}\n'
                f'总面积：{self.area}\n'
                f'剩余面积：{self.free_area}\n')

    def add_item(self, item: HouseItem) -> None:
        self.item_list.append(item.name)
        self.free_area -= item.area
        print(f'放置家具 {item.name}，当前剩余面积：{self.free_area}')


if __name__ == '__main__':
    bed = HouseItem("席梦思", 4)
    chest = HouseItem("衣柜", 2)
    table = HouseItem("餐桌", 1.5)
    print(bed)
    print(chest)
    print(table)
    print("-" * 100)

    house = House("三室一厅", 120)
    print(house)

    house.add_item(bed)
    house.add_item(chest)
    house.add_item(table)
