def group(list,size):
    list2=[]
    for i in range(0,len(list),size):
        list2.append(list[i:i+size])
    return list2

def main():
    list=[1,2,3,4,5,6,7,8,9,10]
    size=int(input("enter the size of the smaller blocks : "))
    print(group(list,size))
main()