#Abed Islam Ai1138 I attempted to do the foward and back tracking along with io handiling
import operator
import collections
import random
import copy
#the nodes represent the pieces of boards
class Node:
   

    def __init__ (self, data = 0, position = None, up  = None , down  = None, left  = None, right  = None, next = None) :
        self.data = data               
        self.position = position                
        self.up= up                 
        self.down  = down               
        self.left = left               
        self.right= right              
        self.next  = next               
        self.domain= [1, 2, 3, 4, 5]    
        self.constraintsDict = {}                

    def hasANext (self):
        return self.next != None;
#the board class
class Board:
    def __init__ (self, boardLst, horizContraintLst = [], vertContraintLst = [] ):

        self.board_Lst = board_Lst
        self.horizContraint = horizContraint
        self.vertContraint = vertContraint

        self.p11 = Node(position = 11);
        self.p12 = Node(position = 12);
        self.p13 = Node(position = 13);
        self.p14 = Node(position = 14);
        self.p15 = Node(position = 15);
        self.p21 = Node(position = 21);
        self.p22 = Node(position = 22);
        self.p23 = Node(position = 23);
        self.p24 = Node(position = 24);
        self.p25 = Node(position = 25);
        self.p31 = Node(position = 31);
        self.p32 = Node(position = 32);
        self.p33 = Node(position = 33);
        self.p34 = Node(position = 34);
        self.p35 = Node(position = 35);
        self.p41 = Node(position = 41);
        self.p42 = Node(position = 42);
        self.p43 = Node(position = 43);
        self.p44 = Node(position = 44);
        self.p45 = Node(position = 45);
        self.p51 = Node(position = 51);
        self.p52 = Node(position = 52);
        self.p53 = Node(position = 53);
        self.p54 = Node(position = 54);
        self.p55 = Node(position = 55);

        self.Row1  = [self.p11,self.p12,self.p13,self.p14,self.p15]
        self.Row2  = [self.p21,self.p22,self.p23,self.p24,self.p25]
        self.Row3  = [self.p31,self.p32,self.p33,self.p34,self.p35]
        self.Row4  = [self.p41,self.p42,self.p43,self.p44,self.p45]
        self.Row5  = [self.p51,self.p52,self.p53,self.p54,self.p55]

        self.Col1  = [self.p11,self.p21,self.p31,self.p41,self.p51]
        self.Col2  = [self.p12,self.p22,self.p32,self.p42,self.p52]
        self.Col3  = [self.t13,self.t23,self.t33,self.t43,self.t53]
        self.Col4  = [self.t14,self.t24,self.t34,self.t44,self.t54]
        self.Col5  = [self.t15,self.t25,self.t35,self.t45,self.t55]

        self.Rows  = [self.Row1, self.Row2, self.Row3, self.Row4, self.Row5]
        self.Cols  = [self.Col1, self.Col2, self.Col3, self.Col4, self.Col5]

        self.nodesContainer = [self.p11,self.p12,self.p13,self.p14,self.p15,
                         self.p21,self.p22,self.p23,self.p24,self.p25,
                         self.p31,self.p32,self.p33,self.p34,self.p35,
                         self.p41,self.p42,self.p43,self.p44,self.p45,
                         self.p51,self.p52,self.p53,self.p54,self.p55]

        

    def constructBoard(self):
        for row in self.Rows:
            for  i in range(len(row)):
                if i < (len(lst) - 1):
                    row[i].right = row[i+1];
                    row[i].next  = row[i+1];

                if  i > 0 :
                    row[i].left = row[i-1];
        for i in range (5) :
            self.Row2[i].up   = self.Row1[i];
            self.Row3[i].up   = self.Row2[i];
            self.Row4[i].up   = self.Row3[i];
            self.Row5[i].up   = self.Row4[i];
            self.Row1[i].down = self.Row2[i];
            self.Row2[i].down = self.Row3[i];
            self.Row3[i].down = self.Row4[i];
            self.Row4[i].down = self.Row5[i];

        for i in range( len(self.Col5) ):
            if (i != (len(self.Col5) - 1) ):
                self.Col5[i].next = self.Col1[i+1];

    def fillBoardFromLst (self, input):
        for i in range(len(input)):
            self.nodesContainer[i].data = input[i];

    def addConstraintsHori(self, lst):
        horiz1 = lst[0 : 4]
        horiz2 = lst[4 : 8]
        horiz3 = lst[8 : 12]
        horiz4 = lst[12 : 16]
        horiz5 = lst[16 : 20]

        
        for i in range(len(horiz1)):
            if str(horizContraints1[i]) in "<>":
                self.Row1[i].constraintsDict["lhs"]   = horiz1[i];
                self.Row1[i+1].constraintsDict["rhs"] = horiz1[i];

        for i in range(len(horiz2)):
            if str(horizContraints2[i]) in "<>":
                self.Row2[i].constraintsDict["lhs"]   = horiz2[i];
                self.Row2[i+1].constraintsDict["rhs"] = horiz2[i];

        for i in range(len(horiz3)):
            if str(horizContraints3[i]) in "<>":
                self.Row3[i].constraintsDict["lhs"]   = horiz3[i];
                self.Row3[i+1].constraintsDict["rhs"] = horiz3[i];

        for i in range(len(horiz4)):
            if str(horizContraints4[i]) in "<>":
                self.Row4[i].constraintsDict["lhs"]   = horiz4[i];
                self.Row4[i+1].constraintsDict["rhs"] = horiz4[i];

        for i in range(len(horiz5)):
            if str(horizContraints5[i]) in "<>":
                self.Row5[i].constraintsDict["lhs"]   = horiz5[i];
                self.Row5[i+1].constraintsDict["rhs"] = horiz5[i];

    def addConstraintsVerti(self, vertConstraint):
        vert1 = vertConstraint[0 : 5]
        vert2 = vertConstraint[5 : 10]
        vert3 = vertConstraint[10 : 15]
        vert4 = vertConstraint[15 : 20]

        for i in range( len(vert1) ):
            if str(vert1[i]) in "^v":
                self.Row1[i].constraintsDict["uhs"] = vert1[i];
                self.Row2[i].constraintsDict["dhs"] = vert1[i];

        for i in range( len(vertContraints2) ):
            if str(vert2[i]) in "^v":
                self.Row2[i].constraintsDict["uhs"] = vert2[i];
                self.Row3[i].constraintsDict["dhs"] = vert2[i];

        for i in range( len(vert3) ):
            if str(vert3[i]) in "^v":
                self.Row3[i].constraintsDict["uhs"] = vert3[i];
                self.Row4[i].constraintsDict["dhs"] = vert3[i];

        for i in range( len(vert4) ):
            if str(vert4[i]) in "^v":
                self.Row4[i].constraintsDict["uhs"] = vert4[i];
                self.Row5[i].constraintsDict["dhs"] = vert4[i];

    def addConstraintsFromLsts(self, horizContraintsLst, vertConstraintsLst) :
        self.addConstraintsHori(horizContraintsLst);
        self.addConstraintsVerti(vertConstraintsLst);

    def isComplete(self):
        for node in self.nodesContainer:
            if node.data == 0:
                return False
        return True


