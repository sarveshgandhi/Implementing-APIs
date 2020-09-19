import requests

myToken = '20c15f0c6e30cf9947c1fd1c63b7ecfc51f03673'
myUrl = 'http://127.0.0.1:8000/generic/article/3'
head = {'Authorization': 'token {}'.format(myToken)}
# response = requests.get(myUrl, headers=head)
response = requests.get(myUrl, auth = ('Sarvesh', '123456'))
print(response.content)
