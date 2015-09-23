# py-mapzen-whosonfirst-geojson

Python tools for doing GeoJSON related things with Who's On First data

## Usage

### mapzen.whosonfirst.geojson.encoder

This is primary (and so far only) use for this package. Basically it exists for two purposes:

* Ensure that coordinates are trimmed to (6) decimal points
* Ensure that the `geometry` property of GeoJSON features are _not_ indented while everything else is

For example:

```
import mapzen.whosonfirst.geojson
import sys
import geojson

path = '/path/to/101/736/545/101736545.geojson'

fh = open(path, 'r')
f = geojson.load(fh)

e = mapzen.whosonfirst.geojson.encoder()
e.encode_feature(f, sys.stdout)
```

Would yield:

## Caveat

I wish we didn't have to this.

## See also