from random import randint
from os import system

class Engine(object):
  def __init__(self,nums):
    self.list = nums
   
  def Organize(self):
    New_Order,Numberlist = [],self.list
    
    Largest  = max(Numberlist)
    Smallest = min(Numberlist)

    P_Largest  = Numberlist.index(Largest)
    del Numberlist[P_Largest]

    P_Smallest = Numberlist.index(Smallest)
    del Numberlist[P_Smallest]

    x = int(Numberlist[0])
    y = int(Numberlist[1])
    
    if x <= y: 
     New_Order.append(int(x))
     New_Order.append(int(y))
    else: 
     New_Order.append(int(y))
     New_Order.append(int(x))
    
    New_Order.insert(0,int(Smallest))
    New_Order.insert(3,int(Largest))
  
    return New_Order

  def BruteForce(self):
    global Processes;Processes=[]
    for A,num1 in enumerate(self.list):
     for B,num2 in enumerate(self.list):
      for C,num3 in enumerate(self.list):
       for D,num4 in enumerate(self.list):
        if A!=B and A!=C and A!=D and B!=C and B!=D and C!=D and r!=24: 
         for i in range(96):
           try:
            Result = Connect(num1,Connect(num2,Connect(num3,num4)))
            if Result == 24:
             display = []
             for i,k in enumerate(Processes): 
              if k not in display: 
               display.append(k) 
             print ('\n\n{}'.format(''.join(display)));return
           except:pass 
           del Processes[:]

def Algorithm():
        global Processes,r;r=0
        for x,left in enumerate(List):
	 for y,right in enumerate(List):
	  
	  q = []
	  if x != y:
	   q.append(left)
	   q.append(right)

	   alpha=(max(q))
	   beta=(min(q))
	   
	   Subsets = Sets(alpha,beta)
           Alpha,Beta,Gamma,Delta = List[0],List[1],List[2],List[3]

	   for i,k in enumerate(Subsets):
	    Process = []
	    if k in Factors:
	     Process.append(Steps(alpha,beta,i)) 
	     num1_pos = List.index(alpha)
	     num2_pos = List.index(beta)
	  
	     alpha,beta,gamma,delta = False,False,False,False 
	     Alpha_Used,Beta_Used,Gamma_Used,Delta_Used = False,False,False,False

	     if num1_pos == 0: alpha = True
	     elif num1_pos == 1: beta = True
	     elif num1_pos == 2: gamma = True
	     elif num1_pos == 3: delta = True
	     
	     if num2_pos == 0: alpha = True
	     elif num2_pos == 1: beta = True
	     elif num2_pos == 2: gamma = True
	     elif num2_pos == 3: delta = True

	     if alpha and beta: 
	      Subsets = Sets(Delta,Gamma)
	      for l,m in enumerate(Subsets):
	       if m in Factors:
		if not Delta_Used and not Gamma_Used:
		 Process.append(Steps(Delta,Gamma,l))
		 Subsets = Sets(k,m)
		 for n,r in enumerate(Subsets):
		  if r == 24: 
		   Process.append(Steps(m,k,n) if m >= k else Steps(k,m,n))
		   print '\n\n';print ''.join(Process);return
		 Delta_Used,Gamma_Used = True,True 

	     if alpha and gamma:
	      Subsets = Sets(Delta,Beta)
	      for l,m in enumerate(Subsets):
	       if m in Factors:
		if not Delta_Used and not Beta_Used:
		 Process.append(Steps(Delta,Beta,l))
		 Subsets = Sets(k,m)
		 for n,r in enumerate(Subsets):
		  if r == 24: 
		   Process.append(Steps(m,k,n) if m >= k else Steps(k,m,n))
		   print '\n\n';print ''.join(Process);return
		 Delta_Used,Beta_Used = True,True

	     if alpha and delta:
	      Subsets = Sets(Gamma,Beta)
	      for l,m in enumerate(Subsets):
	       if m in Factors:
		if not Gamma_Used and not Beta_Used:
		 Process.append(Steps(Gamma,Beta,l))
		 Subsets = Sets(k,m)
		 for n,r in enumerate(Subsets):
		  if r == 24: 
		   Process.append(Steps(m,k,n) if m >= k else Steps(k,m,n))
		   print '\n\n';print ''.join(Process);return
		 Gamma_Used,Beta_Used = True,True

	     if beta  and gamma:
	      Subsets = Sets(Delta,Alpha)
	      for l,m in enumerate(Subsets):
	       if m in Factors:
		if not Delta_Used and not Alpha_Used:
		 Process.append(Steps(Delta,Alpha,l))
		 Subsets = Sets(k,m)
		 for n,r in enumerate(Subsets):
		  if r == 24: 
		   Process.append(Steps(m,k,n) if m >= k else Steps(k,m,n))
		   print '\n\n';print ''.join(Process);return
		 Delta_Used,Alpha_Used = True,True

	     if beta  and delta:
	      Subsets = Sets(Gamma,Alpha)
	      for l,m in enumerate(Subsets):
	       if m in Factors:
		if not Gamma_Used and not Alpha_Used:
		 Process.append(Steps(Gamma,Alpha,l))
		 Subsets = Sets(k,m)
		 for n,r in enumerate(Subsets):
		  if r == 24: 
		   Process.append(Steps(m,k,n) if m >= k else Steps(k,m,n))
		   print '\n\n';print ''.join(Process);return
		 Gamma_Used,Alpha_Used = True,True

	     if gamma and delta:
	      Subsets = Sets(Beta,Alpha)
	      for l,m in enumerate(Subsets):
	       if m in Factors:
		if not Beta_Used and not Alpha_Used:
		 Process.append(Steps(Beta,Alpha,l))
		 Subsets = Sets(k,m)
		 for n,r in enumerate(Subsets):
		  if r == 24: 
		   Process.append(Steps(m,k,n) if m >= k else Steps(k,m,n))
		   print '\n\n';print ''.join(Process);return
		 Beta_Used,Alpha_Used = True,True
	     alpha=(max(q))
	     beta=(min(q))
        

          
