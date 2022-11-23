#!/usr/bin/python3
"""A Python script that fetches https://alu-intranet.hbtn.io/status and uses a urlib package"""
import urllib.request


if __name__ == "__main_":
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
         html = response.read()
         print('Body response:')
         print('\t- type: {}'.format(type(html)))
         print('\t- content: {}'.format(html))
         print('\t- utf8 content: {}'.format(html.decode('utf-8')))