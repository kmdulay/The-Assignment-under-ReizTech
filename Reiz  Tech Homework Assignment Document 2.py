class Branch:
    BranchList = []
    def __init__(self):
        print ('Let\'s create a new list.\n') 
        self.Branches = Branch.listCreator(self.BranchList)
        print(f'The list created is: {self.Branches}') 
        print(f'Let\'s check how deep this list goes. \nThe max depth is: {Branch.depthChecker (self.Branches)}')

    def listCreator (theList):
        return [[[1]] , [[[4],  [[5], 4], 3]]] 

    def depthChecker(theList):
        holder = [] #store depth of each sublist in the original list
        for item in theList:
            if isinstance(item, list): #if a "sub list" is found in the original list being checked, it will run the recursion and add the "depth value" to the holder list for this node.  
                holder.append(Branch.depthChecker(item))
        if len(holder) > 0:
            return 1 + max(holder) #returns the highest of the depths stored in holder then adds one to compensate for the "starter node"
        return 1
    

Branch()


