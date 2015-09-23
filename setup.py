#!/usr/bin/env python

from setuptools import setup, find_packages

packages = find_packages()
desc = open("README.md").read(),

setup(
    name='mapzen.whosonfirst.geojson',
    namespace_packages=['mapzen', 'mapzen.whosonfirst', 'mapzen.whosonfirst.geojson'],
    version='0.02',
    description='Python tools for doing GeoJSON related things with Who\'s On First data',
    author='Mapzen',
    url='https://github.com/mapzen/py-mapzen-whosonfirst-geojson',
    install_requires=[
        ],
    dependency_links=[
        ],
    packages=packages,
    scripts=[
        'scripts/wof-encode',
        ],
    download_url='https://github.com/mapzen/py-mapzen-whosonfirst-geojson/releases/tag/v0.02',
    license='BSD')