#  Forward Check 

def changeColDomains(currNode, board):
    
    colPos = currNode.position%10; 
    for i in range( len(board.Cols) ): 
        if i == (colPos -1):
            for node in board.Cols[i]:
                if currNode.data in node.domain:
                     node.domain.remove(currNode.data);

def channgeRowDomains(currNode, board):
    
    rowPos = int(str(currNode.position)[0]);   
    for i in range(len(board.Rows) ): 
        if i == (rowLoc -1):
            for node in board.Rows[i]:
                 if currNode.data in node.domain:
                    node.domain.remove(currNode.data)

def removeMaxVd(domain, val):
    deleteLst = []
    for item in domain:
        if item >= val:
            deleteLst.append(elem)
    for item in deleteLst:
        domain.remove(elem);


def removeMinVd(domain, val):
   deleteLst = []
    for item in domain:
        if item <= val:
            deleteLst.append(elem)
    for item in deleteLst:
        domain.remove(elem);


def fixLhsInequal(currNode):
    rhs = currNode.right;

    if currNode.data != 0:
        if currNode.constraintsDict["lhs"] == "<" :
            removeMinVd(rhs.domain, currTile.data)
        elif currNode.constraintsDict["lhs"] == ">" :
            removeMaxVd(rhs.domain, currTile.data)
    
    elif currNode.data == 0:
        if rhs.data != 0 :
            if rhs.constraintsDict["rhs"] == "<" :
                removeMaxVd(currTile.domain, rhs.data)
            elif rhs.constraintsDict["rhs"] == ">" :
                removeMinVd(currTile.domain, rhs.data)

