import os
# import the library opencv
import cv2
# globbing utility.
import glob
# select the path
path = "IMG/*.*"
ruta = 'IMG/'
carpeta = input("INGRESA UN NOMBRE PARA LA CARPETA DE SALIDA")

def crearFolder():
    query = ruta+carpeta
    print(query)
   # isExist = os.path.exists(ruta+'/colocolo')
    if not query:
        # Create a new directory because it does not exist 
        rutanueva = query
        carpetacreada = os.makedirs(rutanueva)
        print(rutanueva, "ESTA DEBERIA SER UNA RUTA")
        print("TAMOS LISTOCO CON LA NUEVA CARPET ",carpetacreada)
        return rutanueva
    else :
        print(query, "ESTA CARPETA YA EXISTE")
        return query
        
        

for bb,file in enumerate (glob.glob(path)):
  image_read = cv2.imread(file)
  # conversion numpy array into rgb image to show 
  c = cv2.cvtColor(image_read, cv2.COLOR_BGR2GRAY)
  # writing the images in a folder output_images
  query = crearFolder()
  cv2.imwrite(query+'MONOCHROME{}.png'.format(bb), c)
  cv2.imshow('PLOMO', c)
  # wait for 1 second
  k = cv2.waitKey(1000)
  # destroy the window
  cv2.destroyAllWindows()
  
  
  




