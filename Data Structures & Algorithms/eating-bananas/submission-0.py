class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        print(l,r)
        mid = l+(r-l)//2

        while(l<r):
            total = sum(((pile-1)//mid)+1 for pile in piles)
            if total > h:
                l = mid+1
            else:
                r = mid

            mid = l+(r-l)//2
        return l
                