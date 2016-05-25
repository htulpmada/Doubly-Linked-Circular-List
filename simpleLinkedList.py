#################
#adam pluth
#apluth@crimson.ua.edu
#project4
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
  
  def __str__(self):
    return str(self.data)

class llist(object):
  def __init__(self,n=1,f=1,b=1,head=None,tail=None,foward=True,last=None):
    self.head=head
    self.tail=tail
    self.foward=foward
    self.n=n
    self.f=f
    self.b=b


  def insert(self,dat):
    newNode=node(dat)
    if self.head==None:
      self.head=self.tail=newNode
    else:  
      newNode.prev=self.tail
      newNode.nex=self.head
      self.tail.nex=newNode
      self.tail=newNode
      self.head.prev=self.tail

  def r(self):
    self.last=self.head.data
    if self.head.prev==self.head==self.head.nex:
      self.head=None
      self.tail=None
      return
    self.last=self.head.data
    if self.head!=None:
      self.tail.nex=self.head.nex
      self.head.nex.prev=self.tail
      self.head=self.head.nex
      self.tail.nex=self.head
    self.mov(self.foward)    

  def t(self):
    if self.foward:
      self.foward=False
    else:
      self.foward=True

  def m(self):
    if self.foward:
      for i in range(self.f):
        self.head=self.head.nex
    else:
      for i in range(self.b):
        self.head=self.head.prev
    self.tail=self.head.prev
    self.tail.nex=self.head
#    self.print()

  def mov(self,foward):
    if foward:
        self.head=self.head.prev
    self.tail=self.head.prev
    self.tail.nex=self.head
#    self.print()

  def c(self):
    h=self.head.data
    newNode=node(h)
    if self.foward:
      self.insert(h)
    else:
      fow=not self.foward
      self.insert(h)
      self.mov(fow)

  def print(self):
    print('nodes:')
    curr=self.head
    while curr is not None or curr!=self.head or curr!=self.tail.nex :
      print(curr.data)
      if curr==self.head.prev==self.tail:
        break
      curr=curr.nex
    print('"'*20)


def main(args):
  
  lis=llist()

  with open(args[1],'r') as f:
    for line in f:
      l=line.split()
      for i in l:
        if i.isalpha():

      if 'Buy'or'buy' in l:
        lis.insert(l)
      
  
  
  for i in range(0,n+1):
    lis.insert(i)

 
if __name__=='__main__':
  sys.exit(main(sys.argv))
