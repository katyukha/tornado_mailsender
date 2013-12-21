# -*- coding: utf-8 -*-
#
# Author: Dmytro Katyukha <firemage.dima@gmail.com>
# Created: 21/12/2013
#
"""
   This is a simple web server with aming only to send emails.
   Server side configuration is done via command line arguments passed to a server.

   After install to see all available options just call:

      $ tornado_mailsender_server --help

   To send mail via this server just make post request to URL /send_mail/
   To get information on what data shoud be supplied to POST request, just do
   GET request to that address.
"""
from setuptools import setup


setup(
    name="tornado_mailsender",
    version="0.0.2",
    author="Dmytro Katyukha",
    author_email="firemage.dima@gmail.com",
    description="Simple web server to send mails by post request on specified URL",
    long_description=__doc__,
    classifiers=[
        'Programming Language :: Python',
    ],
    license="BSD",
    keywords="tornado tornadoweb email mail send_mail",
    #url="https://github.com/troolee/tornado-routes",
    install_requires=['tornado', 'futures'],
    packages=['tornado_mailsender'],
    entry_points=dict(console_scripts=['tornado_mailsender_server=tornado_mailsender.server:main']),
)
