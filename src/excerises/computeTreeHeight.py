import sys
import threading
def compute_height(n, parents):
   heights = [0] * n

   def get_height(i):
        if parents[i] == -1:
            return 1
        if heights[i] != 0:
            return heights[i]
        heights[i] = 1 + get_height(parents[i])
        return heights[i]

   return max(get_height(i) for i in range(n))
def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

