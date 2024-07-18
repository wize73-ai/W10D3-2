# W10D3-2

Solving the Merge Two Sorted Lists Problem

 

Objective:

Enhance your problem-solving skills by solving the Merge Two Sorted Lists problem on LeetCode and documenting your solution approach.

 

Problem Statement:

Solve the LeetCode problem: https://leetcode.com/problems/merge-two-sorted-lists/Links to an external site.

 

Steps to Complete the Exercise:

Understand the Problem:
   - Carefully read the problem statement.

   You are given the heads of two sorted linked lists list1 and list2.

    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.


   - Identify the inputs and expected outputs.

        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]

        Input: list1 = [], list2 = []
        Output: []

        Input: list1 = [], list2 = [0]
        Output: [0]

   - Note the constraints and possible edge cases.

        The number of nodes in both lists is in the range [0, 50].
        -100 <= Node.val <= 100
        Both list1 and list2 are sorted in non-decreasing order.

Plan Your Approach:
   - Consider different strategies to solve the problem.

   compare list1 index 0 to list 2 index 0 and add the larger one to the sorted list
   
   handle empty lists by ensuring len > 0 or return other value, returning none if both empty

   - Choose the most efficient algorithm considering time and space complexity.

   - Outline your solution before coding.

Write the Code:
   - Use your preferred coding environment.

    Python3

   - Implement your solution clearly and concisely.

   - Use meaningful variable names and comments to explain your code.

Test Your Solution:
   - Test your code with various test cases, including edge cases.

   - Ensure your solution passes all test cases on LeetCode.

        see screenshots in repo

Document Your Solution:
   - Create a documentation file in PDF or Markdown format.

   - Explain your code design choices.

   - Describe any specific algorithms or data structures used.

   - Detail your approach and reasoning for solving the problem.

Submit Your Solution:
   - Ensure your solution passes the LeetCode submission.

   class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # a new head node for linked list output
        newHead = ListNode()
        current = newHead

        # select lower value of two options and add to new list updating head
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # add orphaned list items when only one list remaining
        current.next = list1 if list1 else list2

        # Return the merged list, starting from newHead(new node for merged list)
        return newHead.next

    def create_linked_list(self, lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for value in lst[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def print_linked_list(self, node):
        values = []
        while node:
            values.append(node.val)
            node = node.next
        print(" -> ".join(map(str, values)) + " -> None")


   - Submit your documentation and LeetCode solution via the designated platform.

   Conclusion

   - This challenge was interesting introduction to linked list manipulation.  It solidified my understanding of the use of linked lists, and exposed where they are less efficient and more efficient.

   - This solution took more than one day, first day got the logic and approach, but I needed to sleep on this problem in order to work out logical order and then syntax.