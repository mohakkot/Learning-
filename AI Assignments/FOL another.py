

import collections
import sys
import copy
sys.setrecursionlimit(10000) 


	
class KB:
	m='10'
	factdict={}
	clause={}
	processed={}
	facts=[]
	implications=[]
	corresponding={}
	for_prefix=[]
	count=0
	objects=[]
	final_objects=[]
	def make_kb(self,rule):
		
		
		ready=self.splitclause(rule)
		self.implications.append(rule)
		self.for_prefix.append(ready)
	#	else:
	#		self.addfacts(rule)
	#		self.facts.append(rule)

		#print "For postfix:",self.for_prefix	
		
		
	def splitclause(self,rule):
		
		#print "Rule is:",rule
		
		new=[]
		new=list(rule)
		#print new
		i=0
		con=[]

		while i!=len(new):
			if new[i] in ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'):
				str=[]	
				while new[i] !=')':
					if new[i]=="":
						i=i+1
					str.append(new[i])
					
					i=i+1
				str.append(new[i])
				string=''.join(str)
				#print "here it is:",string
				
				predicate,var=self.splitword(string)
				#print "Predicate is:",predicate
				#number=self.convert(predicate)
				term1=term(predicate)
				term1.name=predicate
				term1.variables=var
				#print "PRINTING :",term1.name,term1.variables,term1.value
				con.append(term1)
				self.objects.append(term1)
			else: 
				if new[i]=='':
					continue
				term1=term(new[i])
				term1.name=new[i]
				con.append(term1)
			i=i+1
			
		#ready=''.join(con)
		#print "Final:",con
		
		return con

	def convert(self,string):
		
		if string not in self.corresponding.keys():
			self.m=str(int(self.m)+1)
			self.corresponding[string]=self.m
		print(self.corresponding)

		return self.m
					
	
	def addfacts(self,rule):
		predicate,arg=self.splitword(rule)
		
		if predicate in self.factdict.keys():
			
			self.list.append(arg)
			self.factdict[predicate]=self.list
		else:
			self.list=[]
			self.list.append(arg)
			#print self.list
			self.factdict[predicate]=self.list
			
		#print "Fact table is:",self.factdict


	def splitword(self,rule):
		split=[]
		arguments=[]
		split=rule.rsplit("(")
		predicate=split[0]
		#print "splits:",split
		arg=split[1].rsplit(")")
		v=arg[0].rsplit(",")
		for i in range(0,len(v)):
			arguments.append(v[i])
		#print "predicate is:",predicate
		#print "Arguments are:",arguments
		return predicate,arguments

		
class POST:
	
	op = -1
	operand = -2
	lbracket = -3
	rbracket = -4
	empty = -5
	expressions=[]
 	def precedence_operator(self,j):
    		if j is '(':
        		return 0
    		elif j is '~':
        		return 1
    		elif j is '&' or j is'|' or j is'=' or j is '>' or j is '=>':
    	    		return 2
    		else:
        		return 1000
	def find(self,j):
    		if j is '(':
        		return self.lbracket
    		elif j is ')':
        		return self.rbracket
    		elif j is '=>' or j is'implies' or j is '&' or j is '|' or j is '~':
        		return self.op
    		elif j is ' ':
        		return self.empty    
    		else :
        		return self.operand   
                 
	def convert(self,list1):
			
		for element in list1:
			postfix = []
			temp = []
			infix=element
			#print "infix:",infix
			inf=list(infix)
			str=[]
			str1=[]
			i=0
			while i!=len(inf):
				if inf[i].value=='=':
		
					if inf[i+1].value=='>':
						imp='implies'
						n=term(imp)
						str.append(n)
						str1.append(n.value)
					i=i+1
				else:
					str.append(inf[i])
					str1.append(inf[i].value)
				i=i+1
			#print 'hereeee',str
			#for s in str:
				#print s.value
			#print "thereee",str1
			for i in str:
				type = self.find(i.value)
				#print "TYpe is:",type
    				if type is self.lbracket :
        				temp.append(i.value)
    				elif type is self.rbracket :
        				next =temp.pop()
        				while next is not '(':
						for i in str:
							if next==i.value:
            							postfix.append(i)
						
            					next = temp.pop()
    				elif type is self.operand:
        				 postfix.append(i)
					
    				elif type is self.op:
        				#p =self.precedence_operator(i.value)
					#print self.precedence_operator(temp[-1])
        				#while len(temp) is not 0 and p <= self.precedence_operator(temp[-1]) :
	  				 #   for i in str :
					#	if temp.pop()==i.value:
				         #   		postfix.append(i)
					  
        				temp.append(i.value)
    				elif type is self.empty:
        				continue
				print("temp:", temp)

			while len(temp) > 0 :
				for i in str :
					if temp.pop()==i.value:	
						print("yes")
						postfix.append(i)
			print("postfix is:", postfix)
			for k in range(0,len(postfix)):
				print("pstfix:", postfix[k].value)
			i=0
			while i!=len(postfix):
				if postfix[i].value=='implies':
					 postfix[i].value='=>'
				i=i+1
			#print "It's postfix notation is ",''.join(postfix)
			#expr=''.join(postfix)
			self.expressions.append(postfix)

		return self.expressions

