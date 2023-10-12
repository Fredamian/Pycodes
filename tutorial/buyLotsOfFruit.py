# buyLotsOfFruit.py
# -----------------
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

#Fredy Brito - LEIT 3 Ano

"""
To run this script, type

  python buyLotsOfFruit.py

Once you have correctly implemented the buyLotsOfFruit function,
the script should produce the output:

Cost of [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)] is 12.25
"""

fruitPrices = {'apples': 2.0,'pears': 3.0,'limes': 4.0} #dicionario com chaves que sao as frutas e valores que sao os numeros

def buyLotsOfFruit(orderList):
    totalCost = 0.0
    for fruit, numPounds in orderList:
        if fruit in fruitPrices:
            totalCost += fruitPrices[fruit] * numPounds
        else:
            print(f"At the moment we don't have{fruit}")
            return 0

    return totalCost

# Test function
orderList = [('apples', 2.0), ('pears', 3.0), ('limes', 4.0)]
cost = buyLotsOfFruit(orderList)
print(f"Cost of {orderList} is {cost}")

