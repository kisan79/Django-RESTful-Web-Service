#Deserialization
from pprint import pprint
import json

#Function For Deserialisation
def loadFromFile(fileName):
    with open(file=fileName,mode='r') as file:
        res=json.load(file)
        pprint(res)
    #Checking whether file is closed or not
    # print(f'{fileName} isCloased?? {file.closed}')

def main():
    loadFromFile('./json/demo2.json')
main()