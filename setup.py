#!/usr/bin/env python
# from distutils.core import setup
from setuptools import setup, find_packages, Extension

setup(  name='py_sandbox',
        version='0.1',
        description='Common Python Functions & Fun Stuff!',
        author='Robert Cofield',
        author_email='robertgcofield@gmail.com',

        packages=[  'rgc_decorators',
                    'rgc_operators',
                    'rgc_types',
                    'rgc_utils'
        ],

        # py_modules=['rgc_decorators',
                    # 'rgc_operators'],
        
        ext_modules=[
            Extension(  'rgc_boost_python.libyay',
                        ['rgc_boost_python/yay.cxx'],
                        libraries=['boost_python']
            )
        ]
)