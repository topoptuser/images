from PIL import Image
import sys, time

def crop(file_name):
   img = Image.open(file_name, 'r');
   if img.size!=(36,9):
      return;
   for i in range(4):
      x1,y1 = 9*(i  ),0;
      x2,y2 = 9*(i+1),9;
      img.crop((x1,y1,x2,y2)).save(file_name[:len(file_name)-4]+'-'+str(i)+'.bmp','bmp');

if __name__ == "__main__":
   if len(sys.argv)>1:
      crop(sys.argv[1]);