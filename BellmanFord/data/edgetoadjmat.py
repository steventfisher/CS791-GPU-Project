import sys
import random
import subprocess
import os
import glob
import numpy


def parser(currList):
    #adjMat = numpy.zeros(shape=(10, 10))
    for file in currList:
        df = open(file, "r+")
        tmpName = file.split('.')
        outputName = tmpName[0] + ".mat.txt"
        n = int(tmpName[0])
	print(n)
        df2 = open(outputName, "a+")
        #numpy.resize(adjMat, (n, n))
        #adjMat = numpy.zeros(adjMat)
        #adjMat = numpy.zeros(shape=(n, n)).astype(int)
        adjMat = numpy.zeros((n, n)).astype(int)
        #adjMat = adjMat.astype(int)
        for line in df:
            left = line.split('\t')
            if left[0] == 'EDGES':
                print("TOP")
            elif left[0] == 'NODES':
                df2.write(left[1].strip() + "\n")
                #adjMat[0][0] = int(left[1])
            else:
                ran = random.randint(1,5)
                tmpran = str(ran).split('.')
                adjMat[int(left[1].strip())][int(left[2].strip())] = tmpran[0]
        
        '''for i in range(n):
            for j in range(n):
                if j == (n-1):
                    tmpVal = str(adjMat[i][j]).split('.')
                    df2.write(tmpVal[0] + "\n")
                else:
                    tmpVal = str(adjMat[i][j]).split('.')                    
                    df2.write(tmpVal[0] + "\t")'''
        adjMat1 = numpy.int_(adjMat)
        #print(adjMat1)
        numpy.savetxt(df2, adjMat1, fmt='%i', delimiter="\t")
        del adjMat
        df.close()
        df2.close()
        p = subprocess.Popen("rm " + file, shell=True)

if __name__ == '__main__':
    currlist = glob.glob("*.brite")
    currlist2 = currlist[0:2]
    parser(currlist)
    #print(currlist2)
