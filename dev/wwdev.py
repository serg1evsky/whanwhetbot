import primitives
import requests


SITE_URL = 'http://localhost:8000'
def send_data():
	files = {'settings.py': open('settings.py','rb')}
	r = requests.post(SITE_URL, files=files)
	
if __name__ == '__main__':
	send_data()
