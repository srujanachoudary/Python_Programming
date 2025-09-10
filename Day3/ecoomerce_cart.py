def add(x, arr):
    arr = arr + [0]
    arr[len(arr)-1] = x
    return arr

def remove(x, arr):
    if x in arr:
        q = arr.index(x)
        for w in range(q, len(arr)-1):
            arr[w] = arr[w+1]
        arr = arr[:-1] 
    else:
        print(f"{x} is not in the list")
    return arr

def search(x, arr):
    if x in arr:
        print(f"{x} is found at index:", arr.index(x))
    else:
        print(f"{x} is not in the list")

def count(list):
    return len(list)

def sorting(list):
    return sorted(list)

def clear(list):
    del list
    print('list is cleared')

def display(arr):
    print("Current list:", arr)

arr = ["a", "b", "c", "d", "e"]
while True:
    print("\n--- Menu ---")
    print("1. Add")
    print("2. Remove")
    print("3. Search")
    print("4. Display")
    print("5. count")
    print("6. Sort the items")
    print("7. Clear")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        val = input("Enter element to add: ")
        arr = add(val, arr)
    elif choice == 2:
        val = input("Enter element to remove: ")
        arr = remove(val, arr)
    elif choice == 3:
        val = input("Enter element to search: ")
        search(val, arr)
    elif choice == 4:
        display(arr)
    elif choice == 5:
        print("Total products in the cart are: ",count(arr))
    elif choice == 6:
        arr=sorting(arr)
        print("after sorting:",arr)
    elif choice == 7:
        clear(arr)
    elif choice == 8:
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Try again.")
