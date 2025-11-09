import time
import sys
from backgrounds import *

def move1(list):
    ans =[]
    for item in list:
        if item:
            ans.append(item[1:]+item[0])
    return ans

layer1List = layer1.split("\n")
layer2List = layer2.split("\n")
layer3List = layer3.split("\n")

looper=1


while True:
    sys.stdout.write("\033[H")
    for ind , i in enumerate(layer1List):
        if " " in i:
            for spaceindex in range(len(i)):
                if i[spaceindex] ==" ":
                    if layer2List[ind]:
                        if layer2List[ind][spaceindex] !=" ":
                            sys.stdout.write(layer2List[ind][spaceindex])
                        elif layer3List[ind]:
                            sys.stdout.write(layer3List[ind][spaceindex])
                else:
                    sys.stdout.write(i[spaceindex])
            sys.stdout.write("\n")
        else:
            sys.stdout.write( i +"\n")
    sys.stdout.flush()
    if looper %2==0:
        layer1List = move1(layer1List)
    if looper %5 ==0:
        layer2List = move1(layer2List)
    if looper %20 ==0:
        layer3List = move1(layer3List)
    time.sleep(0.01)
    looper +=1

    