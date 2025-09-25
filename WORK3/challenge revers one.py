# 1) create an empty stack
stack = []

# 2) push each character of the string onto the stack
s = "URRWANDA"
for c in s:
    stack.append(c)       # push c onto stack  <-- corresponds to step 2

# 3) prepare an empty result container
reversed_s = ""           # corresponds to step 3

# 4) pop until empty, collecting characters
while stack:              # while stack is not empty
    ch = stack.pop()      # pop top character     <-- corresponds to step 4
    reversed_s += ch      # append to result

# 5) reversed_s now holds the reversed string
print(reversed_s)         # prints "ADNARRU"
