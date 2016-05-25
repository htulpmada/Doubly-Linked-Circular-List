#################
#adam pluth
#apluth@crimson.ua.edu
#project3
#linked lists
#2/18/15
#cs260
###################

import sys

class node(object):
  def __init__(self, data, prev=None, nex=None):
    self.data=data
    self.prev=prev
    self.nex=nex
    self.i=data
  def __str__(self):
    return str(self.data)

class llist(object):
  def __init__(self,f,n,b,head=None,tail=None,foward=True,last=None):
    self.head=head
    self.tail=tail
    self.foward=foward
    self.curr=self.head
    self.f=f
    self.n=n
    self.b=b
    self.len=0


  def insert(self,dat):
    newNode=node(dat)
    print('inserting node:',dat)
    print('index:',newNode.i)
    self.len+=1
    if self.head==None:
      self.head=self.tail=newNode
      self.curr=self.head
      print(newNode.data)
    else:  
      newNode.prev=self.tail
      newNode.nex=self.head
      self.tail.nex=newNode
      self.tail=newNode
      self.curr=self.head
      self.head.prev=self.tail
    print('curr node:',self.curr.data)
    print('nex:',self.curr.nex)
    print('prev:',self.curr.prev)
    print('len:',self.len)
    print('head:',self.head.data) 
    print('tail:',self.tail.data) 

  def r(self):
    currnex=self.curr.nex
    currprev=self.curr.prev
    print('deleting curr node:',self.curr.data)
    self.last=self.curr.data
    if self.curr!=None:
      self.curr.prev.nex,self.curr.nex.prev=self.curr.nex,self.curr.prev
      self.tail.nex=self.head

    if self.curr==self.head:
      self.head=self.head.nex
      self.tail.nex=self.head
    
    if self.foward:
      self.curr=self.curr.prev
      self.tail.nex=self.head
    else:
      self.curr=self.curr.nex
      self.tail.nex=self.head
    self.len-=1
    if self.curr.prev==self.curr==self.curr.nex:
      self.head=None
      self.tail=None
    print('curr node:',self.curr.data)
    print('nex:',self.curr.nex)
    print('prev:',self.curr.prev)
    print('head:',self.head.data) 
    print('len:',self.len)
    print('tail:',self.tail.data) 
   


  def t(self):
    print('curr node tog:',self.curr.data)
    if self.foward:
      self.foward=False
      print('going backwards')
    else:
      self.foward=True
      print('going fowards')

  def m(self):
    if self.foward:
      print('moving foward:', f,'nodes')
      for i in range(self.f):
        self.curr=self.curr.nex
    else:
      print('moving backward:', b,'nodes')
      for i in range(self.b):
        self.curr=self.curr.prev
#the error is right here
    self.head=self.curr
    self.tail=self.head.prev
    self.tail.nex=self.head
# something here ^^^^^^
    print('curr node:',self.curr.data)
    print('nex:',self.curr.nex)
    print('prev:',self.curr.prev)
    print('head:',self.head.data) 
    print('len:',self.len)
    print('tail:',self.tail.data) 


  def i(self):
    print('inc node:',self.curr.data)
    if self.curr.data<self.n:
      self.curr.data=(self.curr.data+1)%self.n
    print('curr node:',self.curr.data)
    print('nex:',self.curr.nex)
    print('prev:',self.curr.prev)
    print('head:',self.head.data) 
    print('len:',self.len)
    print('tail:',self.tail.data) 
    
  def d(self):
    print('dec node:',self.curr.data)
    if self.curr.data<self.n:
      self.curr.data=(self.curr.data-1)%self.n
    print('curr node:',self.curr.data)
    print('nex:',self.curr.nex)
    print('prev:',self.curr.prev)
    print('head:',self.head.data) 
    print('len:',self.len)
    print('tail:',self.tail.data) 

  def c(self):
    newNode=node(self.curr.data)
    if self.foward:
      print('copy ',self.curr.data,'behind')
      self.curr.prev.nex=newNode
      newNode.prev=self.curr.prev
      self.curr.prev=newNode
      newNode.nex=self.curr.prev
      self.tail.nex=self.head
    else:
      print('copy ',self.curr.data,'infront')
      self.curr.nex.prev=newNode
      newNode.nex=self.curr.nex
      self.curr.nex=newNode
      newNode.prev=self.curr.nex
      self.tail.nex=self.head
    print('curr node:',self.curr.data)
    print('nex:',self.curr.nex)
    print('prev:',self.curr.prev)
    print('head:',self.head.data) 
    print('tail:',self.tail.data) 
    self.len-=1
    print('len:',self.len)

  def print(self):
    print('nodes:')
    curr=self.head
    for i in range(0,self.len): 
#    while curr is not None or curr!=self.head or curr!=self.tail.nex :
      print(curr.data)
      if curr==self.head.prev==self.tail==self.curr:
        break
      curr=curr.nex
    print('"'*20)


def main(argv):
  global n,f,b,s
  n=int(input())
  f=int(input())
  b=int(input())
  st=str(input())
  s=[]
  
  for o in st:
    s.append(o.lower())
  print(s)
  lis=llist(f,n,b)
  for i in range(0,n+1):
    lis.insert(i)

  print('head:',lis.head)

  while lis.curr!=None or lis.head!=None or lis.tail!=None:
#   lis.print()
#   try: 
    for i in s:
      if i=='t':
        lis.t()
      elif i=='m':
        lis.m()
      elif i=='i':
        lis.i()
      elif i=='d':
        lis.d()
      elif i=='c':
        lis.c()
      elif i=='r':
        lis.r()
#      lis.print()
#    if lis.head==None:
#    if lis.curr.prev==lis.curr==lis.curr.nex:
#      break
#   except(AttributeError):
#      break
#  lis.print()
  print('last item deleted:',lis.last)
  print('curr node:',lis.curr.data)
  print('nex:',lis.curr.nex)
  print('prev:',lis.curr.prev)
  print('head:',lis.head.data) 
  print('len:',lis.len)
  print('tail:',lis.tail.data) 


if __name__=='__main__':
  sys.exit(main(sys.argv))
