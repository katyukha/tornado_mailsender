# -*- coding: utf-8 -*-
#
# Author: Dmytro Katyukha <firemage.dima@gmail.com>
# Created: 21/12/2013
#

from setuptools import setup


setup(
    name="tornado-mailsender",
    version="0.0.1",
    author="Dmytro Katyukha",
    author_email="firemage.dima@gmail.com",
    description="Simple web server to send mails by post request on specified URL",
    classifiers=[
        'Programming Language :: Python',
    ],
#    license="BSD",
    keywords="tornado tornadoweb email mail send_mail",
    #url="https://github.com/troolee/tornado-routes",
    py_modules=['tornado_mailsender'],
    install_requires=['tornado', 'futures'],
)
