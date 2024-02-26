import pyqrcode

url = input("QR kod oluşturucuya urlyi yazınız:  ")

QR_code = pyqrcode.create(url)
QR_code.svg('QR_kod.svg,scale=8')
