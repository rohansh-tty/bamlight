from PIL import Image
import os
from functools import wraps
from time import perf_counter, localtime
from datetime import datetime, timezone
import argparse
from collections import defaultdict

def valid_path(path):
	if not os.path.isdir(path) or not isinstance(path, str):
		raise ValueError

CROP_PATH = r'.\cropped_images'
RESIZE_PATH = r'.\resize'
JPG_PATH, PNG_PATH = r'.\jpg_images', r'.\png_images'
IMAGE_DIRECTORY = r'.\images' 



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
	def inner(*args):
		nonlocal count
		nonlocal total_time

		func_time = datetime.now(timezone.utc)
		func_id = hex(id(fn.__name__))

		start_time = perf_counter()
		result = fn(*args)
		elapsed_time = perf_counter()-start_time

		func_reg[inner.__name__] = count
		count = count + 1
		total_time = total_time + elapsed_time

		print(f'Function named {fn.__name__} with ID of {func_id} was executed at {func_time}\n Current Execution Time: {elapsed_time} seconds \n Total Execution Time: {total_time} seconds')
		return result
	return inner


@func_log
def j2p(folder_path:str, dest_folder:str):
	valid_path(folder_path)
	total_files = len(os.listdir(str(folder_path)))
	count = 0
	new_ext = 'png'
	dest_path = dest_folder

	if not os.path.isdir(dest_folder):
		os.mkdir(dest_folder)
	
	for img in os.listdir(folder_path):
		img_name = img.split('.')
		img_ext = img.split('.')[-1]
		if not img_ext == new_ext:
			img = Image.open(os.path.join(folder_path, img))
			new=img.convert('RGB')

			print(f'IMAGE {img_name} CONVERTED TO {new_ext}')
			print(dest_path+'\\'+str(img_name[0]+'.'+str(new_ext)))
			
			new.save(os.path.join(dest_path, str(img_name[0]+'.'+str(new_ext))))
			count += 1

	if count == total_files:
		print(f'<<<CONVERTED {total_files} FILES TO {new_ext}>>>')
	else:
		print(f'<<<CONVERTED {total_files-count} FILES TO {new_ext}>>>')
	print('-'*60)
	

@func_log
def p2j(folder_path:str, dest_folder:str):
	valid_path(folder_path)
	total_files = len(os.listdir(str(folder_path)))
	count = 0
	new_ext = 'jpg'
	dest_path = dest_folder
	
	if not os.path.isdir(dest_folder):
		os.mkdir(dest_folder)
	
	for img in os.listdir(folder_path):
		img_name = img.split('.')
		img_ext = img.split('.')[-1]
		if not img_ext == new_ext:
			img = Image.open(os.path.join(folder_path, img))
			new=img.convert('RGB')
			
			print(f'IMAGE {img_name} CONVERTED TO {new_ext}')
			print(dest_path+'\\'+str(img_name[0]+'.'+str(new_ext)))

			new.save(os.path.join(dest_path, str(img_name[0]+'.'+str(new_ext))))
			count += 1

	if count == total_files:
		print(f'<<<CONVERTED {total_files} FILES TO {new_ext}>>>')
	else:
		print(f'<<<CONVERTED {total_files-count} FILES TO {new_ext}>>>')
	print('-'*60)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='An easy way to convert png to jpg and vice-versa.')
	parser.add_argument('--type', type=str, help='path to image directory') # this is to understand the type of conversion whether its (png to jpg) or (jpg to png)
	parser.add_argument('--convert', type=str, nargs='+', help='path to jpg image directory and final output directory') # this is bulk conversion from (jpg/jpeg to png) or (png to jpg)
	args = parser.parse_args()
	type_ = args.type
	source_folder, dest_folder = [i for i in args.convert][0], [i for i in args.convert][1]

	print(f'\n[SOURCE FOLDER]: {source_folder}\n')
	print(f'[DESTINATION FOLDER]: {dest_folder}\n')

	if type_ == 'j2p':
		j2p(source_folder, dest_folder)
	elif type == 'p2j':
		p2j(source_folder, dest_folder)

