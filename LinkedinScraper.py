import requests
from lxml import html
from bs4 import BeautifulSoup

username = "sample_username"
password = "sample_password"

session_requests = requests.session()
login_url = "https://www.linkedin.com/uas/login"
result = session_requests.get(login_url)
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='loginCsrfParam']/@value")))[0]

payload = {
	"session_key": username, 
	"session_password": password, 
	"loginCsrfParam": authenticity_token
}

result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
)

url = 'https://www.linkedin.com/mynetwork/'
result = session_requests.get(
	url, 
	headers = dict(referer = url)
)

soup = BeautifulSoup(result.content, 'lxml')
print(soup.title)
for link in soup.find_all('img'):
    print(link.get('src'))
