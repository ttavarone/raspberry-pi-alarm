import urllib.request
import json
term = "water"
contents = urllib.request.urlopen("http://api.urbandictionary.com/v0/define?term="+term).read()
definition = json.loads(contents)
for p in contents['list']:
        print(p['definition'])
