import PIL
from PIL import Image
im = Image.open ("dog.jpg")
im.show()
pix = im.load()
print (im.size)



darkBlue = (0, 51, 76)
red = (217, 26, 33)
lightBlue = (112, 150, 158)
yellow = (252, 227, 166)
new_image=[]
#for j in range (1200):
    #for i in range (630):
        #print (pix [i,j])
#x=1200
#y=630
#width=1200
#height=630
#for x in width:
    #for y in height:
        #current_color = im.getpixel((x, y))
        #new_color= (0, 51, 76)
        #im.putpixel((x,y), new_color)

for i in range(1200):
    for j in range(630):   
        r=(pix[i, j][0])
        g=(pix[i, j][1])
        b=(pix[i, j][2])
        total=(r+b+g)
        
        if total<182:
            new_image.append((0, 51, 76))
        if total<364 or total>182:
            new_image.append((217, 26, 33))
            
        if total<546 or total>364:
            new_image.append((112, 150, 158))
        if total>546:
            new_image.append((252, 227, 127))
         

im.putdata(new_image)
im.show()
