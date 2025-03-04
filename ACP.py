s={1,1,2,3,4,5,6,6,7,8,9}
print(s)

s1={1,2,4,5,8,9,11}
s2={3,6,10,25,4}

print("\n s1:",s1)
print("\n s2:",s2)
print("\n" ,s1.difference(s2))
print(s1.symmetric_difference(s2))
print(s1.union(s2))
print(s1.intersection(s2))