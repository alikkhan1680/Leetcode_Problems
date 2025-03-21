
# Reverse Linked List 206 easy
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  # Keyingi tugunga ishora

class LinkedList:
    def __init__(self):
        self.head = None  # Boshlang‘ichda bosh tugun yo‘q

    def append(self, value):  # Tugun qo‘shish metodi
        new_node = Node(value)  # Yangi tugun yaratamiz
        if not self.head:  # Agar ro‘yxat bo‘sh bo‘lsa
            self.head = new_node
            return
        current = self.head
        while current.next:  # Oxirgi tugunni topamiz
            current = current.next
        current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.value, end=" ->")
            current = current.next
        print("none")


ll = LinkedList()
ll.append(10)
ll.append(20)
ll.display()