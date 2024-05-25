arr = []

def num(i, val):
    arr.insert(i, val)

def delete(i):
    del arr[i]

def get_length():
    return len(arr)

def is_empty():
    return len(arr) == 0

def rotate_right(k):
    n = len(arr)
    k %= n
    arr[:] = arr[-k:] + arr[:-k]

def reverse():
    global arr
    arr = arr[::-1]

def add_end(val):
    arr.append(val)

def add_start(val):
    global arr
    arr = [val] + arr

def merge(arr2):
    arr.extend(arr2)

def mid():
    if len(arr) % 2 == 0:
        return None
    else:
        return arr[len(arr) // 2]
#Example Here:
add_end(5)
add_end(15)
add_end(25)
add_end(35)

print("Initial dynamic array:", arr)

num(2, 25)
print("Inserting elemnt=25 at index 2:", arr)

delete(1)
print("Deleting element at index 1:", arr)

print("Length of dynamic array:", get_length())
print("Is dynamic array empty?\n", is_empty())

rotate_right(2)
print("Rotating the dynamic array by 2 positions to the right:", arr)

reverse()
print("Reversing the dynamic array:", arr)

add_start(5)
print("After adding 5 at the start of the dynamic array:", arr)
print("Mid element of the dynamic array:", mid())