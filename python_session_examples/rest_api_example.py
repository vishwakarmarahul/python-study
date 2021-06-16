import requests
import json

req_url = 'https://jsonplaceholder.typicode.com/comments'
response = requests.get(req_url)
if response.status_code == 200:
    #pass string value only to loads
    comments = json.loads(response.text)
    for comment in comments:
        print(comment.get('email'))


