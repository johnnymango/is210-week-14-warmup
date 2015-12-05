#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Comprehensions."""


from data import FRUIT


def get_cost_per_item(shoplist):
    """This function gets the cost per item.

    Args:
        shoplist(dict): A dictionary containing the item & its quantity.

    Returns:
        Dict: a new dict containing the cost for each item found in FRUIT.

    Examples:
    >>>get_cost_per_item({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
    {'Lime': 7.08, 'Peach': 95.76, 'Red Pear': 9.96}
    """
    return dict([(k, r * FRUIT.get(k)) for k, r in shoplist.iteritems()
                 if k in FRUIT])


def get_total_cost(shoplist):
    """This function gets the total cost of all items on list.

    Args:
        shoplist(dict): A dictionary containing the item & its quantity.

    Returns:
        Int: The total cost of all items on the list found in FRUIT.

    Examples:
    >>>get_total_cost({'Lime': 12, 'Red Pear': 4, 'Peach': 24, 'Beet': 1})
    112.80000000000001
    """
    return sum([item for item in get_cost_per_item(shoplist).values()])
