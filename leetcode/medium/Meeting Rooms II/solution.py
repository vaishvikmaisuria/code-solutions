def shiftUp(heap, pos, index):
    """
        Bubble up the smaller child until hitting a leaf, as long as min heap condition holds

            Parameters:
                    heap (List[List[int]]): array of meeting time intervals where intervals[i] = [starti, endi]
                    pos (int): index of array interval we are trying to shift up
            Returns:
                    heap (int):  heap where the meeting time interval is moved up 
        >>> shiftUp([[7,10],[2,4]], 0, 1)
        [[2, 4], [7, 10]]
    """

    endPos = len(heap)
    initialPos = heap[pos]
    startPos = pos 
    
    # leftmost child position
    childPos = 2 * pos + 1

    while childPos < endPos:

        # right child adjacent to childPos
        rightPos = childPos + 1

        # Set childpos to index of smaller child.
        if rightPos < endPos and heap[childPos][index] > heap[rightPos][index]:
            childPos = rightPos
        
        # Move the smaller child up.
        heap[pos] = heap[childPos]

        pos = childPos
        # leftmost child position
        childPos = 2 * pos + 1
    
    # the pos index of heap has 
    heap[pos] = initialPos

    # print("end heap", heap)
    heap = shiftDown(heap, startPos, pos)
    return heap 

def shiftDown(heap, startPos, pos):
    """
        Follow the path to the root, moving parents interval down until finding a place. 

            Parameters:
                    heap (List[List[int]]): array of meeting time intervals where intervals[i] = [starti, endi]
                    startPos (int): index of array interval initial position
                    pos (int): index of array interval we are trying to shift down
            Returns:
                    heap (int):  heap where the meeting time interval is moved up 

        >>> shiftDown([[7,10],[2,4]], 0, 1)
        [[2, 4], [7, 10]]
    """

    initialPos = heap[pos]
    while pos > startPos:
        parentPos = (pos - 1) // 2
        parentInterval = heap[parentPos]

        if initialPos[1] < parentInterval[1]:
            heap[pos] = parentInterval
            pos = parentPos
            continue
        break
    heap[pos] = initialPos

    return heap


def minMeetingRooms(intervals) -> int:
    """
        Returns the minimum number of conference rooms required.

            Parameters:
                    intervals (List[List[int]]): array of meeting time intervals intervals where intervals[i] = [starti, endi]

            Returns:
                    free_rooms (int):  Interger representing minimum number of conference rooms required.

        >>> minMeetingRooms([[0,30],[5,10],[15,20]])
        2
        >>> minMeetingRooms([[7,10],[2,4]])
        1
        >>> minMeetingRooms([[7,10], [10,11], [2,4]])
        1
        >>> minMeetingRooms([[0,30],[5,10],[15,25], [0, 20], [20, 25] ])
        3
        >>> minMeetingRooms([[5,8],[6,8]])
        2
        >>> minMeetingRooms([[5,8]])
        1
    """

    intervalLen = len(intervals)
    # If there is no meeting to schedule then no room needs to be allocated.
    if not intervals:
        return 0

    if intervalLen == 1:
        return 1

    # The heap initialization
    rooms = []
    for i in range ( (intervalLen -1), -1, -1):
        heap = shiftUp(intervals.copy(), i, 1)

    # use merge sort instead  
    intervals.sort(key= lambda x: x[0])

    # add the first meeting 
    rooms.append(heap.pop(0))
    
    for j in intervals[1:]:
        # If the earliest room is free, assign that room to this meeting.
        if rooms[0][1] <= j[0]:
            rooms.pop(0)

        # add the new room to the list of in-use room list
        rooms.append(j)

    return len(rooms)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    