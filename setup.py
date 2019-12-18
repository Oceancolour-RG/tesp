#!/usr/bin/env python

from setuptools import setup, find_packages

setup(name='tesp',
      version='0.0.4',
      description=('A temporary solution to get packaging underway. '
                   'Code will eventually be ported eo-datasets.'),
      packages=find_packages(),
      install_requires=[
          'click',
          'click_datetime',
          'folium',
          'geopandas',
          'h5py',
          'luigi',
          'numpy',
          'pathlib',
          'pyyaml',
          'rasterio',
          'scikit-image',
          'shapely',
          'structlog',
          'eodatasets',
          'checksumdir',
          'eugl',
      ],
      dependency_links=[
          'git+https://github.com/GeoscienceAustralia/eo-datasets@develop#egg=eodatasets-0.10',
          'git+https://github.com/OpenDataCubePipelines/eugl.git#egg=0.0.3+s2beta'
      ],
      scripts=['bin/s2package', 'bin/ard_pbs', 'bin/search_s2'],
      include_package_data=True)
