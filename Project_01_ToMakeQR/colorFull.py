import qrcode
from PIL import Image
qr=qrcode.QRCode(version=1, box_size=10,border=4,)
qr.add_data("https://www.instagram.com/priyanshutripathi708/")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="pink")
img.save("Insta.png")