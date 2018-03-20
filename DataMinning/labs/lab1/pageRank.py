#!/usr/env/bin python3
#v' = beta * M * v + (1-beta)e/n

class PageRank(object):
    def __init__(self,pageGraph,sortArray):
        self.factor_Beta = 0.8

        #type：dict
        self.pageGraph = pageGraph
        # type：list
        self.searchIndex = sortArray

        #init the orginal rank Vector to [1/length,1/length,1/length,1/length,,,,,,]
        self.rankVector = [1/len(pageGraph) for i in range(0,len(pageGraph))]

        self.matrix = []

        #init matrix here
        for key,value in self.pageGraph.items():
            self.matrix.append([0 for i in range(len(self.pageGraph))])

            average = 1 / len(value)
            for link_item in value:
                self.matrix[self.__nameToIndex(key)][self.__nameToIndex(link_item)] = average

        self.currentRankVector = []

        self.util = MatrixUtils()

    def cal(self,times):
        #v' = beta * M * v + (1-beta)e/n
        v = self.rankVector.copy()
        M = self.util.transMatrix(self.matrix.copy())

        beta = self.factor_Beta
        n = len(self.rankVector)
        e = self.util.getUnitVector(n)

        part2_factor = (1 - beta) / n
        part2 = self.util.vectorCrossVector(e, [part2_factor, ])

        for i in range(0,times):
            part1 = self.util.vectorCrossVector([beta,],self.util.matrixCrossVector(M,v))
            v = self.util.vectorPlus(part1,part2)
            print(v)
        self.currentRankVector = v

    def printGraph(self):
        for ele in self.pageGraph:
            print(ele,self.pageGraph[ele])

    def printOriginalRankVector(self):
        print(self.rankVector)

    def printNowRankVector(self):
        print(self.currentRankVector)

    def printMatrix(self):
        for vect in self.util.transMatrix(self.matrix):
            print(vect)

    def __nameToIndex(self,info):
        return self.searchIndex.index(info)


class MatrixUtils(object):
    def __init__(self):
        pass

    def getUnitVector(self,rowNum):
        return [1 for i in range(0,rowNum)]

    def transMatrix(self,matrix):
        try:
            if type(matrix) != list and type(matrix[0]) != list:
                return -1
        except:
            print(matrix,"matrix type ERROR")
            return -1

        rows = len(matrix)
        cols = len(matrix[0])

        tMatrix = []

        for newRow in range(0,cols):
            row = []
            for oldRow in matrix:
                row.append(oldRow[newRow])
            tMatrix.append(row)
        return tMatrix

    def vectorCrossVector(self,vector1,vector2):
        if len(vector1) != 1 and len(vector2) != 1 and len(vector1) != len(vector2):
            return -1
        if len(vector1) == 1:
            result = []
            index = 0
            for item in vector2:
                result.append(item * vector1[0])
            return result

        if len(vector2) == 1:
            result = []
            for item in vector1:
                result.append(item * vector2[0])
            return result

        index = 0
        result = 0
        for item in vector1:
            result += item*vector2[index]
            index += 1
        return result

    def matrixCrossVector(self,matrix,vector):
        if len(matrix) != len(vector):
            return -1
        result = []

        for row in matrix:
            result.append(self.vectorCrossVector(row,vector))

        return result

    def vectorPlus(self,vector1,vector2):
        try:
            if len(vector1) != len(vector2):
                return -1
        except:
            print("vectors type Error, no len() function")

        result_vector = []

        index = 0
        for item in vector1:
            result_vector.append(item + vector2[index])
            index += 1
        return result_vector