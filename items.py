#!/usr/bin/env python3
# import all the required libraries


from classes import *


def prep_items(structure):
    item_1 = Items(structure)
    item_1.items_position()
    item_2 = Items(structure)
    item_2.items_position()
    item_3 = Items(structure)
    item_3.items_position()

    while item_1.case_y == item_2.case_y and item_1.case_x == item_2.case_x:
        item_2.items_position()

    while (item_1.case_y == item_3.case_y and item_1.case_x == item_3.case_x) or (
            item_2.case_y == item_3.case_y and item_2.case_x == item_3.case_x):
        item_3.items_position()

    return item_1, item_2, item_3
