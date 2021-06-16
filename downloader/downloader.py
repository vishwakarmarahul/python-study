'''
arguments: -url
'''
import os
import requests
import argparse
import settings
import traceback

class Downloader:
    def download_file(self, url):
        try:
            if url is None or url == '':
                return

            print('Downloading URL : {}'.format(url))
            response = requests.get(url)
            if response.status_code == 200:
                #Example: https://dropbox.com/container/xyz.pdf
                file_name = url.split('/')[-1]

                #Check if path doesn't exists then create the PATH
                if not os.path.exists(settings.DOWNLOADS_DIR):
                    os.makedirs(settings.DOWNLOADS_DIR)

                with open(settings.DOWNLOADS_DIR + file_name, 'wb') as file_o:
                    file_o.write(response.content)
        except Exception as e:
            #print only error message.
            print(str(e))

            #Print detailed error and trace to its origin
            print(traceback.format_exc())

    def batch_download(self, file_path_text):
        try:
            if file_path_text is None or file_path_text == '':
                return

            if not '.txt' in file_path_text:
                return

            if not os.path.exists(file_path_text):
                return

            with open(file_path_text, 'r') as file_o:
                for url in file_o:
                    new_url = url.strip()
                    self.download_file(new_url)
        except:
            pass
