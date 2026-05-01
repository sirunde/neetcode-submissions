class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0]*n
        stack = deque([0])

        for i in range(1,n):
            while(stack):
                temp = stack.popleft()
                if temperatures[temp] >= temperatures[i]:
                    stack.appendleft(temp)
                    
                    break
                else:
                    result[temp] = i-temp               
            stack.appendleft(i)

                
        return result



