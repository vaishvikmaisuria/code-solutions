def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    
    """
        Return the maximum total number of units that can be put on the truck.

        >>> maximumUnits([[1,3],[2,2],[3,1]], [1,2,3,4,5,6,7,8,9,10], 4)
        8
        >>> maximumUnits([[5,10],[2,5],[4,7],[3,9]], 10)
        91
        
    """
    boxTypes.sort(key=lambda x: -x[1])
    cur_size = 0
    max_units = 0
    for i, v in enumerate(boxTypes):
        max_units += v[1] * min(truckSize - cur_size, v[0])
        cur_size += min(truckSize - cur_size, v[0])

    return max_units


if __name__ == '__main__':
    import doctest
    doctest.testmod()