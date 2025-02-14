class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length

def getIntersectionNode(headA, headB):
    lenA, lenB = get_length(headA), get_length(headB)

    # Align the start of both lists
    while lenA > lenB:
        headA = headA.next
        lenA -= 1
    while lenB > lenA:
        headB = headB.next
        lenB -= 1

    # Find intersection
    while headA and headB:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next

    return None  # No intersection

# Example Usage:
# Creating an intersection at node with value 8
common = ListNode(8, ListNode(4, ListNode(5)))

headA = ListNode(4, ListNode(1, common))
headB = ListNode(5, ListNode(0, ListNode(1, common)))

result = getIntersectionNode(headA, headB)
if result:
    print(f"Intersection at node with value {result.val}")
else:
    print("No intersection")
