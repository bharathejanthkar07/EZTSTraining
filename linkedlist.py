class Node:
    def __init__(self,data):
        self.value=data
        self.next=None
Head=Tail=Node(10)
Tail.next=Node(20)
Tail=Tail.next
Tail.next=Node(30)
Tail=Tail.next
Tail.next=Node(40)
Tail=Tail.next
def display(Head):
    if Head.value==None:
        print('Linked List is empty')
    else:
        curr=Head
        while curr!=None:
            print(curr.value,end=' ')
            curr=curr.next
        print()
display(Head)
def Add_front(Head,data):
    temp=Node(data)
    temp.next=Head
    Head=temp
    return Head
Head=Add_front(Head,20)
display(Head)
def Add_End(Tail,data):
    temp=Node(data)
    Tail.next=temp
    Tail=temp
Add_End(Tail,60)
display(Head)
def Specified_Position(Head,pos,data):
    if Head.value==None:
        print('Linked List is empty')
    else:
        cur=Head
        temp=Node(data)
        while cur!=None:
            if pos==cur.value:
                temp.next=cur.next
                cur.next=temp
                break
            else:
                cur=cur.next
Specified_Position(Head,20,22)
display(Head)
