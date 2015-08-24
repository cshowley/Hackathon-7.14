import random
import matplotlib.pyplot as plt
import datetime
import numpy as np

# Start with a 5 hour window with zero congestion and start appending files to certain times to download
# according to their sizes. Make up an estimated time to download, say, 100 Mb/minute
def getBaseData():
# Create PERMANENT historical data to build our downloaded data off of
    baseData = [5.5e9, 5.6e9, 5.2e9, 4.3e9, 3.2e9, 2.5e9, 2.8e9, 3.0e9, 3.2e9, 3.5e9, 3.6e9, 3.6e9, 3.7e9, 3.8e9, 3.9e9, 4.0e9, 4.1e9, 4.3e9, 4.3e9, 4.9e9, 5.1e9, 5.4e9, 5.5e9, 5.4e9]
    new_baseData = []
    for i in baseData:
        i = i * 1
        new_baseData.append(i)
    
    """
    plt.figure()
    plt.bar(range(len(new_baseData)),new_baseData)
    plt.axis([0,24,0,7.5e9])
    plt.xlabel('Time (Hours)')
    plt.ylabel('Network Traffic (Bytes)')
    """

    return new_baseData
    
#---------------------------------------------------------------------------------------------------------

def originalNetworkData(new_baseData,number):
    # Create historical data ONLY for the files that have been scheduled to download
    #with open("C:/Users/cshowley/Desktop/historicalData.txt","w") as data:
    with open("/Users/cshowley/Desktop/historicalData.txt","w") as data:
        for i in range(number):
            data.write('%s\n' % (0.1e8*random.random()))
    
    # Import historical data
    fileSizes = []
    #with open("C:/Users/cshowley/Desktop/historicalData.txt","r") as data:
    with open("/Users/cshowley/Desktop/historicalData.txt","r") as data:
        for line in data.readlines():
            fileSizes.append([])
            for i in line.strip('\n').split(','):
                fileSizes[-1].append(i)
    
    dataSize = np.zeros(shape=(24))
    file = []
    for element in fileSizes:
        dataSize[24*random.random()] += float(element[0])
        file.append(float(element[0]))
    
    
    
    extra = []
    for i in range(300):
        foo = float(0.1e8*random.random())
        extra.append(foo)
        
    for foo in extra:
        print foo
        dataSize[5*random.random()] += foo
        file.append(foo)
    
    
    
        
    
    finalData = []
    for i in range(len(dataSize)):
        foo = dataSize[i] + new_baseData[i]
        finalData.append(foo)
    
    
    plt.figure()
    p1 = plt.bar(range(len(dataSize)),new_baseData,color='b')
    p2 = plt.bar(range(len(dataSize)),dataSize,color='r',bottom=new_baseData)
    p2[0].set_color('r')
    p2[1].set_color('r')
    p2[2].set_color('r')
    p2[3].set_color('r')
    p2[4].set_color('r')
    foo = len(dataSize) * [max(finalData)]
    length = range(0,24)
    plt.plot(length,foo,'--')
    plt.axis([0,24,0,7.5e9])
    plt.title('Data Congestion Before Download Manager')
    plt.xlabel('Time (Hours)')
    plt.ylabel('Network Traffic (Bytes)')
    

    return file,foo,length

    #---------------------------------------------------------------------------------------------------------

# Reorder the downloads according to the lowest traffic per hour during the free period
def newNetworkData(new_baseData,file,foo,length):
    dataSize = np.zeros(shape=(24))
    unixTime = []
    for elements in file:
        lowestTraffic, index = min((lowestTraffic, index) for (index, lowestTraffic) in enumerate(dataSize[0:5] + new_baseData[0:5]))
        dataSize[index] += float(elements)
        if index == 0:
            unixTime.append(1405666800)
        elif index == 1:
            unixTime.append(1405670400)
        elif index == 2:
            unixTime.append(1405674000)
        elif index == 3:
            unixTime.append(1405677600)
        elif index == 4:
            unixTime.append(1405681200)
    
       
    plt.figure() 
    p3 = plt.bar(range(len(dataSize)),new_baseData,color='b')
    p4 = plt.bar(range(len(dataSize)),dataSize,color='r',bottom=new_baseData)
    p4[0].set_color('r')
    p4[1].set_color('r')
    p4[2].set_color('r')
    p4[3].set_color('r')
    p4[4].set_color('r')
    plt.plot(length,foo,'--')
    plt.axis([0,24,0,7.5e9])
    plt.title('Data Congestion After Download Manager')
    plt.xlabel('Time (Hours)')
    plt.ylabel('Network Traffic (Bytes)')

    return unixTime

new_baseData = getBaseData()
file,foo,length = originalNetworkData(new_baseData,700)
unixTime = newNetworkData(new_baseData,file,foo,length)
plt.show()


#with open("C:/Users/cshowley/Desktop/downloadTimes.txt","w") as data:
with open("/Users/cshowley/Desktop/downloadTimes.txt","w") as data:
    for lines in unixTime:
        data.write('%s\n' % lines)




