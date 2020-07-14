import re
Data = open('Data.txt').read()
Names = re.findall('Name : (.*\S)',Data)
Emails = re.findall('Email : (\S*@\S*)',Data)
Phones = re.findall('Phone : (.+\d+)',Data)
List = []
for i in range(len(Names)):
    data = {'Name':Names[i],'Email':Emails[i],'Phone':Phones[i]}
    List.append(data)
#print(List)
print(List[1]['Name'])
print(List[1]['Email'])
print(List[1]['Phone'])