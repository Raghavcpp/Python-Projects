import pyqrcode

url = input("Enter a URL to generate QR Code : \n")

QR = pyqrcode.create(url)
QR.png("webqr.png", scale = 8)