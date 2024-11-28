import heapq

nums = [4,1,7,3]
heapq.heapify(nums)
heapq.heappush(nums,2)

print(heapq.heappop(nums))