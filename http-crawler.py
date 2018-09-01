import urllib, htmllib, formatter
website = urllib.urlopen("http://www.feemic.cn/mooc/icourse163/1002644012?type=hot#myTab")
data = website.read()
website.close()
format = formatter.AbstractFormatter(formatter.NullWriter())
ptext = htmllib.HTMLParser(format)
ptext.feed(data)
for link in ptext.anchorlist:
  if link[-6:] == "sd.mp4" : 
    print link
