#!/usr/bin/env python

import setuptools
from distutils.core import setup, Extension

setup(name='rdpy',
	version='1.3.2',
	description='Remote Desktop Protocol in Python',
	long_description="""
	RDPY is a pure Python implementation of the Microsoft RDP (Remote Desktop Protocol) protocol (Client and Server side). RDPY is built over the event driven network engine Twisted.
	
	RDPY provide RDP and VNC binaries : RDP Man In The Middle proxy which record session, RDP Honeypot, RDP screenshoter, RDP client, VNC client, VNC screenshoter, RSS Player
	""",
	author='Sylvain Peyrefitte',
	author_email='citronneur@gmail.com',
	url='https://github.com/citronneur/rdpy',
	packages=[
			'rdpy',
			'rdpy.core',
			'rdpy.security',
			'rdpy.protocol',
			'rdpy.protocol.rdp',
			'rdpy.protocol.rdp.pdu',
			'rdpy.protocol.rdp.nla',
			'rdpy.protocol.rdp.t125',
			'rdpy.protocol.rfb'
		],
	ext_modules=[Extension('rle', ['ext/rle.c'])],
	install_requires=[
			'twisted',
          	'pyopenssl',
          	'service_identity',
          	'rsa',
          	'pyasn1',
	  	],
)
