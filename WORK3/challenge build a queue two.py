from collections import deque

# 1) create an empty queue
canteen_queue = deque()          # step 1

# 2) enqueue arrivals
canteen_queue.append("Alice")    # Alice arrives -> goes to the back
canteen_queue.append("Bob")      # Bob arrives -> goes to the back
canteen_queue.append("Clara")    # Clara arrives

# 3) serve (dequeue) from the front
served = canteen_queue.popleft() # serve the person at the front (Alice)
print("Served:", served)         # prints "Served: Alice"

# 4) peek next (optional)
if canteen_queue:
    print("Next to be served:", canteen_queue[0])  # shows Bob

# 5) enqueue more arrivals or continue serving:
canteen_queue.append("David")
# then continue popleft() when serving
