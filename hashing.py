from PIL import Image
from scipy.misc import toimage
import hashlib
blank = []
f = open("/Users/Nikhil/Desktop/crypto-art/output.txt", "r", encoding = 'utf-8')
blank.append(f.read())
f.close()
hash_object = hashlib.sha256(str(blank).encode('utf-8')).hexdigest()
s = str(hash_object) #storing the hash as a string. Hashed using SHA256.
#print(s)
data = []
for item in s:
    data.append(item)
#print(data)
#print(len(data))
chdata=[]
for i in data:
    chdata.append(ord(i))
#Using the ordinate of each character in the hash string to convert to a number.
#Can be reversed using str("number")
#print(chdata)
frame = []

for x in range(8):
    frame.append(["O"] * 8)

#An empty 8x8 frame. To be filled with the ord values.

def print_frame(frame):
    for row in frame:
        print(" ".join(row))

#print_frame(frame)

temp = 0

for i in range(8):
    for j in range(8):
        frame[i][j] = chdata[temp+j]
    temp = temp + 8
#print(frame)
#Frame is now populated with ord values.
toimage(frame).show() #Converts the frame to a bitmap image. Only black, white and grey.

#Add colours to the image.


"""data1 = [
    [1,0,0,1,0],
    [1,1,1,0,0],
    [1,1,0,1,0],
    [1,0,1,1,0],
    [0,1,1,0,1],
    ]


img = Image.new("1", (8, 8))
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixels[i, j] = data1[i][j]

img.show()
#img.save("img.png")"""
