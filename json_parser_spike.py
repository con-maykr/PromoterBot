import requests
import re

url = 'https://www.facebook.com/events/2817360921721103'  # TODO: interate
# in the text/html version fb includes all the event json
headers = {'accept': 'text/html'}
r = requests.get(url, headers=headers)


title = re.search(
    r'id="pageTitle">(.*)</title>', r.text, flags=re.M | re.DOTALL).group(1)


time = re.search(
    r'id="title_subtitle"><span aria-label="([^"]*)', r.text, flags=re.M | re.DOTALL).group(
    1)

imageURL = re.search(
    r'class="scaledImageFitHeight img" src="([^"]+)"', r.text, flags=re.M | re.DOTALL).group(1).replace("&amp;", "&")


print(title, time, imageURL)


# ///.replace("&amp;", "&")
