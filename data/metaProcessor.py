import json
import gzip

def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield json.loads(l)

idToInfo = {}

for data in parse("raw/meta.gz"):
    title = data.get("title", None)
    artist = data.get("brand", None)
    asin = data.get("asin", None)
    
    if asin is not None:
        idToInfo[asin] = {
            "title": title,
            "artist": artist
        }

processedJson = json.dumps(idToInfo)

f = open("processed/meta.json", "w")

f.write(processedJson)
f.close()