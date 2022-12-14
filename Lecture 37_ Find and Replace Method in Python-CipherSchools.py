# replace() method
# find() method
string= "is She is beutiful and she is a good dancer"
# print(string.replace("is","was",2))

# print(string.find("is",1))
is_pos1= string.find("is")
is_pos2= string.find("is", is_pos1+1)
print(is_pos2)
