sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']



def filter(myvar):
    if isinstance(myvar,int):
        if myvar >= 100:
            print "That's a big number!"
        if myvar <=100:
            print "That's a small number!"
    if isinstance(myvar,str):
        if len(myvar) >= 50:
            print "long sentence"
        if len(myvar) <= 50:
            print "short sentence"
    if isinstance(myvar,list):
        if len(myvar) >= 10:
            print "Big list!"
        if len(myvar) <=10:
            print "Short list!"
filter()