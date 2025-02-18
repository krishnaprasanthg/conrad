# -*- coding: utf-8 -*-

import os
from setuptools import find_packages


here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, 'conrad', '__version__.py'), 'r') as f:
    exec(f.read(), about)

with open('README.md', 'r', encoding="utf8") as f:
    readme = f.read()


requires = [
    "Click==7.0",
    "colorama==0.4.1",
    "requests==2.22.0",
    "SQLAlchemy==1.3.10",
    "jsonschema==3.1.1"
]
dev_requires = [
    "Sphinx==2.2.1"
]
dev_requires = dev_requires + requires


def setup_package():
    metadata = dict(name=about['__title__'],
                    version=about['__version__'],
                    description=about['__description__'],
                    long_description=readme,
                    long_description_content_type="text/markdown",
                    url=about['__url__'],
                    author=about['__author__'],
                    author_email=about['__author_email__'],
                    license=about['__license__'],
                    packages=find_packages(exclude=('tests',)),
                    install_requires=requires,
                    extras_require={
                        'dev': dev_requires,
                    },
                    entry_points={
                        'console_scripts': [
                            'conrad = conrad.cli:cli',
                        ],
                    },
                    classifiers=[
                        # Trove classifiers
                        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
                        'License :: OSI Approved :: Apache Software License',
                        'Programming Language :: Python :: 3.5',
                        'Programming Language :: Python :: 3.6',
                        'Programming Language :: Python :: 3.7'
                    ])

    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    setup(**metadata)


if __name__ == '__main__':
    setup_package()