def fixUhsInequal(currNode):

    dhs = currNode.down;
    if currNode.data != 0:
        if currNode.constraintsDict["uhs"] == "^" :
            removeMinVd(dhs.domain, currTile.data)
        elif currNode.constraintsDict["uhs"] == "v" :
            removeMaxVd(dhs.domain, currNode.data)
    
    elif currNode.data == 0:
        if dhs.data != 0 :
            if dhs.constraintsDict["dhs"] == "^" :
                removeMaxVd(currNode.domain, dhs.data)
            elif dhs.constraintsDict["dhs"] == "v" :
                removeMinVd(currNode.domain, dhs.data)

def changeInequal(currNode):
    if "lhs" in currNode.constraintsDict:
        fixLhsInequal(currNode)

    if "uhs" in currNode.constraintsDict:
        fixUhsInequal(currNode);

def forwardCheck(board):
    curr = board.p11;
    while curr.hasANext():
        if curr.data != 0:
            changeRowDomains(curr, board);
            changeColDomains(curr, board);
        if ("lhs" in curr.constraintsDict) or ("uhs" in curr.constraintsDict):
            fixInequal(curr);
        curr = curr.next;

#  Backtracking

def peekCol(move,currNode, board):
    
    colLoc = currNode.position%10;             
    for i in range( len(board.Cols) ): 
        if i == (colLoc -1):
            for piece in board.Cols[i]:
                if piece.data == move:
                    return False;
    return True;

def peekRow(move,currNode, board):
   
    rowLoc = int(str(currNode.loc)[0]);  
    for i in range(len(board.Rows)): 
        if i == (rowLoc -1):
            for piece in board.Rows[i]:
                if piece.data == move:
                    return False
    return True;

def checkIneq(move,currNode, board):
    for key, val in currNode.constraintsDict.items():
        if key == "lhs":
            rhs = currNode.right;
            if rhs.data == 0:
                continue
            elif val == ">":
                if move < rhs.data:
                    return False;
            elif val == "<":
                if move > rhs.data:
                    return False;
        
        elif key == "rhs":
            lhs = currNode.left;
            if val == ">":
                if lhs.data < move:
                    return False
            elif val == "<":
                if lhs.data > move:
                    return False;
        
        elif key == "uhs":
            dhs = currNode.down;
            if val == "^":
                if move > dhs.data:
                    return False;
            elif val == "v":
                if move < dhs.data:
                    return False;
        
        elif key == "dhs":
            uhs = currNode.up;
            if val == "^":
                if uhs.data > move:
                    return False;
            elif val == "v":
                if uhs.data < move:
                    return False;
    return True;

def peekMove(move,currNode, board):
   
    if len(currNode.constraintsDict) != 0:
        ineqBool = checkIneq(move,currNode, board)
    colBool = peekCol(move,currNode, board)
    rowBool = peekRow(move,currNode, board)
    if len(currNode.constraintsDict) != 0:
        return (ineqBool==True) and (colBool == True) and (rowBool==True)
    return (colBool == True) and (rowBool==True)

def sortTilesMrv(board):
    mrvDict = {}
    for node in board.nodesContainer:
        mrvDict[node] = len(node.domain)
    sort = sorted(mrvDict.items(), key=operator.itemgetter(1))
    sorted_dict = collections.OrderedDict(sort)
    return sorted_dict

