'''Basic Array related operations'''


'''To find the number of items in a for a non-nested list'''
def length(L):
    i = 0
    while True:
        try:
            L[i]
        except IndexError:
            print("Total Number of elements = ", i)
            break
        i += 1
            
'''To find if the list is empty'''
def is_empty(L):
    try:
        L[0]
    except:
        print("Empty list")
    else:
        print("Not an empty list")

'''To find the item at a given index'''
def is_present(L, index, item):
    if(index < len(L)):
        if(L[index] == item):
            return True
    return False

'''To push an item at a particular index'''
def push_item(L, index, item):
    length = len(L)
    if(index == length or length == 0):
         L.append(item)
         print("New list ", L)
    elif(index < length):
        for i in range(length, index, -1):
            try:
                L[i] = L[i-1]
            except IndexError:
                L.append(L[i-1])
        L[index] = item
        print("New list ", L)
    else:
        print("Index out of range")

'''To insert an item at 0th index'''
def push_beg(L, item):
    length = len(L) -1
    if(length == -1):
        L.append(item)
    else:
        for i in range(length, -1, -1):
            try:
                L[i+1] = L[i]
            except:
                L.append(L[i])
        L[0]= item
    print("New List ", L)


'''To find if an item is present and return the indices of the item if present in mutiple places'''
def find(L, item):
    #Use binary or Linear Search
    pass


