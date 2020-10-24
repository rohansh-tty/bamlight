from PIL import Image
import os
import argparse


import convert
import resize
import center_crop

CROP_PATH = r'.\results\cropped_images'
RESIZE_PATH = r'.\results\resized_images'
IMAGE_DIRECTORY = r'.\images' 
J2P_DIRECTORY = r'.\results\j2p_images'
P2J_DIRECTORY = r'.\results\p2j_images'

for path in {CROP_PATH, RESIZE_PATH, J2P_DIRECTORY, P2J_DIRECTORY}:
	if not os.path.isdir(path):
		os.mkdir(path)


convert.j2p(IMAGE_DIRECTORY, J2P_DIRECTORY)
convert.p2j(IMAGE_DIRECTORY, P2J_DIRECTORY)

resize.res_p(IMAGE_DIRECTORY, RESIZE_PATH, pct=0.8)
resize.res_h(IMAGE_DIRECTORY, RESIZE_PATH, height=500)
resize.res_w(IMAGE_DIRECTORY, RESIZE_PATH, width=500)

center_crop.crp_px(IMAGE_DIRECTORY, CROP_PATH, dim=(0, 0, 224, 224))

# center_crop.center_crop_image(IMAGE_DIRECTORY, CROP_PATH, dim=(10,50,20,60))

