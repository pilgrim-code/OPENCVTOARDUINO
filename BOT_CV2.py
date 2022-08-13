import os
# import the library opencv
import cv2
import shutil
# globbing utility.
import glob
# select the path
path = "IMG/*.*"
ruta = 'IMG'


def crearFolder():
    
    query = ruta+'/OUTPUT'
    print(query)
    isExist = os.path.exists(ruta+'/OUTPUT')
    if not isExist:
        # Create a new directory because it does not exist 
        rutanueva = query
        os.mkdir(query)
       # os.makedirs(rutanueva)
        print(rutanueva, "ESTA DEBERIA SER UNA RUTA")
        print("TAMOS LISTOCO CON LA NUEVA CARPET ",rutanueva)
        return rutanueva
    else :
        print(query, "ESTA CARPETA YA EXISTE")
        return query

def MoverArchivos():
    print(query, "ESTE MENSAJE PA VER LA RUTA")
    pattern = ruta + "\OUTPUTMONOCHROME*"
    for file in glob.iglob(pattern, recursive=True):
        # extract file name form file path
        file_name = os.path.basename(file)
        shutil.move(file, query)
        print('Moved:', file)
        
        
query = crearFolder()
for bb,file in enumerate (glob.glob(path)):
  image_read = cv2.imread(file)
  # conversion numpy array into rgb image to show 
  c = cv2.cvtColor(image_read, cv2.COLOR_BGR2BGRA)
 
  #cv2.imwrite(query+'MONOCHROME{}.png'.format(bb), c)
  cv2.imshow('PLOMO', c)
  # wait for 1 second
  k = cv2.waitKey(1000)
  # destroy the window
  cv2.destroyAllWindows()
  xy = (84,48)
  x = cv2.resize(c, xy, interpolation= cv2.INTER_LINEAR)
  cv2.imwrite(query+'MONOCHROME{}.bmp'.format(bb),x)
MoverArchivos()
  
  
  




