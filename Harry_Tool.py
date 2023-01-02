def prime_number(a):
    """
    求质数
    """
    b=1
    c=True
    for i in range(a-2):
        b=b+1
        if a%b==0:
            c=False
            break
    return c

def GCD(a,b):
    """
    求最大公约数
    """
    c=0
    if a>b:
        smaller=b+1
    else:
        smaller=a+1
    for i in range(1,smaller):
        if a%i==0 and b%i==0:
            c=i
    return c

def gcd(a,b):
    """
    九章算术辗转相减法求最大公约数
    """
    x=a
    y=b
    z=0
    while x%2==0 and y%2==0:
        x=x/2
        y=y/2
        z+1
    while y!=x:
            if x>y:
                x=x-y
            else:
                y=y-x
    if z>1:
        x=x+2*z
    return x

def Fibonacci_sequence(a):
    '''
    斐波那契数列第n位
    '''
    x=1
    y=0
    z=0
    b=[1]
    for i in range(a-1):
        z=x
        b.append(x)
        x=x+y
        y=z
    b.append(x)
    return b

def bubble_sort(a):
    '''
    冒泡排序
    '''
    c=True
    b=0
    while c:
        b=b+1
        c=False
        for i in range(len(a)-b): 
            if a[i]>a[i+1]:
                a[i],a[i+1]=a[i+1],a[i]
                c=True
    return a

class Queue(object):
    def __init__(self):
        self.queue=[]
    def push(self,a):
        self.queue.append(a)
    def pop(self):
        return self.queue.pop(0)
        
def Inversion_of_a_three_digit_number(a):
    '''
    数字反转
    '''
    #return int(str(a)[::-1])
    a=str(a)
    a=a[::-1]
    a=int(a)
    return a

def average(a):
    '''
    平均数
    '''
    x=0
    for i in range(len(a)):
        x=x+a[i]
    return x/len(a)

def fahrenheit_to_celsius(f):
    '''
    华氏度转换摄氏度
    '''

    c=5*(f-32)/9*1000
    c=c//1
    c=c/1000
    return c

def sum_of_one_to_x(x):
    '''
    从1加到x
    '''
    y=0
    for i in range(1,x+1):
        y=y+i
    return y

def chicken_and_rabbits(x,y):
    '''
    鸡兔同笼
    x=头    y=腿
    输出=(鸡,兔)
    '''
    a=y
    b=0
    c=False
    for i in range(x):
        if a/4+b/2==x:
            c=True
            break
        else:
            a=a-2
            b=b+2
    if c==True:
        return b/2,a/4
    else:    
        return "wrong"

def chicken_and_rabbits1(x,y):
    '''
    鸡兔同笼
    x=头    y=腿
    输出=(鸡,兔)
    '''
    a=y
    b=0
    for i in range(x):
        if a/4+b/2==x:
            return b/2,a/4
        else:
            a=a-2
            b=b+2
    return "wrong"
a=[2,3,4,1,5,2,5,6,7,3,6,4]
print(average(a))

def factorical(x):
    if x <= 1:
        return 1
    else: 
        return x*factorical(x-1)
'''递归阶乘'''

def fibo(n):
    if n<= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)
        '''斐波那契数列'''

def fibo2(num):
    x0=0
    x1=1
    if num==1 or num==0:
        return num
    else:
        for i in range(num-2):
            x0,x1=x1,x0+x1
        return x1
        '''递推斐波那契'''

def factorical2(n):
    x=1
    for i in range(2,n+1):
        x*=i
    return x
    '''递推阶乘'''


class Node(object):
    def __init__(self, data, next_node=None):        
        self.data=data
        self.next_node=next_node

    def __str__(self):
        return str(self.data)

