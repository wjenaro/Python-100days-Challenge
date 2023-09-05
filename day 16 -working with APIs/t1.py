import requests

response = requests.get("https://www.boredapi.com/api/activity")

print(response.status_code)
print(response.json())

# Writing the content into a text.txt file
with open('data.txt', 'wb') as file:  # Use 'wb' for binary write mode
    file.write(response.content)
