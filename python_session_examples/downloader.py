'''
arguments: -url
'''
import os
import requests
import argparse

DOWNLOADS_DIR = 'd:/temp/downloaded/'

def download_file(url):
    print('Downloading URL : {}'.format(url))
    response = requests.get(url)
    if response.status_code == 200:
        #https://dropbox.com/container/xyz.pdf
        file_name = url.split('/')[-1]
        print(file_name)

        #Check if path doesn't exists then create the PATH
        if not os.path.exists(DOWNLOADS_DIR):
            os.makedirs(DOWNLOADS_DIR)

        with open(DOWNLOADS_DIR + file_name, 'wb') as file_o:
            file_o.write(response.content)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', help='URL to download.')
    arguments = parser.parse_args()
    download_file(arguments.url)
else:
    print('Calling from another module')
    print(__name__)

#'http://www.africau.edu/images/default/sample.pdf'