class CNF:
	kb=[]
	def pre_cnf(self,rules):
		
		for element in rules:
			split=list(element)
			#print split
			split1=[]
			i=0
			while i!=len(split):
				if split[i] in ('1','2','3','4','5','6','7','8','9'):
					#print split[i]+split[i+1]
					split1.append(split[i]+split[i+1])
					i=i+1
				elif split[i]=='=':
					if split[i+1]=='>':
						split1.append(split[i]+split[i+1])
						i=i+1
					
				else:
					split1.append(split[i])
				i=i+1
			#print "Ready for conversion: ", split1
			root=self.tree(split1)
			
 			
			#print "Dislplaying tree",self.inorder(root)

			self.remove_implications(root)
			#print "Displaying tree:",self.postorder(root)
			self.remove_negations(root)
			#print "Displaying tree:",self.postorder(root)			
			self.distribute(root)
			#print "Displaying tree:",self.postorder(root)	
			#print "final cnf is:",self.final
			
			
			self.kb.append(root)
			self.seperate_clauses(root)

	#self.display(kb)
	def display(self,element):
		if element is not None:
			
			self.display(element.left)
			#if element.value.value in ('&','|'):
				#print element.value,
			#else:
			#	for object in kb.objects:
			#		if element.value==object.value:
			#			print object.name,
			#			print object.variables
						#print element.negation
			#print element.value.value,element.value.variables,element.negation
			
			self.display(element.right)
			
	def seperate_clauses(self,element):
		if element is not None:
			if element.value.value=='&':
				if element in kb.final_objects:
					kb.final_objects.remove(element)
					kb.final_objects.append(element.left)
					kb.final_objects.append(element.right)
				else:
					kb.final_objects.append(element.left)
					kb.final_objects.append(element.right)
				self.seperate_clauses(element.left)
				self.seperate_clauses(element.right)
			 
			else:
				kb.final_objects.append(element)
			
	def postorder(self,root):
   		if root is not None:
			
			#print root.negation
        		self.postorder(root.left)
        		#print root.value.value,root.value.variables,root.negation
       			self.postorder(root.right)
		#return self.final

	def distribute(self,root):
		
		if root is not None :
			if root.value.value=='|':
				if root.left is not None:
					if root.left.value.value=='&':
						root.value.value='&'
						root.left.value.value='|'
						temp=root.left.right
						temp1=root.right
						#print "temp1:",root.right.value
						#print "temp:",temp.value
					
						root.left.right=temp1
						#print "root of left of right",root.left.right.value
						root.right=node("|")
						#print "root of right:",root.right.value
						#print "root of left of right",root.left.right.value
						root.right.right=root.left.right
						#print "root of right of right:",root.right.right.value
						root.right.left=temp
						#print "root of right of left:",root.right.left.value
						
					#self.distribute(root.left)
				
				if root.right is not None:	#self.distribute(root.right)
					if root.right.value.value=='&':
						root.value.value='&'
						temp=root.right.left
						root.right.left=root.left
						root.right.value.value='|'
						root.left=node("|")
						root.left.right=temp
						root.left.left=root.right.left
					#self.distribute(root.left)
				self.distribute(root.left)
				self.distribute(root.right)
			else:
				self.distribute(root.left)
				self.distribute(root.right)

		#print "EXITING"
	def remove_negations(self,root):
		if root is not None:
			if root.negation==True:
				if root.value.value=='|':
					root.value.value='&'
					root.negation=False
					if root.left.negation==False:
						root.left.negation=True
					else:
						root.left.negation=False
					if root.right.negation==False:
						root.right.negation=True
					else:
						root.right.negation==False
					self.remove_negations(root.left)			
					self.remove_negations(root.right)
				elif root.value.value=='&':
					root.value.value='|'
					root.negation=False
					if root.left.negation==False:
						root.left.negation=True
					else:
						root.left.negation=False
					if root.right.negation==False:
						root.right.negation=True
					else:
						root.right.negation==False
					self.remove_negations(root.left)			
					self.remove_negations(root.right)
				
			else:
				self.remove_negations(root.left)
				self.remove_negations(root.right)
		
				
	def remove_implications(self,root):
		if root is not None:
			if root.value.value=='=>':
				root.value.value='|'
				root.left.negation=True
						
				self.remove_implications(root.left)
				self.remove_implications(root.right)
			else:
				self.remove_implications(root.left)
				self.remove_implications(root.right)
		

	def tree(self,exp):
			
			temp=[]
			l=[]
			d=0
			stack=[]
			for element in exp:
				if element.value=='=>' or element.value=='&' or element.value=='|':
					rchild=stack.pop()
					lchild=stack.pop()
					newnode=node(element)
					newnode.left=lchild
					#print "left:",newnode.left.value
					newnode.right=rchild
					stack.append(newnode)
				elif element.value=='~':
					child=stack.pop()
					if child.negation==False:
						child.negation=True
					else:
						child.negation=False
					stack.append(child)
					
				else:
					newnode=node(element)
					stack.append(newnode)
					
			root=stack.pop()
			
			#print "value of root is:",root.value.value
			return root

	
