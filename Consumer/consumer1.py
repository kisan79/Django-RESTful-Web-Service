#Importing HTTP library requests
import requests
''' Javascript Object notation '''
import json

def main():
    URL1="http://127.0.0.1:8000/html"
    URL2="http://127.0.0.1:8000/json"
    URL3="http://127.0.0.1:8000/json2"
    # getResponse(URL1)
    getResponse(URL2)
    getResponse(URL3)
def getResponse(url):
    #Getting Httpresponse Using get method of http
    response=requests.get(url)
    
    print(response.status_code)
    print(response)
    #for getting data in str form
    print(response.text)
    #for getting data in bytes form
    print(response.content)
    #loads will deserialize str/bytes/bytearray instance containing json into python object form
    dict_data=json.loads(response.content)
    print(dict_data)


#Executing main fun
main()