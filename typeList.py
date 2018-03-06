#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"

# print len(l)
i = 0
count = 0
string = "String:"
if type(l) != int:
        print "The list you entered is of mixed type"
for i in l: 
    if type(i) == int:
        count = count + i
    if type(i) == str:
        string = string + " " + i
    if type(i) == float:
        count = count + i
print "Sum: {}".format(count)
print string

# input
# m = [2,3,1,7,4,12]
# #output
#  if type(m) = int:
#      print "The list you entered is of integer type"
     
