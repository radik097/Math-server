from flask import *
import requests
import math
f = Flask(__name__)
@f.route('/', methods=['GET'])
def index():
	return """<!DOCTYPE html><html><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="X-UA-Compatible" content="IE=edge"><title>MATH</title><meta name="description" content=""><meta name="viewport" content="width=device-width, initial-scale=1"></head><body style="width: 720; height: 1344;"><center><div><form  method="POST" action="/main">Значеие Y: <input type="text" name="Y"><p id="ry"></p><br>Значеие K: <input type="text" name="K"><p id="rk"></p><br>Значеие X: <input type="text" name="X"><p id="rx"></p><br>Степень: <input  type="text" name="P"><p id="rpow"></p><br>Значеие B: <input type="text" name="B"><p id="rb"></p><br><br><br><input type="submit" value="Решить"></form><a href="javascript:;" onclick='window.open("https://2ip.ua/ru/myspeed","speedo","width=875"+",height=615,left="+(screen.width - 875)/2+",top="+(screen.height - 615)/2+",scrollbars=yes,resizable=yes" );' title="Тест скорости Интернет соединения"><img src="https://2ip.ua/images/speedometr/7.png" style="width:200px;"></a></div></center></body></html>"""
@f.route('/main', methods=['POST'])
def value():
    y = int(request.values['Y'].upper())
    k = int(request.values['K'].upper()) 
    x = int(request.values['X'].upper())
    b = int(request.values['B'].upper())
    p = int(request.values['P'].upper())
    K =  str((y - b) / p)
    Y =  str(k*p + b)
    X =  str(math.sqrt(p))
    B =  str(y - k*p)
    return "<h1>K: </h1>" + K + "<h1> Y: </h1><br>" + Y + "<h1> X: </h1><br>" + X + "<h1> B: </h1><br>" + B
if __name__ == '__main__':
	f.run(port=80)
