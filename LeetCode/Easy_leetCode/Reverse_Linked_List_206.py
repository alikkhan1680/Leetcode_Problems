


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    prev = None  # Oldingi tugunni saqlash uchun
    current = head  # Hozirgi tugun

    while current:
        next_node = current.next  # Keyingi tugunni saqlab qolamiz
        current.next = prev  # Hozirgi tugunni oldingi tugunga bog‘laymiz
        prev = current  # Oldingi tugunni yangilaymiz
        current = next_node  # Keyingi tugunga o‘tamiz

    return prev  # Yangi bosh tugunni qaytaramiz


# ListNode obyektlari orqali bog‘langan ro‘yxat yasash
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

# To‘g‘ri chaqirish
reversed_head = reverseList(node1)

# Natijani chiqarish
while reversed_head:
    print(reversed_head.val, end=" -> ")
    reversed_head = reversed_head.next
















# Reverse Linked List 206 easy
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None  # Keyingi tugunga ishora
#
# class LinkedList:
#     def __init__(self):
#         self.head = None  # Boshlang‘ichda bosh tugun yo‘q
#
#     def append(self, value):  # Tugun qo‘shish metodi
#         new_node = Node(value)  # Yangi tugun yaratamiz
#         if not self.head:  # Agar ro‘yxat bo‘sh bo‘lsa
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:  # Oxirgi tugunni topamiz
#             current = current.next
#         current.next = new_node
#
#     def display(self):
#         current = self.head
#         while current:
#             print(current.value, end=" ->")
#             current = current.next
#         print("none")
#
#
# ll = LinkedList()
# ll.append(10)
# ll.append(20)
# ll.display()