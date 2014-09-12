from setuptools import setup, find_packages
import os

version = '0.1.2'

setup(name='plonetheme.intkModern',
    version=version,
    description="An installable Diazo theme for Plone 4",
    long_description=open("README.txt").read(),
    classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
    ],
    keywords='',
    author='Andre Goncalves',
    author_email='andre@intk.com',
    url='https://github.com/intk/plonetheme.intkModern',
    download_url='https://github.com/intk/plonetheme.intkModern/tarball/0.1.1',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plonetheme'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'setuptools',
	'plone.app.theming',
    ],
    extras_require={
        "test": ["plone.app.testing"]
    },
    entry_points={
        "z3c.autoinclude.plugin": "target = plone",
    }
)
