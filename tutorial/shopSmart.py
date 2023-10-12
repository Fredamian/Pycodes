# shopSmart.py
# ------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
Here's the intended output of this script, once you fill it in:

Welcome to shop1 fruit shop
Welcome to shop2 fruit shop
For orders:  [('apples', 1.0), ('oranges', 3.0)] best shop is shop1
For orders:  [('apples', 3.0)] best shop is shop2
"""
from __future__ import print_function
import shop


def shopSmart(orderList, fruitShops):
    """
    orderList: List of (fruit, numPound) tuples
    fruitShops: List of FruitShops
    """
    # Initialize variables to keep track of the best shop and its cost
    best_shop = None
    best_cost = float('inf')  # Initialize with positive infinity

    # Iterate through the list of fruit shops
    for shop in fruitShops:
        # Calculate the cost of the order for the current shop
        cost = shop.getPriceOfOrder(orderList)

        # If the current shop's cost is lower than the best cost, update the best shop and best cost
        if cost < best_cost:
            best_shop = shop
            best_cost = cost

    return best_shop

if __name__ == '__main':
    orders1 = [('apples', 1.0), ('oranges', 3.0)]
    orders2 = [('apples', 3.0)]
    dir1 = {'apples': 2.0, 'oranges': 1.0}
    shop1 = shop.FruitShop('shop1', dir1)
    dir2 = {'apples': 1.0, 'oranges': 5.0}
    shop2 = shop.FruitShop('shop2', dir2)
    shops = [shop1, shop2]

    # Test cases
    print("For orders ", orders1, ", the best shop is", shopSmart(orders1, shops).getName())  # Should print "shop1"
    print("For orders: ", orders2, ", the best shop is", shopSmart(orders2, shops).getName())  # Should print "shop2"

