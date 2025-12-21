#вузол
class Node:
    def __init__(self, value):
        self.value = value  #число
        self.next = None    #за яку тримається далі

#список
class LinkedList:
    def __init__(self):
        self.head = None  

    #додати число в кінець 
    def add(self, value):
        new_node = Node(value)
        if self.head is None:   #якщо список пустий
            self.head = new_node
            return
        
        current = self.head
        while current.next:     #йдемо до останнього
            current = current.next
        current.next = new_node #чіпляємо нову

    #виводимо список
    def show(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    #розворот
    def reverse(self):
        prev = None             #попередньої спочатку немає
        current = self.head     #починаємо з першої
        
        while current:
            next_node = current.next #запам'ятали наступну
            current.next = prev      #розвернули 
            
            prev = current           #перемістилися на крок
            current = next_node
            
        self.head = prev        #останній став першим

    #сортування
    def sort(self):
        sorted_head = None       #створ відсортований список
        current = self.head      #перебр зі старог списку

        while current:
            next_node = current.next #замітка
            
            #якщо список пустий або число менше за перше
            if sorted_head is None or sorted_head.value >= current.value:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.value < current.value:
                    temp = temp.next
                
                #вставака
                current.next = temp.next
                temp.next = current
            
            current = next_node #некст
        
        self.head = sorted_head #

#злиття 
def merge_lists(list1, list2):
    dummy = Node(0)      
    tail = dummy          #кінець списку

    l1 = list1.head
    l2 = list2.head

    while l1 and l2:     
        if l1.value < l2.value:
            tail.next = l1     
            l1 = l1.next
        else:
            tail.next = l2      
            l2 = l2.next
        tail = tail.next     

    #те що лишилось в одне
    if l1:
        tail.next = l1
    elif l2:
        tail.next = l2

    #результат після порожнього
    result = LinkedList()
    result.head = dummy.next
    return result

#вивід

print("створення списку:")
my_list = LinkedList()
my_list.add(3)
my_list.add(1)
my_list.add(4)
my_list.add(2)
my_list.show()  

print("\n--робимо reverse")
my_list.reverse()
my_list.show()  

print("\n--зʼєднання")
my_list.sort()
my_list.show()  

print("\n--перетворення двох списків в один")
list_A = LinkedList() 
list_A.add(10)
list_A.add(30)

list_B = LinkedList() 
list_B.add(20)
list_B.add(40)

#зʼєднання
final_list = merge_lists(list_A, list_B)
final_list.show() 
