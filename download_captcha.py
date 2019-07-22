import base64
from selenium import webdriver
import os

driver = webdriver.Chrome(executable_path='/home/phamhung/Downloads/handle-image/chromedriver')
driver.set_script_timeout(10)
driver.get("https://dk-sis.hust.edu.vn/Users/Login.aspx")

for i in range(100,1000000):
	# find the captcha element
	ele_captcha = driver.find_element_by_xpath("//*[@id='ccCaptcha_IMG']")

	try:
		# get the captcha as a base64 string
		img_captcha_base64 = driver.execute_async_script("""
			var ele = arguments[0], callback = arguments[1];
			ele.addEventListener('load', function fn(){
			ele.removeEventListener('load', fn, false);
			var cnv = document.createElement('canvas');
			cnv.width = this.width; cnv.height = this.height;
			cnv.getContext('2d').drawImage(this, 0, 0);
			callback(cnv.toDataURL('image/png').substring(22));
			}, false);
			ele.dispatchEvent(new Event('load'));
			""", ele_captcha)
		path = '/home/phamhung/Downloads/handle-image/images/'+str(i)+'.png'
		# save the captcha to a file
		with open(path, 'wb') as f:
			f.write(base64.b64decode(img_captcha_base64))
			print(path)
		driver.refresh()
	except Exception as e:
		print(e)
		driver.refresh()