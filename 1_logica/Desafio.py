def micro_grupos(pessoas, amizades):
    #Creates am object with an id and its relationship to others objects represented by their ids
    class Membro:
        def __init__(self, id):
            self.id = id
            self.relações = []
        def nova_relação(self, friend):
            if self.relações.count(friend) == 0: self.relações.append(friend) #Only counts each unique relationship


    groups = []
    membrosDictionary = {}
    uniqueInTree = []                                #Unique relation in the tree

    def tree_navigator (relationTree):               #Uses recursion to navigate a relationship tree by going through each member, exploring their relations and saving each unique one
        for i in relationTree:
            if uniqueInTree.count(i) == 0: 
                uniqueInTree.append(i)
                tree_navigator(membrosDictionary[i].relações)
        uniqueInTree.sort()                         #Then sorts the tree so that it can assure to be unique
        return uniqueInTree


    for i in range(1, pessoas + 1):                  #Produces a dictionary containg each member and their respective object 
        membrosDictionary[i] = Membro(i)             

    for relationship in amizades:                    #Assing each relation described by "amizades"
        membrosDictionary[relationship[0]].nova_relação(relationship[1])
        membrosDictionary[relationship[1]].nova_relação(relationship[0])

    searchesTodo = []
    searchesTodo.extend(membrosDictionary.keys())

#Navigates the tree by calling a subroutine, assinings found tree to "groups", removing explored objects from the list of searches to do, and then clearing the buffer
    for id in searchesTodo:
        tree_navigator (membrosDictionary[id].relações)
        if groups.count(uniqueInTree) == 0: 
            groups.extend([uniqueInTree.copy()])
            for i in uniqueInTree: searchesTodo.remove(i)
        uniqueInTree.clear()

    return len(groups)

print (micro_grupos(7, [[1,2],[2,3],[3,1],[3,4],[6,5],[5,7]])) #Expected output: 2
