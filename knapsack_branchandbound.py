class Item:
    def __init__(self, name, value, weight):
        self.name = name
        self.weight = weight
        self.value = value
    
    def getRatio(self):
        return self.value/float(self.weight)
        
    def __str__(self):
        return self.name
        
    def __repr__(self):
        return self.name


class Node:
    def __init__(self, level, items, takenItems, maxWeight):
        self.level = level
        self.allItems = items
        self.maxWeight = maxWeight
        self.taken = takenItems
        self.bound = 0

    
    def getWeight(self):
        return sum([item.weight for item in self.taken])
    

    def getValue(self):
        return sum([item.value for item in self.taken])
    
    
    def addItem(self, item):
        self.taken.append(item)


    def calcBound(self):
        # For all upcoming items calc it as a fractional
        cWeight = self.getWeight()
        self.bound = self.getValue()
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
        cNode = tree.pop(0)
        
        print str(cNode.bound) + " --- " + str(bestNode.getValue())
        print cNode.taken
        if cNode.bound > bestNode.getValue() and cNode.level < len(items):
            print "+"
            
            withNode = Node(cNode.level + 1, items, cNode.taken[:], maxWeight)
            itemToAdd = items[cNode.level]
        
            if (withNode.getWeight() + itemToAdd.weight) <= maxWeight:
                withNode.addItem(itemToAdd)
                withNode.calcBound()
                
                if withNode.getValue() > bestNode.getValue():
                    bestNode = withNode
                    
                if withNode.bound > bestNode.getValue():
                    print "with " + itemToAdd.name + " (%d)" % (withNode.bound)
                    tree.append(withNode)
            
            withoutNode = Node(cNode.level + 1, items, cNode.taken[:], maxWeight)
            withoutNode.calcBound()
            if withoutNode.bound > bestNode.getValue():
                print "without " + itemToAdd.name + " (%d)" % (withoutNode.bound)
                tree.append(withoutNode)
    
    
    for item in bestNode.taken:
        print item.name

    
knapsackSolve([Item("A", 45, 3), Item("B", 30, 5), Item("C", 45, 9), Item("D", 10, 5)], 16)
