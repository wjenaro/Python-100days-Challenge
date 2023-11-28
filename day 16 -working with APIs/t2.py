import requests, json

res=requests.get("https://official-joke-api.appspot.com/random_joke")

#function to

def printResponse(obj):
    """
    Takes an object as input and prints it in a formatted JSON string.

    """
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

printResponse(res.json())