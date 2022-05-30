name=input("Enter your name here:")
list=['Ananya','Yuvraj','Daddy','Mom','Dadi']
if list.__contains__(name) or name in list:
    print("Yes it already contains this name")
else:
    print("This is a new name")