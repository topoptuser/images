import sys, time, requests

# defines the quantity of requests
if len(sys.argv)>1:
   requests_quantity = int(sys.argv[1]);
else:
   requests_quantity = 5;

# get the images and saves it
for i in range(requests_quantity):
   image_name =time.strftime("%Y%m%d%H%M%S", time.gmtime())+'.bmp';
   s = requests.session()
   r2 = s.request(
      'GET',
      'http://10.10.180.1/vld.bmp' );
   with open( image_name, 'wb' ) as f:
      f.write(r2.content);
   time.sleep(1);
