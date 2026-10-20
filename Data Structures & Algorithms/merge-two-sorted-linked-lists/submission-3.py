# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
                current = current.next
            elif list1.val > list2.val:
                current.next = list2
                list2 = list2.next
                current = current.next
        current.next = list2 if list2 is not None else list1
        return dummy.next

'''
dummy = 0
next = current

for n in list2:
    while list1.val == list2.val:

for each item in the list 2
if the first item in list1 is same as first item in list2, link it
compare item2 list1 and item2 list2
link the smaller one
then link the next one
compare the item3 list2 and item3 list1
link smaller
then link next one
keep going till while is none
return linked list


for x in thing:
    while y is none:
        blahblah

take the first item in the first list
if it's same as the second item next to it, assign currentitem.next = next
if it's same as the third item next to it, etc.
if not, if it's same as first item in list2,
assign currentitem.next = next
if item 2 in list 1 is greater than item 2 in list 

take the first
take the second list
new linked list combines 1 and 2
in numerical order
return the head of the new linked list

new_list = []
for n in list1:
    for i in list2:
        new_list.append(n)
        new_list.append(i)
        sorted(new_list)
    return new_list
'''