def Connect(x,y):
   global Processes

   a,b=max([x,y]),min([x,y])
   i = randint(0,3)

   ops = {0:'({} + {}) = {} '.format(a,b,Add(a,b)),
          1:'({} - {}) = {} '.format(a,b,Subtract(a,b)),
          2:'({} / {}) = {} '.format(a,b,Divide(a,b)),
          3:'({} x {}) = {} '.format(a,b,Multiply(a,b))}
   Ops = [Add(a,b),Subtract(a,b),Divide(a,b),Multiply(a,b)]

   Processes.append(ops[i])
   return Ops[i]
            
def Isprime(n):
  if n % 2 == 0:
   return False
  if n % 3 == 0:
   return False

  i,w = 5,2
 
  while i * i <= n:
   if n % i == 0:
    return False
   i += w
   w = 6 - w
  return True	   
  
def Steps(a,b,i):
  Steps = {0:'({} + {}) = {}  '.format(a,b,Add(a,b)),
            1:'({} - {}) = {} '.format(a,b,Subtract(a,b)),
            2:'({} / {}) = {} '.format(a,b,Divide(a,b)),
            3:'({} x {}) = {} '.format(a,b,Multiply(a,b))}

  return Steps[i]

def Sets(a,b):
   return [Add(a,b),Subtract(a,b),Divide(a,b),Multiply(a,b)]	 

def ReadNumbers():
  Newlist,q = [],[] 
  
  for i,item in enumerate(Numbers):
    if not item.isdigit():
     Newlist.append(int(''.join(q)));q=[]
    else:
     q.append(item)
    
  Newlist.append(int(''.join(q)))
  return Newlist

def Divide(x,y):
 a,b=max([x,y]),min([x,y])
 if a == b: return 1
 if b == 1: return a
 if not Isprime(a):
  return a/b

if __name__ == '__main__':
  Add = lambda x,y: x+y
  Multiply = lambda x,y: x*y
  Subtract = lambda x,y: x-y if x >= y else y-x
  try:
   while 1:
    try:
     system('clear')
    except:
     system('cls')
    finally:
     Numbers = raw_input('Enter Four Comma Seperated Numbers: ')
     Factors = [1, 2, 3, 4, 6, 8, 12]
     List = Engine(ReadNumbers()).Organize()
     Algorithm()
     Engine(ReadNumbers()).BruteForce()
     Continue = raw_input('\n\nPress Enter To Continue')
  except KeyboardInterrupt: exit('\n\n')
