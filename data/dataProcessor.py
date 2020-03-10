import json
import gzip
import csv

def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield json.loads(l)

meta = open("processed/meta.json", "r")
metaDict = json.load(meta)

with open("processed/data.csv", "w", newline="") as csvfile:
    for data in parse("raw/data.gz"):
        asin = data.get("asin", None)
        metadata = metaDict.get(asin, None)
        
        if metadata is not None:
            title = metadata["title"]
            artist = metadata["artist"]
            reviewerID = data["reviewerID"]
            rating = data["overall"]

            writer = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([reviewerID, title, artist, rating])
