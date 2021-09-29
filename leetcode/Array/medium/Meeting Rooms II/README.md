# Problem Statement

Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.

# Example 1:

Input: intervals = [[0,30],[5,10],[15,20]]
Output: 2

# Example 2:

Input: intervals = [[7,10],[2,4]]
Output: 1

# Notes:

1. 1 <= intervals.length <= 104
2. 0 <= starti < endi <= 106

# Link: 

https://leetcode.com/problems/meeting-rooms-ii/

#  Solution Thought Process

1. Start with the Base case 
   1. If there is no meeting to schedule then no room needs to be allocated.
   2. Check the case when starti is equal to endi 
2. Understand the important parts of the problem
   1. Manage two seperate times starti and endi 
   2. Sort endi so that the next meeting with starti < endi can be scheduled
3. Decide on a data structure that is efficient to solve this question 
   1. Priority queue -> implemented with min heap -> Choosing this one !!!
   2. Array -> prebuilt sort (python {Timsort}) -> (Interviewer will be happy :} )
   

   