def DegNum(currNode, board):
    rowPos = int(str(currNode.position)[0]);   
    count = 0
    for i in range(len(board.Rows)): 
        if i == (rowPos -1):
            for node in board.Rows[i]:
                if currNode.data == 0:
                    count += 1
    colPos = currNode.loc%10;             
    for i in range( len(board.Cols) ): 
        if i == (colPos -1):
            for node in board.Cols[i]:
                if currNode.data == 0:
                    count += 1;
    return count;

def NodeSort(nodesContainer, board):
    degDict = {}
    for node in board.nodesContainer:
        degDict[node] = DegNum(, board)
    sort = sorted(degDict.items(), key=operator.itemgetter(1))
    sorted_dict = collections.OrderedDict(sort)
    return list(sorted_dict.keys());

def deleteDups(lst):
    dummy = [] 
    for i in lst: 
        if i not in dummy: 
            dummy.append(i) 
    return dummy;

def sortNodes(board):
    tilesMrvSortDict = sortTilesMrv(board);
    lstMrvs = deleteDups(tilesMrvSortDict.values());
    mrvDict = {}
    for mrv in lstMrvs:
        temp = []
        for k,v in tilesMrvSortDict.items():
            if tilesMrvSortDict[k] == mrv:
                temp.append(k)
        mrvDict[mrv] = temp

    for k,v in mrvDict.items():
        k = NodeSort(v, board)

    sortedNode = []
    for k,v in mrvDict.items():
        for node in v:
            sortedNode.append(node)

    return sortedNode;

def getNode(board):
    
    lst = sortNodes(board)
    for node in lst:
        if len(node.domain) != 0 and node.data == 0:
            return node

def Backtracking(board):
    if board.isComplete():
        return True;

    node = getNode(board)

    for move in node.domain:
        if peekMove(move, tile, board):
            tile.data = move;
            oldDomain = copy.deepcopy(tile.domain)
            tile.domain = [];

            res = backTrack(board);
            if res:
                return True;
            
            tile.data = 0;
            tile.domain = oldDomain;

    return False;

# io handling

def fixList(listOfList):
    fixList = [ item for elem in listOfList for item in elem ]
    return fixList;

def fixTypes(lst):
    nums = "012345"
    for i in range(len(lst)):
        if lst[i] in nums:
            lst[i] = int(lst[i]);
    return lst;

def fixInputLst(lstOfLst):
    lst = fixList(lstOfLst)
    lst = fixTypes(lst)
    return lst;

def getBoards(file):
    
    boardLst = []
    horizBoardLst = []
    vertBoardLst = []
    
    counter = -1;
    flines = file.readlines();

    for i in flines:
        
        counter+=1;
        
        if counter < 5:
            boardLst.append(i.strip().split(" "));

        elif (counter < 11) and (counter > 5):
            horizBoardLst.append(i.strip().split(" "));

        elif (counter < 16) and (counter > 11):
            vertBoardLst.append(i.strip().split(" "));
    
    boardLst = fixInputLst(boardLst)
    horizBoardLst = fixInputLst(horizBoardLst)
    vertBoardLst = fixInputLst(vertBoardLst)

    return (boardLst, horizBoardLst, vertBoardLst )

def solveBoard(file):
    lst1, lst2, lst3 = getBoardsFromInputFile(file)
    board1 = Board(boardLst = lst1, horizContraint = lst2, vertContraint = lst3 );
    forwardCheck(board1);
    if (Backtracking(board1)):
        return board1;
    else:
        return False    

def outputFile(outFile, solutionBoard):
    if type(solutionBoard) == bool:
        outFile.write("No Solution")
    else:
        outFile.write(str(solutionBoard))

def main():
    f1 = open("Input1.txt", "r");
    f2 = open("Input2.txt", "r");
    f3 = open("Input3.txt", "r");
    solutionBoard1 = solveBoard(f1)
    solutionBoard2 = solveBoard(f2)
    solutionBoard3 = solveBoard(f3)
    o1 = open("Output1.txt","w+");
    o2 = open("Output2.txt","w+");
    o3 = open("Output3.txt","w+");
    outputFile(o1, solutionBoard1)
    outputFile(o2, solutionBoard2)
    outputFile(o3, solutionBoard3)

main();

