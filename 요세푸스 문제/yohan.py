n, k = list(map(int, input().split()))


class ListNode:
    def __init__(self, val=0, p=None, n=None):
        self.val = val
        self.prev = p
        self.next = n


if n == 1:
    print('<1>')
elif n == 2:
    head = ListNode(1)
    next_node = ListNode(2)
    head.prev = next_node
    head.next = next_node
    head.next.prev = head
    head.next.next = head

    answer = []
    person_index = k
    curr = head

    for _ in range(k):
        curr = curr.next

    answer.append(str(curr.next.val))
    answer.append(str(curr.val))

    print('<' + ', '.join(answer) + '>')
else:
    head = ListNode(1)
    for i in range(2, n + 1):
        new_node = ListNode(i)
        if i == 2:
            head.next = new_node
            new_node.prev = head
        elif i == n:
            head.prev = new_node
            new_node.next = head
            prev_node.next = new_node
            new_node.prev = prev_node
        else:
            prev_node.next = new_node
            new_node.prev = prev_node
        prev_node = new_node

    answer = []
    person_index = k
    curr = head.prev

    for i in range(n):

        for _ in range(k):
            curr = curr.next

        answer.append(str(curr.val))

        tmp = curr
        curr.prev.next = tmp.next
        curr.next.prev = tmp.prev
        curr = curr.prev

    print('<' + ', '.join(answer) + '>')
