"""SETS
1. sets are annoted by curly {} or set()
2. sets stores only unique elements and duplicates are removed
3. sets are unordered that means there is no indexing  you can not add any valur that is immutable
4.sets are Heterogenous
5.sets are SEMI-MUTABLE
"""
#s={}#DIC
#s=set()#EMPTY SET
"""print(type(s))"""
#removal
"""s={1,2,2,3,3,4}
print(s)"""
#unordered
"""s={1,1,2,2,3,4,5,70.2,"sample"}
print(s)
"""
#TYPE CONVERSION LIST TO SETS
"""l=[1,1,2,2,3,4,5]
print(set(l))"""
#SETS METHOD
  #1. .add()->add the value
"""s={1,2,3,4}
s.add(5)"""
  #2. .remove()->remove an element if the e;ement didnt exits we will get an KEY-ERROR
"""s.remove(100)
print(s)"""
  #3. .discard()-> will not show any error if it is not present in set
"""s.discard(100)
print(s)"""

"""!! SETS OPERATION !!"""
# s1={1,2,3,4}
# s2={4,5,6,7,8}
"""1. .union()
merge both the sets"""
# print(f"UNION-> {s1.union(s2)}") 
  #another method without using .union is
#print(f"UNION->{s1|s2}")
"""2. .intersection()
common element"""
# print(f"INTERSECTION->{s1.intersection(s2)}")
   #another method without using .intersection is
# print(f"INTERSECTION->{s1 & s2}")
"""3. .difference()
element present in one sets but not in another"""
# print(f"DIFFERENCE->{s1.difference(s2)}")
# print(f"DIFFERENCE->{s2.difference(s2)}")  #esme dono diff. hote hai
   #another method without using .difference is
#print(f"DIFFERENCE ->{s1-s2}")
"""4. .symmetric_difference()
 """
# print(f"SYMMETRIC->{s1.symmetric_difference(s2)}")
#print(f"SYMMETRIC->{s1^s2}")
"""s={} #empty dic
s=set()#empty set"""
#use of FROZEN SET -> it make any set fixed nothing could be added or removed from it
"""s=frozenset([1,2,3,4,5])
s.add(6)
print(s)"""
