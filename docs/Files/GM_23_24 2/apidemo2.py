from urllib.request import Request, urlopen

url = "https://www.google.com/finance/quote/BTC-USD"

req = Request(url, headers={'User-Agent': 'Colton'})

contents = urlopen(req)

html_bytes = contents.read()
html = html_bytes.decode("utf-8")

string = "\"Bitcoin (BTC / USD)\",3,null,["
# I found this string by searching up the string I wanted (at the time 63000)
# Then I can find the strings around it.

index = html.find("\"Bitcoin (BTC / USD)\",3,null,[")
# This finds where that string is in our html

print(html[index+len(string):index+len(string)+5])
# This prints out the next 5 digits after our string