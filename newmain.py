import socket
from newviews import index, page


URLS = {
    '/': index,
    '/page': page 
}


def generatorResponse(request):
    method, url = parsRequest(request)
    headers, code = generateHeaders(method, url)
    body = generatorContent(code, url)
    return (headers + body).encode()



def parsRequest(request):
    """ Функция которая парсит запрос клиента"""
    pars = request.split(' ')
    method = pars[0]
    url = pars[1]
    return (method, url)


def generateHeaders(method, url):
    if not method == "GET":
        return('HTTP/1.1 405 Method not allowed\n\n', 405)
    elif url not in URLS:
        return('HTTP/1.1 404 Not Found\n\n', 404)
    else:
        return('HTTP/1.1 200 OK\n\n', 200)


def generatorContent(code, url):
    if code == 405:
        return '<h1>405</h1><p>Method not allowed</p>'
    elif code == 404:
        return '<h1>404</h1><p>Not found</p>'
    else:
        return URLS[url]()
    


def run():
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    serverSocket.bind(('localhost', 8000))
    serverSocket.listen()

    while True:
        clientSocket, addr = serverSocket.accept()
        request = clientSocket.recv(1024)
        
        response = generatorResponse(request.decode('utf-8'))

        clientSocket.sendall(response)
    
        clientSocket.close()



if __name__ == '__main__':
    run()