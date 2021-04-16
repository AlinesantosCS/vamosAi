from requests import get

# from requests import post
google = get("http://google.com")
# print(f"Google: {google}") 
print(google.status_codes())
# print(f"Status: {google}") # 200

# cabecalho =google.headers
# print(f"HEADERS: {cabecalho}") #Cabeçalho da resposta
# info = google.cookies
# print(f"COOKIES: {info}") # Cookies de requisição
# texto = google.text
# print(f"Texto: {texto}") 

# google = post("http://google.com")
# print(f"Google: {google}") # 405

# razao= google.reason
# print(f"Razão: {razao}") # Método não permitido

# encodando= google.encoding
# print(f"Encoding: {encodando}") # UTF-8

# fechar= google.close
# print(f"Fechar: {fechar}") # Encerra a comunicação
