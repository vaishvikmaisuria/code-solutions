from typing import List
from collections import defaultdict
from itertools import combinations


def mostVisitedPattern(username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
    """
        Returns 3-sequence visited by the largest number of users. Where 3-sequence is a list of websites 
        of length 3 sorted in ascending order by the time of their visits.

            Parameters:
                    username (List[str]): array of users, user with name username[i] 
                    website (List[str]): array of websites, website with name website[i]
                    timestamp (List[int]): array of times, time where username[i] visited website[i]

            Returns:
                    top_seq (List[str]):  3-sequence visited by the largest number of users

        >>> mostVisitedPattern(["joe","joe","joe","james","james","james","james","mary","mary","mary"], [1,2,3,4,5,6,7,8,9,10], ["home","about","career","home","cart","maps","home","home","about","career"])
        ['home', 'about', 'career']
        >>> mostVisitedPattern(["joe","joe","joe"], [1,2,3], ["home","about","career"] )
        ['home', 'about', 'career']
        >>> mostVisitedPattern(["u1","u1","u1","u2","u2","u2"], [1,2,3,4,5,6], ["a","b","c","a","b","a"])
        ['a', 'b', 'a']
        >>> mostVisitedPattern(["u1","u1","u1","u2","u2","u2"], [1,2,3,4,5,6], ["a","b","a","a","b","c"])
        ['a', 'b', 'a']
    """
    # store website and how many users 
    users = defaultdict(list)

    # create list of tuples ---> [('joe', 3, 'career'),....]
    packed_tuple = zip(username, timestamp, website)
    
    # websites in list are in ascending timestamp order
    for user, time, site in sorted(packed_tuple, key = lambda x: (x[1])): 
        users[user].append(site)

    counter_dict= defaultdict(int)

    for website_list in users.values():
        combs = set(combinations(website_list, 3))
        for comb in combs:
            counter_dict[comb] += 1
        
    # sort descending by value, then lexicographically
    sorted_counter_dict = sorted(counter_dict, key=lambda x: (-counter_dict[x], x)) 
    return list(sorted_counter_dict[0])

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
    # timestamp = [1,2,3,4,5,6,7,8,9,10]
    # website = ["home","about","career","home","cart","maps","home","home","about","career"]
    
    # print(mostVisitedPattern(username, timestamp, website))