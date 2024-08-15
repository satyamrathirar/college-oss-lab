def duplicate(list):
    print("duplicate function : ",end="\n")
    dict = {}
    for i in list:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
            
    duplicates = [num for num,count in dict.items() if count>1]
    return duplicates

def main():
    list=[1,2,3,3,1,2,5,6,7,6] 
    print(duplicate(list))
main()