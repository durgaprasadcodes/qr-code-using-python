import qrcode
text = input('Enter Your Link or text meant to convert Qr Code : ')
img = qrcode.make(text)
file_name = input("Enter your file name to save Qr Code (without .png, Ex: myQr): ").strip()
img.save(f'{file_name}.png')
print('Image Saved to Your Gallery Successfully')
