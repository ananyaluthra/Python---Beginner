marks=[]
for i in range(0,6):
    x=input("Enter your marks here:")
    x=int(x)
    marks.insert(i,x)
marks.sort()
print(marks)
