# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import sys
import json
import logging
import re

float_pat = re.compile(r'^-?\d+\.\d+(e-?\d+)?$')
charfloat_pat = re.compile(r'^[\[,\,]-?\d+\.\d+(e-?\d+)?$')
        
class encoder:

    def __init__(self, **kwargs):

        indent = kwargs.get('indent', 2)
        indent = int(indent)

        if indent <= 0:
            indent = None

        precision = kwargs.get('precision', None)

        if precision != None:

            precision = int(precision)

            if precision <= 0:
                precision = None

        fmt = None

        if precision != None:
            fmt = "%." + str(precision) + "f"

        self.indent = indent
        self.precision = precision
        self.fmt = fmt

    def _encode(self, data, fh, indent):

        # From TileStache's vectiles GeoJSON encoder thingy
        # (20130317/straup)
        
        encoder = json.JSONEncoder(separators=(',', ':'), indent=indent, sort_keys=True)
        encoded = encoder.iterencode(data)

        for token in encoded:

            if charfloat_pat.match(token) and self.precision:
                # in python 2.7, we see a character followed by a float literal
                fh.write(token[0] + self.fmt % float(token[1:]))

            elif float_pat.match(token) and self.precision:
                # in python 2.6, we see a simple float literal
                fh.write(self.fmt % float(token))
            
            else:
                fh.write(token)

    def encode_feature(self, feature, fh=sys.stdout):

        spec = {
            'id' : '',
            'type': 'Feature',
            'properties': {},
            'bbox': [],
            'geometry': {}
        }

        fh.write("{\n")

        for k in ('id', 'type', 'properties', 'bbox', 'geometry'):

            default = spec[k]

            fh.write(' ' * self.indent)
            fh.write('"%s": ' % k)

            if k in ('bbox', 'geometry'):
                self._encode(feature.get(k, default), fh, None)
            else:
                self._encode(feature.get(k, default), fh, self.indent * 2)

            if k != 'geometry':
                fh.write(',')

            fh.write('\n')

        fh.write('}')

if __name__ == '__main__':

    import geojson

    e = encoder()

    for path in sys.argv[1:]:

        fh = open(path, 'r')
        f = geojson.load(fh)

        e.encode_feature(f)
