import json, requests
import urllib2
import urllib
import shutil
import requests
import os

API_KEY = os.environ["flickr_api_key"]

data = urllib2.urlopen(
    "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=" + API_KEY + "&tags=sunrise&lat=12.86&lon=77.78&radius=10&format=json&nojsoncallback=1")
json_data = json.load(data)
# print data2["photos"]["photo"][0]["id"]

print len(json_data.get("photos").get("photo"))

i = 0
for id in json_data["photos"]["photo"]:
    y = id["id"]

    get_sizes = urllib2.urlopen(
        "https://api.flickr.com/services/rest/?method=flickr.photos.getSizes&api_key=" + API_KEY + "&photo_id=" + y + "&format=json&nojsoncallback=1")
    get_imgs = json.load(get_sizes)
    # #get high res image
    # get_img_id= get_imgs.get("sizes").get("size")[-1].get("source")

    # get low res image
    get_img_id = get_imgs.get("sizes").get("size")[4].get("source")

    print get_img_id

    response = requests.get(get_img_id, stream=True)
    with open("0" + str(i) + '.jpg', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)
    del response

    i = i + 1
