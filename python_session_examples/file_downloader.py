import requests
image_url = 'https://upload.wikimedia.org/wikipedia/en/1/11/Demons_Souls_remake_cover_art.jpg'

#Get Image Content
response = requests.get(image_url)

#Check Status Code
if response.status_code == 200:
    #Write to file.
    with open('d:/temp/art.jpg', 'wb') as file_o:
        file_o.write(response.content)