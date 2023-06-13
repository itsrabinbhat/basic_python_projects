import qrcode
def qr_gen(data):
    img = qrcode.make(data)
    img.save('/qrcodes/img.png')

data = input("Enter Your data here: ")
qr_gen(data)
