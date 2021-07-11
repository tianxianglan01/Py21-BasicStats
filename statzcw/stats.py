
from typing import List
import math


# ./tt runs the test 
def zcount(list: List[float]) -> float:
    return len(list)

# print("stats test")
# print("zcount should be 5 ==", zcount([1.0,2.0,3.0,4.0,5.0]))

def zmean(list: List[float]) -> float:
    return sum(list) / zcount(list)

def zmode(list: List[float]) -> float:
    return max(set(list), key = list.count)

def zmedian(list: List[float]) -> float:
    sortedLst = sorted(list)
    lstLen = len(list)
    index = (lstLen - 1) // 2
   
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0


def zvariance(list: List[float]) -> float:
	# Number of observations
     n = zcount(list) - 1
     # Mean of the data
     #mean = sum(data) / n
     mean = zmean(list)
     # Square deviations
     deviations = [abs(mean - xi) ** 2 for xi in list]
     # Variance
     variance = sum(deviations) / n
     return variance
     
def zstddev(list: List[float]) -> float:
    return math.sqrt(zvariance(list))

def zstderr(list: List[float]) -> float:
    return zstddev(list) / math.sqrt(len(list))

def zcov(a, b):
    sum = 0
    if len(a) == len(b):
        for i in range(zcount(a)):
            sum += ((a[i] - zmean(a)) * (b[i] - zmean(b)))
    cov = sum/(zcount(a)-1)
    return cov

def zcorr(listx: List[float], listy: List[float]) -> float:
    return zcov(listx, listy) / (zstddev(listx) * zstderr(listy))


def readDataSets(files):
#    print("in readDataSets...", files)
    data = {}
    for file in files:
        twoLists = readDataFile(file)
        data[file] = twoLists
    return data

def readDataFile(file):
    x,y = [], []
    with open(file) as f:
        first_line = f.readline() # consume headers
        for l in f:
            row = l.split(',')
            #print(row, type(row))
            x.append(float(row[0]))
            y.append(float(row[1]))
    return (x,y)
