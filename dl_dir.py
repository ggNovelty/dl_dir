import os
import re
import requests
import urllib.request

from bs4 import BeautifulSoup


# often need a non-blank user-agent
headers = {'user-agent': 'test-app/0.0.1'}

print('Welcome to dl_dir.py\n')
print('Please enter directory URL: ')
base_url = input()


# standardizing url
base_url = base_url.lower()

if base_url[:4] == 'http':

    if base_url[:5] == 'https':
        base_url = base_url[8:]

    else:
        base_url = base_url[7:]

if base_url[:3] == 'www':
    base_url = base_url[4:]

if base_url[-1:] != "/":
    base_url += "/"


new_dir = base_url.replace("/", "\\")
os.mkdir(new_dir)
print("Beginning work on " + new_dir)



def build_dir(url, os_dir):

    os.chdir(os_dir)
    http_url = "http://" + url

    r = requests.get(http_url, headers = headers)
    soup = BeautifulSoup(r.text, 'html.parser')

    for link in soup.find_all('a'):
        destination = link.get('href')

        #parent dir
        if destination[0] == "/":
            pass

        # if destination is a 3 or 4 char extension (file), download it
        elif re.search(r"^.+\....?$", destination):

            try:
                print("downloading " + http_url + destination)
                print("to: " + os.getcwd() + "/" + destination)
                urllib.request.urlretrieve(http_url + destination, destination)

            except:
                print("error downloading" + destination)
                pass
        
        # sub dir
        elif (destination[-1:] == "/"):

            new_dir_name = destination.replace("/", "\\")
            print("Creating " + new_dir_name)

            os.mkdir(new_dir_name)

            build_dir(url + destination, new_dir_name)

        else:
            pass

    os.chdir("..")

    return("finished downloading dir: " + str(url))


build_dir(base_url, new_dir)
