def stat(x):
    totalsum=0
    for x in data:
        totalsum=totalsum+x
    N=len(data)
    mean=totalsum/N
    return totalsum,mean

data=[1,4,5,7,3,8]
totalsum,mean=stat(data)
print("total sum=",totalsum)
print("mean =",mean)
