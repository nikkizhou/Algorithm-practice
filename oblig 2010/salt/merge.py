#https://leetcode.com/problems/merge-two-sorted-lists/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
      i,j=list1,list2
      head =ListNode()
      tail= head
      while i is not None and j is not None:
          if i.val <= j.val:
              tail.next=i
              i=i.next
          else:
              tail.next=j
              j=j.next
          tail=tail.next
              
      while i is not None:
          tail.next=i
          i=i.next
          tail=tail.next
      while j is not None:
          tail.next=j
          j=j.next
          tail=tail.next
      
      return head.next
      
              

#better solution found online:
""" 
while True:
  if i is None:
      tail.next = j
      break
  if j is None:
      tail.next = i
      break
  if i.data <= j.data:
      tail.next = i
      i = i.next
  else:
      tail.next = j
      j = j.next
  tail = tail.next
return head.next
"""
