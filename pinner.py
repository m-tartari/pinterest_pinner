# \file    pinner.py
# \author  Michele Tartari
# \date    04/03/2019
# this file can be modified to work on any website by properly modifying lines 39:42
import sys
import json
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup

with open("./data.json") as f:
    json_obj = json.loads(f.read())
the_album = json_obj["the_album"]
access_token = json_obj["access_token"]
board_name = json_obj["board_name"]

the_page = urllib.request.urlopen(the_album)
soup = BeautifulSoup(the_page, "html.parser")
print("Saving pictures from '"+soup.title.text +
      "' into the board '"+board_name+"'.")

# find board ID
api_request_url = "https://api.pinterest.com/v1/me/boards/?access_token=" + \
    access_token + "&fields=id%2Cname%2Curl"
board_list = requests.get(api_request_url).json()
for item in board_list['data']:
    if item['name'] == board_name:
        board_id = item["id"]
        print(board_name, "has ID=", board_id)


# generate url for api request to generate pins
api_request_url = "https://api.pinterest.com/v1/pins/?access_token=" + access_token

# finds all image urls from page and save them
print("Working on it...")
i = 0
total = len(soup.find_all('a', {"class": "fbPhoto"}))
for link in soup.find_all('a', {"class": "fbPhoto"}):
    the_href = str(link.get('href'))
    the_caption = soup.title.text+" "+str(link.get('title'))

    # create json request for pintest
    payload = {
        "board": board_id,
        "note": the_caption,
        "image_url": the_href,
        "link": the_album
    }
    r = requests.post(api_request_url, json=payload)
    i = i+1
    progres = i/total*100

    sys.stdout.write('\x1b[1A') # CURSOR_UP_ONE_LINE
    sys.stdout.write('\x1b[2K') # ERASE_LINE
    print("Working on it... Done "+"{0:.1f}".format(progres)+"%")

print("Finished, Pinned "+str(i)+" images")
