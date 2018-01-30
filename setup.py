'''
Created on 08 January 2018
@author: tom
'''

from setuptools import setup

setup(name="systeminfo",
      version="0.1",
      decription="Basic system information for COMP30670",
      url="",
      author="Thomas Anderson",
      author_email="thoma.anderson@ucdconnect.ie",
      license="gpl3",
      packages=['systeminfo'],
      entrypoints={
          'console_scripts':['comp30670_systeminfo=systeminfo.main:main']
          }
      )
      