class term:
	def __init__(self,value):
		self.value = value
        	self.negation=False
		self.name=None
		self.variables=[]
		
			
class node:
	def __init__(self,value):
		self.value = value
        	self.left = None
        	self.right = None
		self.negation=False
		self.unique=[]
		self.visited=[]

class Resolution:
	f1=open("output.txt","w")
	def empty_list(self,root):
		l=[]
		list=self.give_list(l,root)
		return list
	def give_list(self,l,root):
		if root is not None:
			if root.value.value !='|':
				l.append(root)
				self.give_list(l,root.left)
				self.give_list(l,root.right)
			else:
				self.give_list(l,root.left)
				self.give_list(l,root.right)
		return l
	def output(self,answer):
		print "Entering"
		self.f1.write(answer+'\n')
	def resolution(self,query_list):
		self.f1=open("output.txt","w")
		for query in query_list:
			self.temp_kb=[]
			#query=query_list[0]
			for i in range(0,len(kb.final_objects)):
				kb.final_objects[i].visited=[]
				kb.final_objects[i].id=[]
			if query.negation==True:
				query.negation=False
			else:
				query.negation=True
			for i in range(0,len(kb.final_objects)):	
				self.temp=copy.deepcopy(kb.final_objects[i])
				self.temp_kb.append(self.temp)
			#self.temp_kb=kb.final_objects
			self.temp_kb.append(query)
			print ("PRINTING TEMP KB:")
			#print "Size:",len(self.temp_kb)
			i=0
			#while i!=len(self.temp_kb):
			#	cnf.display(self.temp_kb[i])	
			#	print ""
			#	i=i+1
			#print "TEMP KB ENDS"	
			k=0
			for i in range(0,len(self.temp_kb)):
                		j=0
                		
                		while(j < len(self.temp_kb)):
                    			if i == j:
                        			j += 1
                        			continue
					if len(self.temp_kb) >200:
						
						#print "False because of size"
						break
					if j not in self.temp_kb[i].visited:
						answer=self.solve(self.temp_kb[i],self.temp_kb[j])
						if answer==True:
							ans='True'
							#print i,j
							self.output(ans)
							break
                   				self.temp_kb[i].visited.append(j)
						self.temp_kb[j].visited.append(i)

 	                   		j=j+1
                		if j!= len(self.temp_kb):
                    			break
                		i = i+1
                	if i==len(self.temp_kb):
				self.output("False")
				
				#print "False"

	
		#for obj in self.temp_kb:
		#	for obj1 in self.temp_kb:
		#		if obj!=obj1:
		#			
		#			answer=self.solve(obj,obj1)
		#			if answer==True:
		#				break
		#answer=self.solve(self.temp_kb[0],self.temp_kb[1])
		#for i in range(0,int(n_rules)):
		#	cnf.display(kb.final_objects[i])	
		#	print ""
		#print "KB ENDS HERE"	
			#print "ANSWER IS:",answer
		self.f1.close()
	def variable(self,x):
		if x.islower():
			return True
		else:
			return False
	def unify(self,l1,l2):
			if l1==[] and l2==[]:
				return False
			#print l1,l2
			#while h==True and i!=len(l1)-1 and j!=len(l2)-1:
			for i in range(0,len(l1)):
				if self.variable(l1[i][0])==True and self.variable(l2[i][0])==False:
					self.dict[l1[i]]=l2[i]
					#print "can unify"
				elif self.variable(l1[i][0])==False and self.variable(l2[i][0])==True:
					self.dict[l2[i]]=l1[i]
					#print "can unify"
				elif self.variable(l1[i][0])==False and self.variable(l2[i][0])==False:
					if l1[i]!=l2[i]:
						return False
				elif self.variable(l1[i][0])==True and self.variable(l2[i][0])==True:
					self.dict[l2[i]]=l1[i]
			#print "dictionary",self.dict
			if i == len(l1)-1:
            			return True
			else:
        			return False
	def delete(self, root, ele):
        	if root.left is not None:
            		root.left = self.delete(root.left, ele)
        	if root.left is None and root.right is None:
            		if  root.value.value == ele.value.value and root.negation == ele.negation:
                		for i in range(0,len(ele.value.variables)):
                    			if ele.value.variables[i] != root.value.variables[i]:
                        			break
                		if i == len(ele.value.variables)-1:
                    			return None
                		else:
                    			for k in range(len(root.value.variables)):
                        			if root.value.variables[k] in self.dict.keys():
                            				root.value.variables[k] = self.dict[root.value.variables[k]]
            		elif (root.value.value!='|') and root.value.value != ele.value.value: 
                		for k in range(0,len(root.value.variables)):
                    			if root.value.variables[k] in self.dict.keys():

                        			root.value.variables[k] = self.dict[root.value.variables[k]]
		
        	if root.right is not None:
            		root.right = self.delete(root.right, ele)
        	return root

	

	def just_copy(self,obj):
		if obj is not None:
			term1=term(obj.value.value)
			term1.name=obj.value.value
			
			for i in range(0,len(obj.value.variables)):

				term1.variables.append(obj.value.variables[i])
			copy=node(term1)
			copy.negation=obj.negation
			copy.left=self.just_copy(obj.left)
			copy.right=self.just_copy(obj.right)
		else:
			return obj
		return copy	

	def solve(self,obj1,obj2):
		#print "TEMP BEGINS"
		#i=0
		#while i!=len(self.temp_kb):
		#	cnf.display(self.temp_kb[i])	
		#	print ""
		#	i=i+1
		#rint "TEMP KB ENDS"	
		list1=self.empty_list(obj1)
		list2=self.empty_list(obj2)
		
		#print "list1:",list1
		#print "list2:",list2
		for i in range(0,len (list1)):
			#print "element in 1",element1.value.value,len(list1),element1.value.variables
			#for element2 in list2:
			j=0
			while j<len(list2):
				#print "element in 2:",element2.value.value,len(list2),element2.value.variables
				if list1[i].value.value==list2[j].value.value and list1[i].negation!=list2[j].negation:
					#print "Yes"
					if obj1.unique is not None and hash(obj2) in obj1.unique:
                            			return False
                        		if obj2.unique is not None and hash(obj1) in obj2.unique:
                            			return False

					arglist1=list1[i].value.variables
					#print "Arguments :",list1[i].value.value,arglist1
						
					arglist2=list2[j].value.variables
					#print "Arguments :",list2[j].value.value,arglist2
					self.dict={}
					ans=self.unify(arglist1,arglist2)
					if ans==True:
						#print "can unify"
						if len(list1)==1 and len(list2)==1:
							print "length is 1"
							return True
						else:
							copy1=self.just_copy(obj1)
							copy2=self.just_copy(obj2)
							#print "Creating copy 1",copy1
							#print obj1
							#print "Creating copy 2",copy2
							#print obj2
							if len(list1)==1:
								copy1=None
							else:
								copy1=self.delete(copy1,list1[i])
								#print "deleted"
							if len(list2)==1:
								copy2=None
								#print "deleted"
							else:
								copy2=self.delete(copy2,list2[j])
								#print "deleted"
							#print "copy1 after deletion",cnf.display(copy1)
							#print "copy2 after deletion",cnf.display(copy2)
							combine=term("|")
							combine.name="|"
							n=node(combine)
							n.left=copy1
							n.right=copy2
							
							#cnf.display(n)
							#print list1
							#print list2
							new_hash1 = (hash(obj1))
                                			
                                			n.unique.append(new_hash1)
							new_hash2 = (hash(obj2))
                                			n.unique.append(new_hash2)
                                			if obj1.unique is not None:
								for m in range(0,len(obj1.unique)):
	
                                    					n.unique.append(obj1.unique[m])
                                			if obj2.unique is not None:
                                    				for h in range(0,len(obj2.unique)):
	
                                    					n.unique.append(obj2.unique[h])
							self.temp_kb.append(n)
							list1=list1[0:i]+list1[i+1:]
							list2=list2[0:j]+list2[j+1:]
							#print list1
							#print list2
							return False
				j=j+1
			#print "out of for"
		return False
	

