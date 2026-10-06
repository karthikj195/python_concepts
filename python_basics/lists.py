l = [1, 2, 3]
l = list()

l = [1]
l.append(2)
l.append("abc")
l.append({2})
l.append([1, "abc", {"abc"}])
l.append(["hi", "hello"])
l.append((1, 2, 3))
print(l) #[1, 2, 'abc', {2}, [1, 'abc', {'abc'}], ['hi', 'hello'], (1, 2, 3)]

"extending a list using extend() method here we have to pass only iterables like list, tuple, set, dictionary etc"
l = [1]
l.extend("abc") # it will add each character of the string as a separate element in the list
print(l) #[1, 'a', 'b', 'c']

l.extend([2,3]) # it will add each element of the list as a separate element in the list
print(l) #[1, 'a', 'b', 'c', 2, 3]

l.extend(("hi")) # it will add each character of the string as a separate element in the list because tuple is an iterable and it will convert the string to a tuple of characters
print(l) #[1, 'a', 'b', 'c', 2, 3, 'h', 'i']

l.extend({"name": "karthik"}) # it will add each key of the dictionary as a separate element in the list because dictionary is an iterable and it will convert the dictionary to a list of keys
print(l) #[1, 'a', 'b', 'c', 2, 3, 'h', 'i', 'name']    

l.extend(["hello"]) # it will add each element of the list as a separate element in the list
print(l) #[1, 'a', 'b', 'c', 2, 3, 'h', 'i', 'name', 'hello']   

l.extend({"new"}) # it will add each element of the set as a separate element in the list because set is an iterable and it will convert the set to a list of elements
print(l) #[1, 'a', 'b', 'c', 2, 3, 'h', 'i', 'name', 'hello', 'new']    


"""pop method removes the last element from the list and returns it"""
l = [1, 'a', 'b', 'c', 2, 3, 'h', 'i', 'name', 'hello', 'new']
print(l.pop()) #'new'
print(l) #[1, 'a', 'b', 'c', 2, 3, 'h', 'i', 'name', 'hello']

print(l.pop(0)) #1
print(l) #['a', 'b', 'c', 2, 3, 'h', 'i', 'name', 'hello']  


"""remove method removes the first occurrence of the element from the list and returns it"""
l.remove("a") 
print(l) #['b', 'c', 2, 3, 'h', 'i', 'name', 'hello']

"""insert method inserts the element at the specified index in the list"""
l.insert(0, 1)
print(l) #[1, 'b', 'c', 2, 3, 'h', 'i', 'name', 'hello']

"""del statement removes the element at the specified index from the list"""

del l[0:3] # it will remove the elements from index 0 to 2
print(l) #[2, 3, 'h', 'i', 'name', 'hello']

"""count method returns the number of occurrences of the element in the list"""
l = [1, 2, 3, 1, 2, 3]
print(l.count(1)) #2    

"""sort method sorts the list in ascending order by default and returns None"""


