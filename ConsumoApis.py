import requests

url='https://www.youtube.com/'
respuesta=requests.get(url)
print(respuesta)

if respuesta.status_code==200:
	print(respuesta.content)
	contenido=respuesta.content
	archivo=open('jose.html','wb')
	archivo.write(contenido)
	archivo.close()
