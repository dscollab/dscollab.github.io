from urllib.request import Request, urlopen
# This package let us send HTML requests and receive data.

url = "https://api.pokemontcg.io/v2/types"

req = Request(url, headers={'User-Agent': 'Colton'})
# A request object lets us add additional data to our url.
# It's important to add headers so the website knows who is accessing their website.
# In practice, just add them and don't worry about it too much.

contents = urlopen(req)
# This is where we actually retreive the data from the API.

html_bytes = contents.read()
html = html_bytes.decode("utf-8")
# We need to decode the html the website gives us.

print(html)