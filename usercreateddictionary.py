mydict= {
    "hamesha":"everyday",
    "joote":"shoes",
    "khaana" : "food",
    "ganda" : "dirty"
}
option=input("Enter 1 if you want to add a word and 2 if you want to explore")
option=int(option)
if(option==1):
        word=input("Enter word of you choice")
        meaning=input("Enter its meaning too")
        newdict={
            word:meaning
             }
        mydict.update(newdict)
        print(mydict.items())
else:
    print(mydict.items())