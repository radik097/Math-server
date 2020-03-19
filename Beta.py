from flask import *
from sympy import *
import requests
import math
f = Flask(__name__)
@f.route('/', methods=['GET'])
def index():
	return """<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><title>MATH</title><meta name="description" content=""><meta name="viewport" content="width=device-width, initial-scale=1"></head><body style="width: 720; height: 1344;"><center><div><form  method="POST" action="/main">Пример: <input type="text" name="K"><p id="rk"></p><br>Значеие X: <input type="text" name="X"><p id="rx"></p><br><br><br><input type="submit" value="Решить"></form></a></div></center></body></html>"""
@f.route('/main', methods=['POST'])
def value():
    value = int(request.values['K'].upper())
    x = int(request.values['X'].upper())
    x = symbols('x')
    k = int(value)
    K = str(diff(k))
    return "<H1>Gooood</H1>" + K
if __name__ == '__main__':
	f.run(port=80)
