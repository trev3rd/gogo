def main():


def getIterations():
    return int(input("How many number will you add")







def getAverage(y):
    firstList=[]

    for a in range(0,y):
        testscore=int(input("enter your test score"))
        firstList.append(testscore)

    firstList.append(100)
    lengthofList= len(firstList)
    sum=0
    print("the number you entered were:", end="  ")
    for c in range(0, lengthofList):
        print(firstList[c], end="  ")
        sum=sum+firstList[c]
    print("")
    print("the average of your number is ")

main()