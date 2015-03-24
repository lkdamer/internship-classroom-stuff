class Node():
    def __init__(self, val, nxt):
        self.val = val
        self.nxt = nxt

def func(circ_size, start_per, num_skip):
    if start_per > circ_size:
        return "Bad input."
    current = False
    last = Node(circ_size, False)
    current = last
    people = range(circ_size-1)
    people.reverse()
    for i in people:
        current = Node(i + 1, current)
    last.nxt = current
    while current.val != start_per:
        current = current.nxt
    while current.nxt != current:
        for i in range(num_skip):
            current = current.nxt
        current.nxt = current.nxt.nxt
    return current.val

print func(12, 6, 3)
