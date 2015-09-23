# https://pythonhosted.org/setuptools/setuptools.html#namespace-packages
__import__('pkg_resources').declare_namespace(__name__)

import sys
import json
import logging
import re

class encoder:

    def __init__(self, **kwargs):
        self.indent = kwargs.get('indent', 2)

    def _encode(self, data, fh, indent):

        # From TileStache's vectiles GeoJSON encoder thingy
        # (20130317/straup)
        
        float_pat = re.compile(r'^-?\d+\.\d+(e-?\d+)?$')
        charfloat_pat = re.compile(r'^[\[,\,]-?\d+\.\d+(e-?\d+)?$')
        
        encoder = json.JSONEncoder(separators=(',', ':'), indent=indent, sort_keys=True)
        encoded = encoder.iterencode(data)

        for token in encoded:

            if charfloat_pat.match(token):
                # in python 2.7, we see a character followed by a float literal
                fh.write(token[0] + '%.6f' % float(token[1:]))
            
            elif float_pat.match(token):
                # in python 2.6, we see a simple float literal
                fh.write('%.6f' % float(token))
            
            else:
                fh.write(token)

    def encode_feature(self, feature, fh=sys.stdout):

        fh.write("{\n")

        keys = ('id', 'type', 'properties', 'bbox', 'geometry')

        for k in keys:

            fh.write(' ' * self.indent)
            fh.write('"%s": ' % k)

            if k in ('bbox', 'geometry'):
                self._encode(feature[k], fh, None)
            else:
                self._encode(feature[k], fh, self.indent * 2)

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
