import pyqrcode
#import png
from pyqrcode import QRCode

a="hello WORLD"

url=pyqrcode.create(a)

url.svg("myqr.svg",scale=8)
#create and save the
#url.png("myqr.png",scale=6)