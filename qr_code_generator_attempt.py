#insert text
#insert file name
#
import qrcode
user_input = input("Insert the text URL here: ")
img = qrcode.make(user_input)
type(img)  # qrcode.image.pil.PilImage
user_file = input("Enter the filename: ")
img.save(user_file)
print("QR code saved as ", user_file)
