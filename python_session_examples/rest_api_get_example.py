import json
import requests

'''
GET
POST
PUT
DELETE
'''
# #Get Example
# response = requests.get('https://jsonplaceholder.typicode.com/photos')
# if response.status_code == 200:
#     photos = json.loads(response.text)
#     for photo in photos:
#         print(photo.get('url'))
#
# #Post Example
# comment = {'postId': 1,
#             'name': 'rahul',
#             'email': 'abc@xyz.com',
#             'body': 'This is my comment'}
#
# data = json.dumps(comment)
# response = requests.post('https://jsonplaceholder.typicode.com/comments', data=data)
# print(response.status_code)
# print(response.text)
#
# '''
# PUT Example
# '''
# comment = {'name': 'rahul'}
# response = requests.put('https://jsonplaceholder.typicode.com/comments/1', data=comment)
# print(response.status_code)
# print(response.text)
#

'''
DELETE Example
'''
response = requests.delete('https://jsonplaceholder.typicode.com/comments/1')
print(response.status_code)
print(response.text)

