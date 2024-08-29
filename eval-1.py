# Satyam Rathi - 22103125 - OSSLAB eval 1

shop_list = []

def add_item(item: str):
    shop_list.append(item)
    print(f"'{item}' to the shopping list.")


def remove_item(item: str):
    if item in shop_list:
        shop_list.remove(item)
        print(f"Removed '{item}'")
    else:
        print(f"'{item}' is not on the shopping list.")


def display_list():
    print("Current Shopping List:")
    if not shop_list:
        print("- The list is empty.")
    else:
        for item in shop_list:
            print(f"{item}")

def search(shop_list, item_to_find, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if shop_list[mid] == item_to_find:
        return mid
    elif shop_list[mid] < item_to_find:
        return search(shop_list, item_to_find, mid + 1, end)
    else:
        return search(shop_list, item_to_find, start, mid - 1)

def binary_search(shop_list,item_to_find):
    return search(shop_list, item_to_find, 0, len(shop_list) - 1)



def main():
    while True:
        print("\n menu:")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Search Item")
        print("4. Display List")
        print("5. Exit")


        option = input("choice: ")


        if option == "1":
            item = input("Enter the item to add: ")
            add_item(item)

            
        elif option == "2":
            item = input("Enter the item to remove: ")
            remove_item(item)


            
        elif option == "3":
            item = input("Enter the item to search: ")
            print(f"{item} found at : " , binary_search(shop_list, item))
        elif option == "4":
            display_list()
        elif option == "5":
            print("Exiting")
            break
        else:
            print("Invalid.")


main()





