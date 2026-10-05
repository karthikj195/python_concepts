a = "name"
b = a
print(a)
print(b)

print(id(a))   #4324349384
print(id(b)) # 4324349384
"both are pointing to the same object in memory"


s = "karthik"
t = "karthik"

print(id(s))  #4331018480
print(id(t))  #4331018480

"""both are pointing to the same object in memory because strings are immutable in python because both contains same data"""


f = "hi"
g = "hello"

print(id(f))  
print(id(g))