import sys
import os
from PIL import Image
#Get arguments from user
ImageFolder=sys.argv[1] # Image is stored here
OutputFolder=sys.argv[2] # Image should be converted and stored in this folder
#Check if folder already exists
if not os.path.exists(OutputFolder):
    os.makedirs(OutputFolder) # Make Folder
#loop over all images present
for image in os.listdir(ImageFolder):
    img= Image.open(f'{ImageFolder}{image}')
    # Without indexing splitext gives a tuple of ('filename,'mode')
    nameofpic=os.path.splitext(image)[0] 
    img.save(f'{OutputFolder}{nameofpic}.gif','gif')
    print("done")