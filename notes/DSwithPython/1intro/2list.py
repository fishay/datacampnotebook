x = ["a", "b", "c", "d"]
x[1:3]
return ["b","c"]
x[1:] = ["b","c","d"]
del(x[])
shallow copy 
deep copy for list:
y = list(x)
y = [:]

x = ["a", "b", "c", "d"]
y = x + ["e", "f"]
