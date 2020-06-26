#Serialization
import json
from pprint import pprint
#Python list object containing many dictionaries
students=[
    {'id':101,'name':'kisan','course':'python','isJoined':False,'isMarried':None},
    {'id':102,'name':'Kumar','course':'Django','isJoined':True,'isMarried':True},
    {'id':103,'name':'Behera','course':'Django-REST-API','isJoined':False,'isMarried':None},
]
pprint(students)
#Function For Dumping into a File
def dumpIntoFile(fileName,students,/):
    with open(file=fileName,mode='w') as jsonFile:
        json.dump(students,jsonFile,indent=0,separators=(',',':'))
        print('Json File Created Successfully')

def main():
    dumpIntoFile('./json/demo2.json',students)
main()