# name = "      Har    shit   "
# dots="..........."
# print(name+dots)
# print(name.lstrip()+dots)
# print(name.rstrip()+dots)
# print(name.strip()+dots)
# print(name.replace(" ", "")+ dots)

name, char= input("Enter comma seprated name and character :  ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count: {name.strip().lower().count(char.strip().lower())}")
# name.strip().lower().count(char.strip().lower())
# char.strip().lower()
