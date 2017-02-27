import pywinauto
from lxml import html
import requests


search_string = "oasis+wonderwall"

page = requests.get("https://www.ultimate-guitar.com/search.php?search_type=title&order=&value="
                    + search_string)

tree = html.fromstring(page.content)

rating = tree.xpath('//span[@class="ratdig"]/text()')
rating

# Start tuxguitar
# app = pywinauto.Application().start("C:/Program Files (x86)/tuxguitar-1.4/tuxguitar.exe")
# app.TuxGuitarUntitled.menu_select("File->Open")
# app.TuxGuitarUntitled.click()
