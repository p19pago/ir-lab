from urllib.request import urlopen
url = "http://shakespeare.mit.edu/romeo_juliet/romeo_juliet.1.1.html"
page = urlopen(url)
page
<http.client.HTTPResponse object at 0x105fef820>
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
