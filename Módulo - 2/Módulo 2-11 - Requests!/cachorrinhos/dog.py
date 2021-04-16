import requests
requisicao = requests.get('https://dog-facts-api.herokuapp.com/api/v1/resources/dogs/all')
print(requisicao.status_code,'\n\n')

print(requisicao.headers,'\n\n') #Cabeçalho da resposta

print(requisicao.encoding,'\n\n')# # UTF-8

print(requisicao.cookies,'\n\n')

print(requisicao.text,'\n\n')




