'''
@author: nir
'''

from bottle import route, run, request

@route("/matrix/:input")
def multiplication_matrix(input= '7'):
    n = int(input)
    html = ""    
    for i in range(1,n):
        html += "<br>" 
        for j in range(1,n):
            html += "{} ".format(i*j)
    return html

@route("/")
def default_matrix():
    return multiplication_matrix (7)

run(host="localhost", port="8080")
