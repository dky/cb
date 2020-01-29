# Original
# A => B => C => D => 0
# Reverse
# D => C => B => A => 0

# Reversed arrows
# A => B => C => D => 0

# In this example:
# A => B => C => D => 0

# prev = A
# cur = B

# https://www.youtube.com/watch?v=xFuJI29BiDY


def reverse_iterative(self):
    prev = None
    cur = self.head
    # while cur is not none (not null or end of list)
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = cur.next
    self.head = prev
