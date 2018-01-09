import requests

s = requests.session()

hp_form ={
   'user_name' :hp_username,
   'password'  :hp_password,
   'vld_code'  :hp_vld_code,
};

r = s.request(
   'POST',
   'http://10.10.180.1/web/device/login',
   data = hp_form,
);