class LinkedList(object):
    def __init__(self, head=None):
        self.head=head

    def __len__(self):
        if self.head is None:
            return 0
        self.current=self.head
        self.len=1
        while self.current.next_node is not None:
            self.current=self.current.next_node
            self.len+=1
        return self.len
    def insert_to_front(self, data):
        if data is None:
            return None
        else:
            self.head=Node(data,self.head)
            return self.head
    def append(self, data):
        if data is None:
           return None
        elif self.head is None:
            self.head=Node(data)
            return self.head
        else:
            current=self.head
            while True:
                if current.next_node is None:
                    last=Node(data)
                    current.next_node=last
                    return last
                current=current.next_node
    def find(self, data):
        current=self.head
        while True:
            if current == None:
                return None
            elif current.data == data:
                return current
            else: 
                current=current.next_node
    def delete(self, data):
        if self.head is None:
            return None
        current=self.head
        if data==current.data:
            self.head=self.head.next_node
            return
        while True:
            if current.next_node == None:
                return
            elif current.next_node.data==data:
                break
            else:
                current=current.next_node
        popit=current.next_node
        current.next_node=popit.next_node

    def print_list(self):
        lst=self.get_all_data()
        print(lst)
        
    def get_all_data(self):
        lst=[]
        current=self.head
        while True:
            if current == None:
                break 
            lst.append(current.data)

            current=current.next_node
        return lst


class Node(object):
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.data)


class Bst(object):

    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            return self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            if node.left is None:
                node.left = self._insert(node.left, data)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, data)
        else:
            if node.right is None:
                node.right = self._insert(node.right, data)
                node.right.parent = node
                return node.right
            else:
                return self._insert(node.right, data)



class StackWithCapacity(Stack):

    def __init__(self, top=None, capacity=10):
        super().__init__(top)
        self.capacity=capacity

    def push(self, data):
        if self.is_full():
            raise Exception
        else:
            super().push(data)

    def pop(self):
        return super().pop()

    def is_full(self):
        if self.top is None:
            return False
        curr=self.top
        ind=1
        while True:
            if curr.next is None:
                return ind==self.capacity
            else: 
                ind+=1
                curr=curr.next

    def is_empty(self):
        return self.top is None


class SetOfStacks(object):

    def __init__(self, indiv_stack_capacity):
        self.capacity=indiv_stack_capacity
        self.stack=[]
    def push(self, data):
        try:
            self.stack[-1].push(data)
        except:
            self.stack.append(StackWithCapacity(capacity=self.capacity))
        else:
            return
        self.stack[-1].push(data)
        
    def pop(self):
        if self.stack:
            temp=self.stack[-1].pop()
            while True:
                if temp is None:
                    self.stack.pop()
                    if self.stack:
                        temp=self.stack[-1].pop()
                    else:
                        return
                else:
                    return temp     
        else:
            return
def int2 (str):
    if str.startswith("0b") or str.startswith("0B"):
        a = 0
        l = len(str)
        for i in range(l - 2):
            a = a + int(str[l-i-1],2) * 2**i
        return a
    else:
        return "Wrong"

def int16 (str):
    if str.startswith("0x") or str.startswith("0X"):
        a = 0
        l = len(str)
        for i in range(l - 2):
            a = a + int(str[l-i-1],16) * 16**i
        return a
    else:
        return "Wrong"

def myint(str):
    if str.startswith("0x") or str.startswith("0X"):
        a = 0
        l = len(str)
        for i in range(l - 2):
            a = a + int(str[l-i-1],16) * 16**i
        return a
    elif str.startswith("0b") or str.startswith("0B"):
        a = 0
        l = len(str)
        for i in range(l - 2):
            a = a + int(str[l-i-1],2) * 2**i
        return a
    else:
        return "Wrong"

def bin2 (n):
    a=[]
    while n != 0:
        a.append(n%2)
        n=n//2
    b=[str(x) for x in a]
    b.reverse()
    b="".join(b)
    return "0b"+b

class Harry(object):
    type1="Human"
    def __init__(self,name):
        print("My name is Harry")
        self.__name = name
    def age(self):
        global birthday
        birthday="2006,9,15"
        global myage
        myage=14
        print(self.name)
    def __str__(self):
        return "This is"+self.name+"'s information"
    def hello(self):
        self.__private()
    def __private(self):
        print("this is ",self.name,"'s private meassage")
    @property
    def name (self):
        return self.__name
    @name.setter

    def name(self,name1):
        self.__name=name1


