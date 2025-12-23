class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    def reverse(self):
        """Реверсування однозв'язного списку, змінюючи посилання між вузлами"""
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def merge_sort(self):
        """Сортування однозв'язного списку методом злиття"""
        if self.head is None:
            return
        self.head = self._merge_sort_recursive(self.head)

    def _merge_sort_recursive(self, head):
       
        if head is None or head.next is None:
            return head
        
        middle = self._get_middle(head)
        next_to_middle = middle.next
        middle.next = None
        
        left = self._merge_sort_recursive(head)
        right = self._merge_sort_recursive(next_to_middle)
        
        return self._merge_sorted_lists(left, right)

    def _get_middle(self, head):
        """Знаходження середнього вузла списку"""
        if head is None:
            return head
        
        slow = head
        fast = head
        
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def _merge_sorted_lists(self, left, right):
        """Злиття двох відсортованих списків"""
        if left is None:
            return right
        if right is None:
            return left
        
        if left.data <= right.data:
            result = left
            result.next = self._merge_sorted_lists(left.next, right)
        else:
            result = right
            result.next = self._merge_sorted_lists(left, right.next)
        
        return result

    @staticmethod
    def merge_two_sorted_lists(list1, list2):
        """Об'єднання двох відсортованих списків в один відсортований список"""
        dummy = Node()
        current = dummy
        
        head1 = list1.head
        head2 = list2.head
        
        while head1 and head2:
            if head1.data <= head2.data:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
            current = current.next
        
        # Додаємо залишок з одного зі списків
        if head1:
            current.next = head1
        if head2:
            current.next = head2
        
        # Створюємо новий список з об'єднаними даними
        merged_list = LinkedList()
        merged_list.head = dummy.next
        return merged_list


llist = LinkedList()

# Вставляємо вузли в початок
llist.insert_at_beginning(5)
llist.insert_at_beginning(10)
llist.insert_at_beginning(15)

# Вставляємо вузли в кінець
llist.insert_at_end(20)
llist.insert_at_end(25)

# Друк зв'язного списку
print("Зв'язний список:")
llist.print_list()

# Видаляємо вузол
llist.delete_node(10)

print("\nЗв'язний список після видалення вузла з даними 10:")
llist.print_list()

# Пошук елемента у зв'язному списку
print("\nШукаємо елемент 15:")
element = llist.search_element(15)
if element:
    print(element.data)

print("\n" + "="*50)
print("ДЕМОНСТРАЦІЯ НОВИХ ФУНКЦІЙ")
print("="*50)

# 1. Реверсування списку
print("\n1. Реверсування списку")
print("-" * 30)
llist_reverse = LinkedList()
llist_reverse.insert_at_end(1)
llist_reverse.insert_at_end(2)
llist_reverse.insert_at_end(3)
llist_reverse.insert_at_end(4)
llist_reverse.insert_at_end(5)

print("Оригінальний список:")
llist_reverse.print_list()

llist_reverse.reverse()
print("\nРеверсований список:")
llist_reverse.print_list()

# 2. Сортування списку
print("\n2. Сортування списку методом злиття")
print("-" * 30)
llist_sort = LinkedList()
llist_sort.insert_at_end(38)
llist_sort.insert_at_end(27)
llist_sort.insert_at_end(43)
llist_sort.insert_at_end(3)
llist_sort.insert_at_end(9)
llist_sort.insert_at_end(82)
llist_sort.insert_at_end(10)

print("Невідсортований список:")
llist_sort.print_list()

llist_sort.merge_sort()
print("\nВідсортований список:")
llist_sort.print_list()

# 3. Об'єднання двох відсортованих списків
print("\n3. Об'єднання двох відсортованих списків")
print("-" * 30)

list1 = LinkedList()
list1.insert_at_end(1)
list1.insert_at_end(3)
list1.insert_at_end(5)
list1.insert_at_end(7)

list2 = LinkedList()
list2.insert_at_end(2)
list2.insert_at_end(4)
list2.insert_at_end(6)
list2.insert_at_end(8)

print("Перший відсортований список:")
list1.print_list()

print("\nДругий відсортований список:")
list2.print_list()

merged_list = LinkedList.merge_two_sorted_lists(list1, list2)
print("\nОб'єднаний відсортований список:")
merged_list.print_list()