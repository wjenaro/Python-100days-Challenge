import requests, json

res=requests.get("https://official-joke-api.appspot.com/random_joke")

#function to

def printResponse(obj):
    """
    Takes an object as input and prints it in a formatted JSON string.

    Args:
        obj (object): The object to be printed as a JSON string.

    Returns:
        None

    Example:
        response = {"name": "John", "age": 30}
        printResponse(response)
        # Output:
        # {
        #     "age": 30,
        #     "name": "John"
        # }
    """
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

printResponse(res.json())