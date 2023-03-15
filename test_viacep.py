import requests as r

print('testando api do viacep')
res = r.get('https://viacep.com.br/ws/13207500/json/')

print(res.json())