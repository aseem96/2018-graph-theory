

def printMatrix(matrix):
    for item in matrix:
        print item

def createMatrix(size):
    toReturn = []
    for i in range(size):
        newRow = []
        for j in range(size):
            if i == j:
                newRow.append(0)
            else:
                newRow.append(1)
        toReturn.append(newRow)

    # toReturn[0][1] = 0
    # toReturn[1][0] = 0
    return toReturn

def matrixDeepCopy(matrix):
    toReturn = []
    for i in range(len(matrix)):
        newRow = []
        for item in matrix[i]:
            newRow.append(item)
        toReturn.append(newRow)
    return toReturn

def deepCopyPathList(list):
    toReturn = []
    for item in list:
        toReturn.append(item)
    return toReturn



def findPathsRecursive(numberOfPaths, paths, matrix, walkLength, startVertexArray, startVertex, endVertex, finalWalkLength):
    verticesToVisit = []
    index = startVertexArray[len(startVertexArray) - 1]
    for i in range(len(matrix[startVertexArray[len(startVertexArray) - 1]])):
        if matrix[index][i] != 0:
            verticesToVisit.append(i)

    for item in verticesToVisit:
        newMatrix = matrixDeepCopy(matrix)
        newList = deepCopyPathList(startVertexArray)
        newList.append(item)
        if item == endVertex and walkLength == finalWalkLength:
            numberOfPaths = numberOfPaths + 1
            startVertexArray.append(item)
            paths.append(startVertexArray)
        elif walkLength < finalWalkLength:
            newMatrix[startVertex][item] = newMatrix[startVertex][item] - 1
            newMatrix[item][startVertex] = newMatrix[item][startVertex] - 1

            numberOfPaths, paths = findPathsRecursive(numberOfPaths, paths, newMatrix, walkLength + 1, newList, item, endVertex, finalWalkLength)



    return numberOfPaths, paths



def getNumberOfPaths(matrix, startVertex, endVertex, finalWalkLength):
    finalPaths = []
    finalNumberOfPaths = 0
    stepOneArray = []
    for i in range(len(matrix[startVertex])):
        if matrix[startVertex][i] != 0:
            stepOneArray.append(i)

    for i in range(len(matrix[startVertex])):
        if i in stepOneArray:
            newMatrix = matrixDeepCopy(matrix)
            # newMatrix[startVertex][i] = newMatrix[startVertex][i] - 1
            # newMatrix[i][startVertex] = newMatrix[i][startVertex] - 1
            startVertexArray = [startVertex, i]
            numberOfPaths, paths = findPathsRecursive(0, [], newMatrix, 2, startVertexArray, startVertex, endVertex, finalWalkLength)
            finalNumberOfPaths = finalNumberOfPaths + numberOfPaths
            for line in paths:
                finalPaths.append(line)
    return finalNumberOfPaths, finalPaths






# printMatrix(newMatrix)
print("")
for i in range(2,10):
    newMatrix = createMatrix(i)
    numberOfPaths, paths = getNumberOfPaths(newMatrix, 0, 1, 3)
    print i, numberOfPaths
    # for path in paths:
    #     print path
print("")
# printMatrix(newMatrix)


go = 3
newMatrix = createMatrix(go)
numberOfPaths, paths = getNumberOfPaths(newMatrix, 0, 1, 3)
print go, numberOfPaths
for path in paths:
    print path
