class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # it is unclear times is sorted by the ui.
        # to easily work, lets sort times first.
        matrix = [[float("inf")]*n for _ in range(n)]
        output = [float("inf")]*n

        for (start,end,time) in times:
            matrix[start-1][end-1] = time
        output[k-1]= 0

        queue = deque([(k-1,0)])
        while(queue):
            node,time = queue.pop()
            for i in range(n):
                if time+matrix[node][i] < output[i]:
                    output[i] = matrix[node][i]+time
                    queue.append((i,time+matrix[node][i]))

        output = max(output)
        return output if output < float("inf") else -1

