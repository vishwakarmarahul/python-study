import requests
image_url = 'https://upload.wikimedia.org/wikipedia/en/1/11/Demons_Souls_remake_cover_art.jpg'
response = requests.get(image_url)
# print(response.status_code)
if response.status_code == 200:
    with open('d:/temp/art2.jpg', 'wb') as file_o:
        file_o.write(response.content)