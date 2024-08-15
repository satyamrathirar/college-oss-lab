#sorted(lst, key=len) : sorts a list and returns a new list.,
#sort int just using sorted and reverse = true for desc order.
def lensort(list):
    return sorted(list, key=len)
def main():
    list=["apple","mango","banana","watermelon","ok"]
    sorted_words = lensort(list)
    print(sorted_words)
    
main()