if __name__ == "__main__":
	f=open("input1.txt","r")

	n_queries=f.readline().rstrip()
	
	query=[]
	for i in range(int(n_queries)):
		
		query.append(f.readline().rstrip())

	print query


			
	n_rules=f.readline().rstrip()
	
	kb=KB()
	for i in range(int(n_rules)):
		rule=f.readline().rstrip()
		kb.make_kb(rule)
	#print "facts are:",kb.facts
	#print "Imp are:",kb.for_prefix

	postfix=POST()
	expressions=postfix.convert(kb.for_prefix)
	#print "postfixes are:",postfix.expressions
	cnf=CNF()
	cnf.pre_cnf(postfix.expressions)
	#print "FINAL KB IS:"
	
	print kb.final_objects
	#print "Size:",len(kb.final_objects)
	#print kb.count
	for i in range(0,int(n_rules)):
		cnf.display(kb.final_objects[i])	
		print ""
	print "KB ENDS HERE"
	query_list=[]
	q_objects=[]
	for q in query:
		
		predicate,var=kb.splitword(q)
		#number=kb.convert(predicate)
		term1=term(predicate)
		term1.name=predicate
		term1.variables=var
		q_objects.append(term1)
		n=node(term1)
		
		
		if '~' in q:
			#n=node(number)
			n.negation=True
		else:
			#n=node(number)
			n.negation=False
		query_list.append(n) 
		#kb.final_objects.append(n)
		kb.objects.append(term1)
	
		
	#for object in kb.objects:s
	#	print "Name:",object.name
	#	print " Value:",object.value
	res=Resolution()
	res.resolution(query_list)
	
