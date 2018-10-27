import os
beibe = "GET / HTTP/1.1"
temp = beibe.split("GET / ")
str_temp = temp[1].split("HTTP/1.1")[0]
#print("Str_temp:",(str_temp))
if not(os.path.exists(str_temp)) and str_temp != '':
	f = open("codigo404.html", "r")
	page = f.read()
	http_response = """\HTTP/1.1 404 Not Found\r\n\r\n""" + page + "\r\n"
	f.close()
elif "GET / " not in beibe:
        f = open("badRequest.html", "r")
        page = f.read()
        http_response = """\HTTP/1.1 400 Bad Request\r\n\r\n""" + page + "\r\n"
        f.close()
elif(str_temp==''):
    f = open("index.html", "r")
    page = '<html><head></head><body><h1>Olá mundo!</h1>O meu servidor funciona!</body></html>'
    http_response = """\HTTP/1.1 200 OK\r\n\r\n""" + page
    f.close()
else:
    f = open(str_temp, "r")
    page = f.read()
    http_response = """\HTTP/1.1 200 OK\r\n\r\n""" + page
    f.close()	
print(http_response)
