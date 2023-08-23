from PIL import Image
Image.open("photo.png").convert('L').save("photo_l.png")
