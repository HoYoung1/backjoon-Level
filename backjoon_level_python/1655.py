import sys
import heapq

if __name__ == '__main__':
    maxheap = []
    minheap = []
    
    N = int(sys.stdin.readline())
    for _ in range(N):
        x = int(sys.stdin.readline())
        if len(maxheap) == len(minheap):
            heapq.heappush(maxheap, -x)
        else:
            heapq.heappush(minheap, x)
        if minheap and -maxheap[0] > minheap[0]:
            # swap
            a = heapq.heappop(minheap)
            b = -heapq.heappop(maxheap)
            heapq.heappush(maxheap, -a)
            heapq.heappush(minheap, b)
        print(-maxheap[0])





        
        