class Solution(object):
    def distanceBetweenBusStops(self, distance, start, destination):
        """
        :type distance: List[int]
        :type start: int
        :type destination: int
        :rtype: int
        """
        if destination > start:
            return min(sum(distance[start:destination]), sum(distance[:start] + distance[destination:]))
        else:
            return min(sum(distance[destination: start]), sum(distance[:destination] + distance[start:]))
