def nodes(lst):
    return {"a": lst, "b": None}
def num(start, index, lst):
    my_node = nodes(lst)
    if index == 0:
        my_node["b"] = start
        return my_node
    now = start
    for i in range(index - 1):
        if now is None:
            return None
        now = now["b"]
    if now is None:
        return None
    my_node["b"] = now["b"]
    now["b"] = my_node
    return start
def show(start):
    now = start
    result = []
    while now:
        result.append(now["a"])
        now = now["b"]
    return result
# Function to delete element at specified index
def delete(start, index):
    if start is None:
        return None
    if index == 0:
        return start["b"]
    temp = start
    for _ in range(index - 1):
        if temp["b"] is None:
            return start
        temp = temp["b"]
    if temp["b"] is None:
        return start
    temp["b"] = temp["b"]["b"]
    return start
# Function to get the size of the linked list
def get_size(start):
    size = 0
    current = start
    while current:
        size += 1
        current = current["b"]
    return size
# Function to check if the linked list is empty
def is_empty(start):
    return start is None
#Function to rotate the  linked list y k positions to the right 
def rotate_right(start, k):
    if start is None:
        return None
    size = get_size(start)
    k %= size
    if k == 0:
        return start
    tail = start
    for _ in range(size - k - 1):
        tail = tail["b"]
    new_head = tail["b"]
    tail["b"] = None
    start = new_head
    new_tail = start
    while new_tail["b"] is not None:
        new_tail = new_tail["b"]
    new_tail["b"] = None
    return start
# Function to reverse the linked list
def reverse(start):
    before = None
    after = start
    while after:
        nxt = after["b"]
        after["b"] = before
        before= after
        after = nxt
    return before
