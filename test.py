import requests

respone = requests.get('https://www.w3schools.com/python/demopage.js')

print(respone.json())