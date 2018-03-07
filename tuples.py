# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
[("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def myTuples(dicto):
    lst = []
    for key in dicto:
        name = key
        phone = dicto[key] 
        myTuple = (name, phone)
        lst.append(myTuple)
    print lst

myTuples(my_dict)