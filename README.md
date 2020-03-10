# CS3244 Project AY19/20 S2

## Dataset

### [Raw](./data/raw/)

Raw data [downloaded here](http://deepyeti.ucsd.edu/jianmo/amazon/index.html)

### [Processed](./data/processed/)

#### `meta.json`

- Generated using `metaProcessor.py`
- Maps the serial number `ASIN` to song title and song artist
- Reading this file using `json.load` will give a `dict` of `{ ASIN: { "title": TITLE, "artist": ARTIST }, ... }`

#### `data.csv`

- Generated using `dataProcessor.py`
- Has headers `Reviewer ID | Song Title | Artist | Rating`
