'''
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

im = Image.open("temp.jpg") # the second one
im = im.filter(ImageFilter.MedianFilter())
enhancer = ImageEnhance.Contrast(im)
im = enhancer.enhance(2)
im = im.convert('1')
im.save('temp2.jpg')
text = pytesseract.image_to_string(Image.open('temp2.jpg'))
print(text)


from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
path = 'temp2.jpg'
img = Image.open(path)
img = img.convert('JPEG')
pix = img.load()
for y in range(img.size[1]):
    for x in range(img.size[0]):
        if pix[x, y][0] < 102 or pix[x, y][1] < 102 or pix[x, y][2] < 102:
            pix[x, y] = (0, 0, 0, 255)
        else:
            pix[x, y] = (255, 255, 255, 255)
img.save('temp3.jpg')
text = pytesseract.image_to_string(Image.open('temp3.jpg'))
# os.remove('temp.jpg')
print(text)
'''

try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

#pytesseract.pytesseract.tesseract_cmd = '<full_path_to_your_tesseract_executable>'
# Include the above line, if you don't have tesseract executable in your PATH
# Example tesseract_cmd: 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'

#print(pytesseract.image_to_string(Image.open('temp.jpg')))
print(pytesseract.image_to_string(Image.open('temp.JPG'), lang='fra'))