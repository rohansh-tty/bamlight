from PIL import Image
import os
import argparse
from collections import defaultdict
from functools import wraps
from time import perf_counter, localtime
from datetime import datetime, timezone


CROP_PATH = r'.\cropped_images'
RESIZE_PATH = r'.\resize'
JPG_PATH, PNG_PATH = r'.\jpg_images', r'.\png_images'
IMAGE_DIRECTORY = r'.\images' 


invoke = False

# validation tests
def valid_path(path):
	if not os.path.isdir(path) or not isinstance(path, str):
		raise ValueError

def valid_pct(pct):
	if pct < 0 or pct > 1:
		raise ValueError

def valid_dim(dim):
	if isinstance(dim, tuple):
		for i in dim:
			if int(i)<0:
				raise ValueError
	else:
		for i in dim[0].split(','):
			if int(i)<0:
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
def crp_p(folder_path:str,  dest_path, pct):
	valid_path(folder_path)
	valid_path(dest_path)
	valid_pct(pct)

	total_files = len(os.listdir(folder_path))
	count = 0
	for img in os.listdir(folder_path):
		name=img
		img = Image.open(os.path.join(folder_path, img))
		w, h = img.size
		# new = Image.new('RGB', (w, h))
		new_w, new_h = w*(1-pct), h*(1-pct)
		sizes = []

		for i in range(0, max(w,h), 10):
			if i+max(new_w, new_h) < max(w,h):
				dim = (i, i, i+max(new_w, new_h),  i+max(new_w, new_h))
		try:
			new = img.crop(dim)
			new.save(os.path.join(dest_path, name))
		except:
			print(f'<<< Cannot crop the {name} due size mismatch. >>>')

		print(f'IMAGE {name} CROPPED BY {dim} ')
		
		count += 1
	if count == total_files:
		print(f'<<<CROPPED {total_files} FILES. SAVED TO {dest_path}>>>')
	else:
		print(f'<<<CROPPED {total_files-count} FILES. SAVED TO {dest_path}>>>')
	print('-'*60)


def crp_px(folder_path:str, dest_path, dim):
	valid_path(folder_path)
	valid_path(dest_path)
	valid_dim(dim)
	count = 0
	total_files = len(os.listdir(folder_path))
	for img in os.listdir(folder_path):
		name=img
		img = Image.open(os.path.join(folder_path, img))
		w, h = img.size
		# new = Image.new('RGB', (w, h))
		# if len(dim)==4:

		new = img.crop(dim)
		new.save(os.path.join(dest_path, name))
		try:
			new = img.crop(dim)
			new.save(os.path.join(dest_path, name))
		except:
			print(f'<<< Cannot crop the {name} due size mismatch. >>>')

		
		print(f'IMAGE {name} CROPPED BY {dim} ')
		
		count += 1
	if count == total_files:
		print(f'<<<CROPPED {total_files} FILES SAVED TO {dest_path}>>>')
	else:
		print(f'<<<CROPPED {total_files-count} FILES SAVED TO {dest_path}>>>')
	print('-'*60)


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Function to crop images by pixels/percentage in bulk')
	parser.add_argument('--type', type=str, help='path to image directory')
	parser.add_argument('--value', nargs='+', help='dim/pct of image pixels to be cropped')
	parser.add_argument('--crop', type=str, nargs='+', help='path to image directory and final output directory')


	# type = ['percent', 'px']
	
	args = parser.parse_args()
	type_ = args.type
	val = args.value
	l1= args.value[0].split(',')
	source_folder, dest_folder = [i for i in args.crop][0], [i for i in args.crop][1]
	
	print(f'\n[SOURCE FOLDER]: {source_folder}\n')
	print(f'[DESTINATION FOLDER]: {dest_folder}\n')

	if type_=='px':
		dim = tuple([int(i) for i in l1])
		crp_px(source_folder, dest_folder, dim = val)
	else:
		pct = [float(i) for i in args.value][-1]
		crp_p(source_folder, dest_folder, pct = pct)
	

