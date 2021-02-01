# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from heapq import heappush, heapify, heappop
class Solution(object):
    def mergeKLists(self, lists):
        answer_head = None
        answer_tail = None
        added = True

        heap = []
        heapify(heap)

        for index, head in enumerate(lists):
            if head != None:
                heappush(heap, (head.val, index))
                lists[index] = head.next

        if len(heap) > 0:
            val, ind = heappop(heap)
            answer_head = ListNode(val)
            answer_tail = answer_head

            if lists[ind] != None:
                heappush(heap, (lists[ind].val, ind))
                lists[ind] = lists[ind].next

        while len(heap) > 0:
            # a =
            # print(a)
            val, ind = heappop(heap)
            answer_tail.next = ListNode(val)
            answer_tail = answer_tail.next

            if lists[ind] != None:
                heappush(heap, (lists[ind].val, ind))
                lists[ind] = lists[ind].next

        return answer_head

        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
