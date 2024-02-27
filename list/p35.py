# intersection_update() method removes the items from the original set  
#where intersection not remove the items form original set
a = {"Devansh", "bob", "castle"}
b = {"castle", "dude", "emyway"}
c = {"fuson", "gaurav", "castle"}
a.intersection_update(b, c)
print(a)