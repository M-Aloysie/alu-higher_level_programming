#!/usr/bin/python3
"""A Python script that:
fetches https://alu-intranet.hbtn.io/status and uses a urlib package.
"""


if __name__ == "__main_":
    import urllib.request

    with urllib.request.urlopen('https://intranet.hbtn.io/status') as res:
        html = res.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode('utf-8')))
