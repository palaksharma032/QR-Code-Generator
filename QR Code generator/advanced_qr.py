import qrcode
from PIL import Image

qr=qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

qr.add_data("https://github.com/palaksharma032")
qr.make(fit=True)
img=qr.make_image(fill_color="blue", back_color="beige")
img.save("Palak Sharma Github Profile.png")