class Node(object):
    
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack(object):

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top is None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.peek() is None

               
def select(l):
    for i in range(1,len(l)):
        mi=i
        for x in range(i-1,len(l)):
            if l[mi]> l[x]:
                mi=x
        if mi!= i-1:
            l[mi],l[i-1]=l[i-1],l[mi]
    return l
def insertsort(l):
    l1=[]
    for i in l:
        if 1>len(l1):
            l1.append(i)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
        else:
            if i<l1[-1]:
                for x in range(len(l1)):
                    if i<l1[x]:
                        l1.insert(x,i)
                        break
            else:
                l1.append(i)
    return l1

def qsort(lit):
    if len(lit)<2:
        return lit
    if len(lit)==2:
        if lit[0]>lit[1]:
            lit[0],lit[1]=lit[1],lit[0]
        return lit
    else:
        index=int(len(lit)/2)
        qsorthelper(lit,index)
        return lit
def qsorthelper(lit,index):
    x=0
    for i in range(index):

        if lit[x]>lit[index]:
            lit.append(lit.pop(i))
            index-=1
            x-=1
        else:
            x+=1
    for i in range(index+1,len(lit)):
        if lit[i]<lit[index]:
            lit.insert(0,lit.pop(i))
            index+=1
            x+=2
        else:
            x+=1
    lit[:index]=qsort(lit[:index])
    lit[index+1:]=qsort(lit[index+1:])
'''
快速排序函数和快速排序辅助函数
'''
class Node(object):
    
    def __init__(self, data, next_node=None):
        self.data=data
        self.next_node=next_node

    def __str__(self):
        return str(self.data)

class LinkedList(object):

    def __init__(self, head=None):
        self.head=Node(head)

    def __len__(self):
        return len(self.get_all_data())

    def insert_to_front(self, data):
        if data==None:
            return None
        else:
            data=Node(data,self.head)
            self.head=data
            return data

    def append(self, data):
        current=self.head
        if data==None:
            return None
        elif current==None:
            self.head=Node(data)
            return self.head
        else:

            while True:
                if current.next_node == None:
                    tempnode=Node(data,None)
                    current.next_node = tempnode
                    return tempnode
                else:
                    current=current.next_node

    def find(self, data):
        current=self.head
        while True:
            if data==current.data:
                return current
            elif current==None:
                break
            else:
                current=current.next_node

    def delete(self, data):
        current=self.head
        while True:
            if current.next_node.data == data:
                current.next_node=current.next_node.next_node
                break
            elif current==None:
                break
            else:
                current=current.next_node

    def print_list(self):
        lst=self.get_all_data()
        for i in lst:
            print(i)

    def get_all_data(self):
        lst=[]
        current=self.head
        while True:
            if current == None:
                return lst
            else:
                lst.append(current.data)
                current=current.next_node
class InsertionSort(object):
    
    def sort(self, data):
        if data is None:
            raise TypeError
        elif data==[]:
            return data
        else:
            temp=[data[0]]
            for i in range(1,len(data)):
                ind=i
                for j in range(len(temp)):
                    if data[i]>temp[j]:
                        pass
                    else:
                        ind=j
                        break
                temp.insert(ind,data[i])
            return temp
x=InsertionSort()
print(x.sort([3,4,5,2,53,5,3,1,5,1]))
def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    dic=dict()
    for i in data:
        dic[i]=dic.setdefault(i,0)
        dic[i]+=1
    temp=i
    for i in dic.keys():
        if dic[i]>dic[temp]:
            temp=i
    return temp

from numpy import array, equal
from bst import Bst


