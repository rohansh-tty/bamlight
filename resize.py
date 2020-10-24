from PIL import Image
import os
import argparse
from functools import wraps
from time import perf_counter, localtime
from datetime import datetime, timezone
from collections import defaultdict



CROP_PATH = r'C:\Users\Rohan Shetty\Desktop\session11-Gilf641\cropped_images'
RESIZE_PATH = r'C:\Users\Rohan Shetty\Desktop\session11-Gilf641\resize'
JPG_PATH, PNG_PATH = r'C:\Users\Rohan Shetty\Desktop\session11-Gilf641\jpg_images', r'C:\Users\Rohan Shetty\Desktop\session11-Gilf641\png_images'
IMAGE_DIRECTORY = r'C:\Users\Rohan Shetty\Desktop\session11-Gilf641\images' 


# validation tests
def valid_path(path):
	if not os.path.isdir(path) or not isinstance(path, str):
		raise ValueError

def valid_w_h(w=0,h=0):
	if w < 0 or h < 0:
		raise ValueError

def valid_pct(pct):
	if pct:
		if float(pct) < 0 or float(pct) > 1:
			raise ValueError

func_reg = defaultdict(lambda : 0)

def func_log(fn):
	'''
	Decorator which holds on log details whenever input function is executed.
	Args:
		fn: A User-Defined Function
	Returns a inner function(callable)
	'''
	
	count, total_time = 0, 0

	@wraps(fn)
	def inner(*args, **kwargs):
		nonlocal count
		nonlocal total_time

		func_time = datetime.now(timezone.utc)
		func_id = hex(id(fn.__name__))

		start_time = perf_counter()
		result = fn(*args, **kwargs)
		elapsed_time = perf_counter()-start_time

		func_reg[inner.__name__] = count
		count = count + 1
		total_time = total_time + elapsed_time

		print(f'Function named {fn.__name__} with ID of {func_id} was executed at {func_time}\n Current Execution Time: {elapsed_time} seconds \n Total Execution Time: {total_time} seconds')
		return result
	return inner

@func_log
def res_p(folder_path:str, dest_path:str, pct:float):
	'''
	Resizes bulk of images as per input passed in
	Args:
		folder_path: source folder containing images
		dest_path: destination path where the resized images are saved
		pct: proportion of image to be resized
	'''
	valid_path(folder_path)
	valid_path(dest_path)
	valid_pct(pct)

	total_files = len(os.listdir(str(folder_path)))
	count = 0

	for img in os.listdir(folder_path):
		img_name=img
		name=img.split('.')
		img = Image.open(os.path.join(folder_path, img))
		w, h = img.size	
		pct_val = float(pct)
		new_w, new_h = int(w*pct_val), int(h*pct_val)
		resized = img.resize((new_w, new_h), Image.BILINEAR)

		print(f'IMAGE {name} RESIZED TO {new_w}x{new_h}')
		print(dest_path+'\\'+str(img_name))
		resized.save(os.path.join(dest_path, img_name))
		count += 1

	if count == total_files:
		print(f'<<<RESIZED {total_files} FILES. SAVED TO {dest_path}>>>')
	else:
		print(f'<<<RESIZED {total_files-count} FILES. SAVED TO {dest_path}>>>')
	print('-'*60)



def res_w(folder_path:str, dest_path, width=500):
	'''
	Resizes bulk of images as per input passed in
	Args:
		folder_path: source folder containing images
		dest_path: destination path where the resized images are saved
		width, height: final width and height of image
	'''
	valid_path(folder_path)
	valid_path(dest_path)
	valid_w_h(width)
	
	total_files = len(os.listdir(str(folder_path)))
	count = 0

	for img in os.listdir(folder_path):
		img_name=img
		name=img.split('.')
		img = Image.open(os.path.join(folder_path, img))
		w, h = img.size
		new_w, new_h = (int(width), int(h))
		resized = img.resize((new_w, new_h), Image.BILINEAR)

		print(f'IMAGE {name} RESIZED TO {new_w}x{new_h}')
		print(dest_path+'\\'+str(img_name))
		resized.save(os.path.join(dest_path, img_name))
		count += 1

	if count == total_files:
		print(f'<<<RESIZED {total_files} FILES. SAVED TO {dest_path}>>>')
	else:
		print(f'<<<RESIZED {total_files-count} FILES. SAVED TO {dest_path}>>>')
	print('-'*60)



def res_h(folder_path:str, dest_path, height=500):
	'''
	Resizes bulk of images as per input passed in
	Args:
		folder_path: source folder containing images
		dest_path: destination path where the resized images are saved
		width, height: final width and height of image
	'''
	valid_path(folder_path)
	valid_path(dest_path)
	valid_w_h(height)
	
	total_files = len(os.listdir(str(folder_path)))
	count = 0

	for img in os.listdir(folder_path):
		img_name=img
		name=img.split('.')
		img = Image.open(os.path.join(folder_path, img))
		w, h = img.size
		new_w, new_h = (int(w), int(height))
		resized = img.resize((new_w, new_h), Image.BILINEAR)

		print(f'IMAGE {name} RESIZED TO {new_w}x{new_h}')
		print(dest_path+'\\'+str(img_name))
		resized.save(os.path.join(dest_path, img_name))
		count += 1

	if count == total_files:
		print(f'<<<RESIZED {total_files} FILES SAVED TO {dest_path}>>>')
	else:
		print(f'<<<RESIZED {total_files-count} FILES SAVED TO {dest_path}>>>')
	print('-'*60)




if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Function to resize images by half in bulk')
	parser.add_argument('--type', type=str, help='type of resize directory')
	parser.add_argument('--value',  help='proportion/percent of image to be resized')
	parser.add_argument('--resize', type=str, nargs='+', help='path to jpg image directory and final output directory')
	

	args = parser.parse_args()
	type_ = args.type
	val = args.value
	source_folder, dest_folder = [i for i in args.resize][0], [i for i in args.resize][1]

	print(f'\n[SOURCE FOLDER]: {source_folder}\n')
	print(f'[DESTINATION FOLDER]: {dest_folder}\n')

	# type = ['prop', 'prop_w', 'prop_h']
	if type_ == 'prop':
		res_p(source_folder, dest_folder, pct = val)
	elif type == 'prop_w':
		res_w(source_folder, dest_folder, width = val)
	elif type == 'prop_h':
		res_h(source_folder, dest_folder, height = val)

