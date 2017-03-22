# py-mapzen-whosonfirst-geojson

Python tools for doing GeoJSON related things with Who's On First data

## Install

```
sudo pip install -r requirements.txt
```

## Usage

### mapzen.whosonfirst.geojson.encoder

This is the primary (and so far only) use for this package. Basically it exists for two purposes:

* Ensure that the `geometry` property of GeoJSON features are _not_ indented while everything else is
* Optionally ensure that coordinates are trimmed to `n` decimal points
  by passing argument to the constructor (the default is `None` which
  is to leave coordinates unchanged)

For example:

```
import sys
import geojson
import mapzen.whosonfirst.geojson

path = '/path/to/101/736/545/101736545.geojson'

fh = open(path, 'r')
f = geojson.load(fh)

e = mapzen.whosonfirst.geojson.encoder(precision=None)
e.encode_feature(f, sys.stdout)
```

Would yield:

```
{
  "id": 101736545,
  "type": "Feature",
  "properties": {
    "edtf:cessation":"u",
    "edtf:inception":"u",
    "geom:area":0.049595,
    "geom:bbox":"-73.974351,45.409653,-73.474127,45.707578",
    "geom:latitude":45.526620,
    "geom:longitude":-73.652698,
    "gn:population":3268513,
    "iso:country":"CA",
    "lbl:latitude":45.572744,
    "lbl:longitude":-73.586295,
    "mps:latitude":45.572744,
    "mps:longitude":-73.586295,
    "name:chi_p":[
        "\u8499\u7279\u5229\u5c14"
    ],
    "name:chi_v":[
        "\u8499\u7279\u5229\u723e"
    ],
    "name:eng_p":[
        "Montreal"
    ],
    "name:eng_s":[
        "Montreal",
        "City of Saints",
        "The Golden City",
        "City of a thousand bell towers",
        "La ville aux cent clochers",
        "The Belltower",
        "Sin City",
        "The Amsterdam of North America",
        "The City Light",
        "The Lamp",
        "The Big Island",
        "The Metropolis",
        "Frenchtown",
        "The City-Mountain",
        "Mount Real",
        "Silvercity",
        "Royal City",
        "The City of Saints",
        "The Festival City",
        "MTL",
        "Montr\u00e9alit\u00e9",
        "La M\u00e9tropole",
        "Hollywood North",
        "YUL"
    ],
    "name:eng_v":[
        "YMQ"
    ],
    "name:fre_p":[
        "Montr\u00e9al"
    ],
    "name:ger_p":[
        "Montreal"
    ],
    "name:jpn_p":[
        "\u30e2\u30f3\u30c8\u30ea\u30aa\u30fc\u30eb"
    ],
    "name:kor_p":[
        "\ubaac\ud2b8\ub9ac\uc62c"
    ],
    "qs:a0":"Canada",
    "qs:a1":"*Quebec",
    "qs:a1_lc":"QC",
    "qs:a1r":"*",
    "qs:adm0":"Canada",
    "qs:id":0,
    "qs:la_lc":"*",
    "qs:level":"locality",
    "qs:loc":"Montr\u00e9al",
    "qs:loc_alt":"Montr\u00e9al",
    "qs:loc_lc":"08b1ec0ebe3d11d892e2080020a0f4c9",
    "qs:pop":0,
    "qs:source":"NCanada Census",
    "qs:type":"Ville",
    "src:geom":"quattroshapes",
    "src:geom_alt":[],
    "src:lbl:centroid":"mapshaper",
    "wof:belongsto":[
        102191575,
        85633041,
        136251273
    ],
    "wof:breaches":[],
    "wof:concordances":{
        "fct:id":"03c06bce-8f76-11e1-848f-cfd5bf3ef515",
        "gn:id":6077243,
        "gp:id":3534,
        "tgn:id":7013051
    },
    "wof:country":"CA",
    "wof:geomhash":"61796e06fa083f36a12ff04906e440c2",
    "wof:hierarchy":[
        {
            "continent_id":102191575,
            "country_id":85633041,
            "locality_id":101736545,
            "region_id":136251273
        }
    ],
    "wof:id":101736545,
    "wof:lastmodified":1442973034,
    "wof:megacity":"1",
    "wof:name":"Montr\u00e9al",
    "wof:parent_id":136251273,
    "wof:placetype":"locality",
    "wof:scale":"1",
    "wof:superseded_by":[],
    "wof:supersedes":[],
    "wof:tags":[]
},
  "bbox": [-73.974351,45.409653,-73.474127,45.707578],
  "geometry": {"coordinates":[ ... ],"type":"Polygon"}
}
```

## Caveat

I wish we didn't have to this. If there's a way to do this using the
default ["override the JSONEncoder class"](https://docs.python.org/2/library/json.html#encoders-and-decoders)
stuff in Python – without converting things in to strings – then I'd love to
hear about it.

## See also

* https://github.com/whosonfirst/py-mapzen-whosonfirst-export
