#Serialization :Dumping Python Object into File Byte-Stream
import json
#Python dict obj
student={
    'id':101,
    'name':'kisan',
    'course':'python',
    'isJoined':False,
    'isMarried':None
    }
print(student)

#Function For Dumping dict into a File
def dumpIntoFile(fileName,d1,/):
    with open(file=fileName,mode='w') as jsonFile:
        json.dump(d1,jsonFile)
        print('Json File Created Successfully')

def main():
    dumpIntoFile('./json/demo1.json',student)
main()
