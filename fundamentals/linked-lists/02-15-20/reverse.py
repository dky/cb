from LinkedLIst import LinkedList

# 1 => 2 => 3
# 3 => 2 => 1

# Edge cases
# None
# Single node
#  1 =>

# cur = 1
# prev = None
# next = 2


def reverseLinkedList(head):
    cur = head
    prev = None

    while cur:
        # already updated cur.next, lost pointer to next element.
        # cur.next = prev
        # prev = cur
        # cur = cur.next
        next = cur.next
        cur.next = prev
        prev = cur
        cur = next
