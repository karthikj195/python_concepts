"""Representation of strings in Python"""
a = "Hello"
a = 'Hello'
a = """Hello"""
a = '''Hello'''
a = "'Hello'"


"""Stringa are immutable in python. we cannot change the value of string once it is created. 
if we try to change the value of string, it will create a new object in memory and assign the new value to that object. 
the old object will be garbage collected if there are no references to it."""

s1 = "fun"
s2 = "gun"
s1 = s2
print(id(s1)) #4371880512
print(id(s2)) #4371880512
print(s2) #gun


"""indexing of strings in python. 
we can access the characters of a string using indexing."""

s = "Hello"
print(s[0]) #H
print(s[1]) #e
print(s[2]) #l
print(s[3]) #l
print(s[4]) #o

f = "hi hello how are you"

"""to find first n characters"""
print(f[:4]) #hi h


"to find last n characters"
print(f[-3:]) #you


"string formatting in python"

"""placeholder for string formatting"""
s = "my name is %s and I am %d years old" %("karthik", 29)
print(s) #my name is karthik and I am 29 years old

".format() method for string formatting"
s = "my name is {} I am {} years".format("karthik", 29)
print(s) #my name is karthik I am 29 years

s = "my name is {name} I am {age} years".format(name="karthik", age=29)
print(s) #my name is karthik I am 29 years

s = "my name is {0}, I am {1} years".format("karthik", 29)
print(s)


"f strings for string formatting"

name = "karthik"
age = 29

s = f"my name is {name} and my age is {age}"
print(s) #my name is karthik and my age is 29


"string methods"

s = "Hi heLLO How ARe you"
print(s.upper())  #HI HELLO HOW ARE YOU
print(s.lower())  #hi hello how are you
print(s.capitalize()) #Hi hello how are you
print(s.casefold())  #hi hello how are you
print(s.swapcase()) #hI HEllo hOW arE YOU
print(s.title())  #Hi Hello How Are You
print(s.index("H")) #0
print(s.rindex("o")) #18
print(s.find("h"))  #3
print(s.rfind("u")) #19
print(s.count("o")) #2 
print(s.count("o", 1))      #2
print(s.count("o", 1, 10))   #0
print(s.startswith("hi"))   #False. it is case sensitive
print(s.endswith("you"))   #True. it is case sensitive
print(s.split())       #["Hi", "heLLO", "How", "ARe", "you"]
print(s.split(" ")) #["Hi", "heLLO", "How", "ARe", "you"]
print(s.split("H")) #["", "i ", "eLLO ", "ow ARe you"]
print(s.split("o")) #["Hi heLLO H", "w ARe y", "u"]
print(s.replace("h", "k")) #Hi keLLO How ARe you
print(s.replace("H", "k", 2)) #ki heLLO kow ARe you
print(len(s))