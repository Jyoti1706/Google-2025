class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.begin = None

    def isEmpty(self):
        if self.begin is None:
            return True
        return False

    def length(self):
        temp = self.begin
        count = 0
        while temp.next:
            count += 1
            temp = temp.next
        return count

    def search(self, element):
        temp = self.begin
        while temp.next:
            if temp.key == element:
                return True
            temp = temp.next
        return False

    def insertAtBeginning(self, node):
        if self.isEmpty():
            self.begin = node
        else:
            self.begin.prev = node
            node.next = self.begin
            self.begin = node

    def insertAtLast(self, node):
        temp = self.begin
        if self.isEmpty():
            self.begin = node
            return
        while temp.next:
            temp = temp.next
        temp.next = node
        node.prev = temp

    def deleteAtBeginning(self):
        if self.isEmpty():
            return None
        elif self.begin.next is None:
            self.begin = None
        else:
            self.begin = self.begin.next
            self.begin.prev = None

    def deleteFromLast(self):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.begin.next is None:
            temp = self.begin.next
            self.begin = None
            return temp
        else:
            temp = self.begin
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
            temp.prev = None
            return temp

    def delete(self, value):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.begin.next is None and self.begin.data == value:
            self.begin = None
        else:
            temp = self.begin
            while temp:
                if temp.key == value:
                    break
                temp = temp.next
            if temp is None:
                print("Element not present in linked list. Cannot delete element.")
            elif temp.next is None:
                self.deleteFromLast()
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                temp.next = None
                temp.prev = None
