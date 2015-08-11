class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.weight = weight
        self.value = value
    
    def getRatio(self):
        return self.value/float(self.weight)


class Node:
    def __init__(self, level, items, takenItems, maxWeight):
        self.level = level
        self.allItems = items
        self.maxWeight = maxWeight
        self.taken = takenItems
        self.bound = [item.value for item in takenItems]
        
    
    def getWeight(self):
        return sum([item.weight for item in self.taken])
    

    def getValue(self):
        return sum([item.value for item in self.taken])
    
    
    def addItem(self, item):
        self.taken.append(item)


    def calcBound(self):
        # For all upcoming items calc it as a fractional
        cWeight = self.getWeight()
        item = None
        
        for i in range(self.level, len(self.allItems)):
            item = self.allItems[i]
            if cWeight + item.weight > self.maxWeight:
                break
            else:
                self.bound += item.value
                cWeight += item.weight
        if item:
            self.bound += (self.maxWeight - cWeight) * (item.value / item.weight)

import copy

def knapsackSolve(items, maxWeight):
    # Get items that is fitable
    items = filter(lambda item: item.weight <= maxWeight, items)
    
    # All items are filtered out
    if len(items) == 0:
        return
    
    # Sort them by ratio so maxbound will be met ASAP
    items.sort(key=lambda item: item.getRatio(), reverse=True)

    tree = []    
    startNode = Node(0, items, [], maxWeight)
    bestNode = copy.deepcopy(startNode)
    
    startNode.calcBound()
    tree.append(startNode)
    
    while len(tree) > 0:
        cNode = tree.pop()
        
        if cNode.bound > bestNode.getValue() and cNode.level < len(items):
            withNode = Node(cNode.level + 1, items, cNode.taken[:], maxWeight)
            itemToAdd = items[cNode.level]
        
            if (withNode.getWeight() + itemToAdd.weight) <= maxWeight:
                withNode.addItem(itemToAdd)
                withNode.calcBound()
                
                if withNode.getValue() > bestNode.getValue():
                    bestNode = withNode
                    
                if withNode.bound > bestNode.getValue():
                    tree.append(withNode)
            
            withoutNode = Node(cNode.level + 1, items, cNode.taken[:], maxWeight)
            withoutNode.calcBound()
            if withoutNode.bound > bestNode.getValue():
                tree.append(withoutNode)
    
    
    for item in bestNode.taken:
        print item.name

    
knapsackSolve([Item("1", 45, 3), Item("2", 30, 5), Item("3", 45, 9), Item("4", 10, 5), Item("4", 100, 5)], 16)
