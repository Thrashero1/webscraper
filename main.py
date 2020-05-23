from bs4 import BeautifulSoup
import requests

search = input("Enter search term: ")
param = {"q": search}
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'}
r = requests.get("http://www.bing.com/search", params=param, headers=header)
print(r.url)

soup = BeautifulSoup(r.text, "html.parser")


# first type in the html tag you are looking for followed by a dictionary of the attributes you want
results = soup.find(id="b_results")

links = soup.find_all("li", {"class": "b_algo"})

for item in links:
    # this is looking for the a tag in the element which contains the href and text associated with the hyperlink
    item_text = item.find("a").text
    # here we look for the attributes of the tag which in this case is the link (href). This is when we want a specific
    # attribute
    item_href = item.find("a").attrs["href"]
    # lists all child elements of the parent


    if item_text and item_href:
        print("This is the search result:", item_text)
        print("This is the link:", item_href)
        print("Parent", item.find("a").parent)
        # finds the parent of the parent or use one of the alternatives below if there is only one element
        # or unique name
        print("Description option 1", item.find("a").parent.parent.find("p").text)
        print("Description option 3", item.find("p").text)

        children_elements = item.children
        for child in children_elements:
            print("This is a child:", child)

        specific_child = item.find("h2")
        print("This is the child of the h2 element:", specific_child.next_sibling, "\n")

