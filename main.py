import requests
from base64 import b64decode
from json import loads
import sys

if "__main__" == __name__:

	if len(sys.argv) > 1:

		urlScrapper = ('{}http://169.254.169.254/latest/').format(sys.argv[1])

		firstResponse =  requests.get(urlScrapper).text

		if '{"page":' in firstResponse:

			htmlMetadata =  b64decode(loads(firstResponse)['page']).decode('utf-8')

		else:

			htmlMetadata = firstResponse

		for a in htmlMetadata.split('\n'):
			print(a)