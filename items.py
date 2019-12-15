#!/usr/bin/env python3
# import all the required libraries


from classes import *


def prep_items(structure):
    """
    The function is use for preparing of items in the game .

    Parameters:
    structure (list): list generated from the Maze class.

    Returns:
        items (objects): return three item objects
    """
    # creates a new instance of the class(Items) and assigns this object to a variable item_1
    item_1 = Items(structure)
    # calling method items_positions()
    item_1.items_position()
    # creates a new instance of the class(Items) and assigns this object to a variable item_2
    item_2 = Items(structure)
    # calling method items_positions()
    item_2.items_position()
    # creates a new instance of the class(Items) and assigns this object to a variable item_3
    item_3 = Items(structure)
    # calling method items_positions()
    item_3.items_position()

    while item_1.case_y == item_2.case_y and item_1.case_x == item_2.case_x:
        item_2.items_position()

    while (item_1.case_y == item_3.case_y and item_1.case_x == item_3.case_x) or (
            item_2.case_y == item_3.case_y and item_2.case_x == item_3.case_x):
        item_3.items_position()
    # return three item class objects
    return item_1, item_2, item_3
