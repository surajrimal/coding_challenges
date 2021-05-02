#link https://leetcode.com/problems/distance-between-bus-stops/submissions/

class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        n = len(distance)
        dist = []
        for i in distance:
            dist.append(i)
        print(dist)
        pdis= 0
        ndis = 0
        if(start>destination):
            destination,start = start,destination
        for j in range(start, destination):
            pdis+=distance[j]
            dist.pop(start)
        ndis = sum(dist)
                    
        print(pdis)
        print(pdis)
        if(pdis>ndis):
            return ndis
        return pdis
