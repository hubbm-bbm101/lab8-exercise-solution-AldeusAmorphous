import sys

students={}

with open("student.txt","r") as f:
    for i in f.readlines():
        name=i.strip().split(":")[0]
        uni=i.strip().split(":")[1]
        students[name]=uni
for i in sys.argv[1].split(","):
    if i in students.keys():
        print("Name: "+ i +", "+ students[i])
    else:
        print("No record of '"+ i +"' was found!")