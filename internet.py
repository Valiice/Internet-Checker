import urllib.request
import threading

def connect(host='http://google.com'):
    try:
        urllib.request.urlopen(host)
        return True
    except:
        return False

def timer5SecondsPrint():
  threading.Timer(5.0, timer5SecondsPrint).start()
  print( "connected" if connect() else "no internet!" )

timer5SecondsPrint()