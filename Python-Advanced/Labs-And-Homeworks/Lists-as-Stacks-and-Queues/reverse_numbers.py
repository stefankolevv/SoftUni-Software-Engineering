# Importing deque
from collections import deque

nums = deque(input().split())

for _ in range(len(nums)):
    print(nums.pop(), end=' ') # Using end to be printed on the same line
