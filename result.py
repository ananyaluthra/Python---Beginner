maths=int(input("Enter marks here:"))
eng=int(input("Enter marks here:"))
sci=int(input("Enter marks here:"))
if maths>=33:
    print("You are pass in maths")
else:
    print("You are fail in maths")
if eng>=33:
    print("You are pass in eng")
else:
    print("You are fail in eng")
if sci>=33:
    print("You are pass in sci")
else:
    print("You are fail in sci")
if (maths+eng+sci)/3 >= 40:
    print("You are pass overall")
else:
    print("You have failed. Kindly repeat you semester")