# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pem.pyc (Python 3.11)

import base64
(stSpam, stHam, stDump) = (0, 1, 2)

def readPemBlocksFromFile(fileObj, *markers):
    startMarkers = dict(map((lambda x: (x[1], x[0])), enumerate(map((lambda y: y[0]), markers))))
    stopMarkers = dict(map((lambda x: (x[1], x[0])), enumerate(map((lambda y: y[1]), markers))))
    idx = -1
    substrate = ''
    certLines = []
    state = stSpam
    certLine = fileObj.readline()
    return (idx, substrate)


def readPemFromFile(fileObj, startMarker, endMarker = ('-----BEGIN CERTIFICATE-----', '-----END CERTIFICATE-----')):
    (idx, substrate) = readPemBlocksFromFile(fileObj, (startMarker, endMarker))
    return substrate


def readBase64fromText(text):
    return base64.b64decode(text.encode())


def readBase64FromFile(fileObj):
    return readBase64fromText(fileObj.read())
