# http://docs.python-guide.org/en/latest/scenarios/scrape/

from lxml import html
import requests

page = requests.get('https://tabs.ultimate-guitar.com/v/van_halen/panama_ver3_tab.htm')
tree = html.fromstring(page.content)

tab_contents = tree.xpath('//pre[@class="js-tab-content"]/text()')

print(tab_contents)

file = open("panama_dump.txt", "w+")

file.write(str(tab_contents))
