from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os


def start_search():
    search = input("Search for:")
    params = {"q": search}
    dir_name = search.replace(" ", "_").lower()

    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)

    r = requests.get("http://www.bing.com/images/search", params=params)
    print(r.url)

    soup = BeautifulSoup(r.text, "html.parser")

    links = soup.find_all("a", {"class": "thumb"})

    for item in links:
        img_obj = requests.get(item.attrs["href"])
        print("Showing:", item.attrs["href"])
        title = item.attrs["href"].split("/")[-1]
        try:
            image = Image.open(BytesIO(img_obj.content))
            image.save("./" + dir_name + "/" + title, image.format)
            print("saved!", image.size)
        except:
            print("image can't be saved")

    start_search()


start_search()
