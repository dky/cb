# 1 => 2 => 3
# 3 => 2 => 1

# None
# 1 =>

# next - 2, 3
# cur.next - None, 1
# prev - None, 2
# cur - 1

# 1 => None, 2 => 3

def reverseLinkedList(head):
    cur = head
    prev = None

    # 1 => None, 2 => 3
    # 2 => 1 => None 

    while cur:
        next = cur.next # 2 (1 => 2), 3 (2 => 3)
        cur.next = prev # None (1 => None), 1 (2 => 1)
        prev = cur # 1, 2
        cur = next # 2, 3

    return prev # At the end of the loop = 3.
