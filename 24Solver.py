#!/usr/bin/env python
#
# Solves 24 problems
#
# Example1: 1,2,3,4 --> 2+1 = 3+3 = 6*4 = 24
#
# Example2: 2,2,2,4 --> 2+2 = 4+2 = 6*4 = 24
#
#

class Arith(object):
 def __init__(self,a,b):
  self.a = max(a,b)
  self.b = min(a,b)

 def add(self):
  return self.a+self.b

 def sub(self):
  return self.a-self.b

 def mul(self):
  return self.a*self.b

 def div(self):
  return self.a/self.b

 def combs(self):
  arith=[self.add(),self.sub(),self.mul(),self.div()]
  return arith

class Solution(object):
 def __init__(self,lst):
  self.list = lst
  self.mem  = []

 def filter(self,lst):
  # takes zeros from list
  return [n for n in lst if n]

 def solve(self):
  for a,alpha in enumerate(self.list):
   for b,delta in enumerate(self.list): # Stage 1  [3,1,2,2] --> [1,2,3]
    if a==b:continue
    _=[_ for _ in range(4) if all([_!=a,_!=b])]
    gamma=self.list[_[0]]
    theta=self.list[_[1]]

    # method 1
    for num1,comb1 in enumerate(self.filter(Arith(alpha,delta).combs())):
     if num1:del self.mem[:]
     # rearrange the order of alpha & delta - instead of 1-2=1 make it 2-1=1
     alpha1=alpha if alpha>=delta else delta
     delta1=alpha if alpha1==delta else delta

     # get sign of the current action
     sign='+' if not num1 else '-' if num1==1 else 'x' if num1==2 else '/'
     self.mem.append('{}{}{}={}  '.format(alpha1,sign,delta1,comb1))

     # combine the combination of alpha & delta with gamma
     for num2,comb2 in enumerate(self.filter(Arith(comb1,gamma).combs())):
      if num2:
       del self.mem[1:]
      # rearrange the order of comb1 & gamma
      _comb1=comb1 if comb1>=gamma else gamma
      _gamma=comb1 if _comb1==gamma else gamma

      # get sign
      sign='+' if not num2 else '-' if num2==1 else 'x' if num2==2 else '/'
      self.mem.append('{}{}{}={}  '.format(_comb1,sign,_gamma,comb2))

      #combine the combination of comb1 & gamma with theta
      for num3,comb3 in enumerate(self.filter(Arith(comb2,theta).combs())):
       # rearrange the of comb2 & theta
       _comb2=comb2 if comb2>=theta else theta
       _theta=comb2 if _comb2==theta else theta

       # get sign
       sign='+' if not num3 else '-' if num3==1 else 'x' if num3==2 else '/'
       self.mem.append('{}{}{}={}  '.format(_comb2,sign,_theta,comb3))
       if comb3==24:
        if len(self.mem)==3:
         exit('\n{}\n'.format(self.cleanDisplay(self.mem)))
       del self.mem[-1]

    # method 2
    for num,comb in enumerate(self.filter(Arith(alpha,delta).combs())):
     del self.mem[:]
     # rearrange the order of alpha & delta - instead of 1-2=1 make it 2-1=1
     alpha1=alpha if alpha>=delta else delta
     delta1=alpha if alpha1==delta else delta

     # get sign of the current action
     sign='+' if not num else '-' if num==1 else 'x' if num==2 else '/'
     self.mem.append('{}{}{}={}  '.format(alpha1,sign,delta1,comb))

     for num1,comb1 in enumerate(self.filter(Arith(gamma,theta).combs())):
      if num1:del self.mem[1:]
      # rearrange the order of gamma & theta - instead of 1-2=1 make it 2-1=1
      gamma1=gamma if gamma>=theta else theta
      theta1=gamma if gamma1==theta else theta

      # get sign of the current action
      sign='+' if not num1 else '-' if num1==1 else 'x' if num1==2 else '/'
      self.mem.append('{}{}{}={}  '.format(gamma1,sign,theta1,comb1))

      # combine comb & comb1
      for num2,comb2 in enumerate(self.filter(Arith(comb,comb1).combs())):
       # rearrange the order of gamma & theta - instead of 1-2=1 make it 2-1=1
       phi=comb if comb>=comb1 else comb1
       pi=comb if phi==comb1 else comb1

       # get sign of the current action
       sign='+' if not num2 else '-' if num2==1 else 'x' if num2==2 else '/'
       self.mem.append('{}{}{}={}  '.format(phi,sign,pi,comb2))
       if len(self.mem)==3:
        if comb2==24:
         exit('\n{}\n'.format(self.cleanDisplay(self.mem)))
       del self.mem[-1]

 def cleanDisplay(self,lst):
  return ''.join(lst).rstrip()

class Numbers(object):
 def __init__(self,lst):
  self.lst = lst
  self.num = []

 def orginize(self):
  for item in self.lst:
   if item.isdigit():
    self.num.append(item)
   else:
    yield eval(''.join(self.num))
    del self.num[:]
  if self.num:
   yield eval(''.join(self.num))

if __name__ == '__main__':
 lst=list(Numbers(raw_input('Enter 4 number separated by commas: ')).orginize())
 Solution(lst).solve()
