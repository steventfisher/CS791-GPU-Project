import subprocess
import time
import math

def runJar(numNodes):
    inputFile = "../data/"+ str(numNodes) + ".mat.txt"
    cmdCPU = "./serial_bellman_ford " + inputFile
    cmdGPU = "./cuda_bellman_ford " + inputFile + " 32 32"
    print('*'*50)
    print("Starting Script")
    print('*'*50)
    p = subprocess.Popen(cmdCPU, shell=True)
    p.wait()
    p2 = subprocess.Popen(cmdGPU, shell=True)
    p2.wait()  

if __name__ == '__main__':
    file = open('../data/dataFile.txt', "r+")
    for line in file:
        tmp = line.split('\t')
        numNodes = tmp[2]
        print(numNodes)
        runJar(numNodes)
        print("Done")
        time.sleep(3)
    file.close()
