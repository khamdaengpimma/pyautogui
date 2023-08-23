
import pyautogui
from PIL import Image

# im1 = pyautogui.screenshot()
# im2 = pyautogui.screenshot("newone.png")
Image.open("photo.png").convert('L').save("photo_l.png")
