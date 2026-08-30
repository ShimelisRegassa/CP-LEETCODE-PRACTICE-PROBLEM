class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
class MyLinkedList:
    def __init__(self):
        self.head=None
        self.size=0
        self.dummy=ListNode(0,self.head)
    def get(self, index: int) -> int:
        if(index<0 or index>=self.size):
            return -1
        temp=self.dummy
        for i in range(index):
            temp=temp.next
        return temp.next.val
    def addAtHead(self, val: int) -> None:
        temp=ListNode(val)
        temp.next=self.dummy.next
        self.dummy.next=temp
        self.size+=1 
    def addAtTail(self, val: int) -> None:
        temp=self.dummy
        newnode=ListNode(val)
        while(temp.next is not None):
            temp=temp.next
        temp.next=newnode
        self.size+=1
    def addAtIndex(self, index: int, val: int) -> None:
        if(index<0 or index>self.size):
            return 
        temp=self.dummy
        newnode=ListNode(val)
        for i in range(index):
            temp=temp.next
        value=temp.next
        temp.next=newnode
        newnode.next=value
        self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        temp=self.dummy
        if(index<0 or index>=self.size):
            return 
        for i in range(index):
            temp=temp.next
        temp.next=temp.next.next
        self.size-=1
       
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)