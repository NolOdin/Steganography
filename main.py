# from stegano import exifHeader
#
# secret = exifHeader.hide("img/usa.jpg", "img/usa_secret.png", "Секретное слово :)")
# result = exifHeader.reveal("img/usa_secret.png")
# result = result.decode()
# print(result)


from steganocryptopy.steganography import Steganography

Steganography.generate_key("")
secret = Steganography.encrypt("key.key", "img/Dope.png", "message/secret_message.txt")
secret.save("img/Dope_secret.png")

result = Steganography.decrypt("key.key", "img/Dope_secret.png")
print(result)