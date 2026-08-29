import qrcode
data=input("Enter text or link to be encoded in QR code: ")
img=qrcode.make(data)
img.save("img.png")
img.show()
print("QR code generated and saved as img.png")