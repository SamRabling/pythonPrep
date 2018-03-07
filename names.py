#part 1

# students = [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
# ]

# def studentsInfo(info):
#      for i in info:
#         print i['first_name'] + ' ' + i['last_name']
# studentsInfo(students)

#part 2
users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }

def studentInstructors(info):
    listStu = info['Students']
    print 'Students'
    for i in range(len(listStu)):
        student_dict = listStu[i]
        stuFname = student_dict['first_name']
        stuLname = student_dict['last_name']
        fullNameStu = stuFname + ' ' + stuLname
        charStu = len(fullNameStu)-1
        print  str(i+1) + ' - ' + fullNameStu + ' - ' + str(charStu)

    print 'Instructors'
    listInst = info['Instructors']
    for i in range(len(listInst)):
        instructor_dict = listInst[i]
        instFname = instructor_dict['first_name']
        instLname = instructor_dict['last_name']
        fullNameInst = instFname + ' ' + instLname
        charInst = len(fullNameInst)-1
        print str(i+1) + ' - ' + fullNameInst + ' - ' + str(charInst)

        
studentInstructors (users)