import requests
import re

url = 'https://www.facebook.com/qnightclub/events'  # TODO: interate
# in the text/html version fb includes all the event json
headers = {'accept': 'text/html'}
r = requests.get(url, headers=headers)


matches = re.search(
    '[^\n]*__bbox.*upcoming_events[^\n]*', r.text)

print(matches.group(0))
