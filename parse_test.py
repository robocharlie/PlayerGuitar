# http://docs.python-guide.org/en/latest/scenarios/scrape/

from lxml import html
import requests

page = requests.get('https://tabs.ultimate-guitar.com/v/van_halen/panama_ver3_tab.htm')
tree = html.fromstring(page.content)

print(tree)