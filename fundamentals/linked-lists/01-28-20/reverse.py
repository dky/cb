# 1 => 2 => 3

# None
# 1 =>

# cur = 1 cur.next = None
# prev = None
# Next = 2


def reverseLinkedList(head):
    cur = head
    prev = None

    # while cur:
    # cur.next = prev
    # prev = cur
    # cur = cur.next

    while cur:
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next

    return prev
