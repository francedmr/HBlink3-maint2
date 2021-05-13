

BRIDGES = {
'HBLink-EchoTest-TG999': [
            {'SYSTEM': 'ECHOTEST',            'TS': 2, 'TGID': 999,     'ACTIVE': True,  'TIMEOUT': 0,  'TO_TYPE':'NONE', 'ON': [],         'OFF': [],      'RESET': []},
            {'SYSTEM': 'MASTER-1',            'TS': 2, 'TGID': 999,     'ACTIVE': True,  'TIMEOUT': 0,  'TO_TYPE':'NONE', 'ON': [],         'OFF': [],      'RESET': []},
        ]
}

if __name__ == '__main__':
    from pprint import pprint
    pprint(BRIDGES)
