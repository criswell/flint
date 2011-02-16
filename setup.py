#!/usr/bin/env python

from distutils.core import setup

scripts = ['flint']

packages = [ 'flintlib' ]

flintlib_templates = [ 'templates/stock.html' ]

package_data = { 'flintlib' : flintlib_templates }

setup(name='flint',
      version='0.0.1',
      description='Flint resume generation tool',
      author='Sam Hart',
      author_email='hartsn@gmail.com',
      url='https://bitbucket.org/criswell/flint',
      license='GNU AGPLv3+',
      scripts=scripts,
      packages=packages,
      package_data=package_data,
     )
