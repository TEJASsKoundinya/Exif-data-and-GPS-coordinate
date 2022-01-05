'''
USer can know location and metadata only if the image is stored and sent by the
original source and copy of it can only be analysied

'''

import exifread 
from GPSPhoto import gpsphoto
from PIL import Image
from PIL.ExifTags import TAGS

imagename = "IMG_20200128_072255.jpg"
image = Image.open(imagename)
exifdata = image.getexif()
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    print(f"{tag:25} : {data}")

print('-----------------*--------------------')
#Latitude and Longitude on GOOGLE MAPS
# Get the data from image file and return a dictionary
datax = gpsphoto.getGPSData('IMG_20200128_072255.jpg')
print('Latitude:> ',datax['Latitude'])
print('Longitude:> ',datax['Longitude'])
LOC = 'https://www.google.com/maps/@'
LOC = LOC+str(datax['Latitude'])
LOC = LOC+','
LOC = LOC+str(datax['Longitude'])
LOC = LOC+',15z'
print(LOC)