class BstLevelLists(Bst):

    def create_level_lists(self):
        level=0
        buff=[self.root]
        lst=[]
        result=[]
        breaker=False
        while True:
            if buff==[]:
                break
            elif buff[0]==None:
                lst.append(buff.pop(0))
                continue
            else:
                temp=buff.pop(0)
                buff.append(temp.left)
                buff.append(temp.right)
                lst.append(temp)
        while True:
            temp=[]
            for i in range(2**level):
                if lst==[]:
                    breaker=True
                    break
                elif lst[0]== None:
                    lst.pop(0)
                    continue
                temp.append(lst.pop(0))
            if temp!= []:
                result.append(temp)
            level+=1
            if breaker:
                
                break

        return result


class QuickSort(object):
    
    def sort(self, data):
        if data is None:
            raise TypeError
        elif len(data)<2:
            return data
        else:
            temp=data[0]
            lstsmall=[]
            lstbig=[]
            equal=[]
            for i in data:
                if i> temp:
                    lstbig.append(i)
                elif i==temp:
                    equal.append(i)
                else:
                    lstsmall.append(i)
            return self.sort(lstsmall)+equal+self.sort(lstbig)

class MergeSort(object):
    
    def sort(self, data):
        if data is None:
            raise TypeError

        elif len(data)<2:
            return data

        else:
            stdata=self.sort(data[:len(data)//2])
            nddata=self.sort(data[len(data)//2:])
            ret=[]
            while True:
                if nddata==[]:
                    for i in stdata:
                        ret.append(i)
                    return ret
                elif stdata==[]:
                    for i in nddata:ret.append(i)
                    return ret
                elif stdata[0]>nddata[0]:
                    ret.append(nddata.pop(0))
                else:
                    ret.append(stdata.pop(0))


class RadixSort(object):
    
    def sort(self, array, base=10):
        if array is None:
            raise TypeError
        elif array ==[]:
            return array
        maxnum=len(str(max(array)))
        data=array.copy()
        for i in range(maxnum):
            buff=[[],[],[],[],[],[],[],[],[],[]]
            for j in data:
                buff[(j//(10**(i)))%10].append(j)
            data=[]
            for j in buff:
                for k in j:
                    data.append(k)
        return data

class Array(object):
    
    def search_sorted_array(self, array, val):
        if array is None or val is None:
            raise TypeError
        elif not val in array:
            return None
        ind=None
        for i in range(len(array)-1):
            if array[i]>array[i+1]:
                ind=i+1
                break
        if val in array[:ind]:
            temp=array[:ind]
            mini=0
            maxi=len(temp)-1
            while True:
                x=(mini+maxi)-1
                if temp[x]==val:
                    return x
                elif temp[x]>val:
                    maxi=x
                else:
                    mini=x
        else:
            temp=array[ind:]
            mini=0
            maxi=len(temp)-1
            while True:
                x=(mini+maxi)-1
                if temp[x]==val:
                    return x+ind
                elif temp[x]>val:
                    maxi=x
                else:
                    mini=x
class Item(object):
    
    def __init__(self, label, value, weight):
        self.label = label
        self.value = value
        self.weight = weight

    def __repr__(self):
        return self.label + ' v:' + str(self.value) + ' w:' + str(self.weight)

class Knapsack(object):
    

    def fill_knapsack(self, input_items, total_weight):
        if input_items is None or total_weight is None:
            raise TypeError
        elif input_items == 0 or total_weight == 0:
            return 0
        for i in range(len(input_items)):
            input_items[i]=[input_items[i].value/input_items[i].weight,input_items[i]]
        c=True
        b=0
        while c:
            b=b+1
            c=False
            for i in range(len(input_items)-b):  
                if input_items[i][0]>input_items[i+1][0]: 
                    input_items[i],input_items[i+1]=input_items[i+1],input_items[i]
                    c=True
        ret=[]
        for i in range(len(input_items)):
            tempit=input_items.pop()
            if tempit[1].weight<=total_weight:
                ret.append(tempit[1])
                total_weight-=tempit[1].weight
        return ret
def clear_bits_msb_to_index(number, index):
    if index<0:
        raise IndexError
    return number & 2**(index+1)
