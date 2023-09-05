import requests
import json

res = requests.get('http://api.open-notify.org/iss-now.json')

# Check if the response status code is OK (200)
if res.status_code == 200:
    # Parse the JSON response
    data = res.json()
    # Check if the "message" field exists in the JSON response
    if 'message' in data:
        msg = data['message']
        print(msg)
    else:
        print("The 'message' field is not present in the JSON response.")
else:
    print(f"Error: Unable to fetch data. Status code: {res.status_code}")
