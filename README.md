# Modules

Modules in Python are objects of ModuleType. 


![](https://media.giphy.com/media/MeJuOjXoc5ZyrWSDev/giphy.gif)


# Assignment Tasks

**1 & 2. JPG/JPEG to PNG conversion** (use PIL library) **j2p** & **PNG to JPG conversion** (use PIL library) **p2j**

    * wrote a single function which does both conversions
    * extracted file extension and found it's counterpart.
    * Used .convert() to modify input image to RGB and then converted image file to png or jpg depending on input file extension.
    * saved converted files in destination folder.

**3**. **Image Resizer** that can resize bulk images with these features: 

    i. resize by user determined percentage (say 50% for height and width) (proportional) res_p
    ii. resize by user determined width (proportional) res_w
    iii. resize by user determined height (proportional) res_h


Procedure:

    * First, checked the resize input params, whether it's resize by (width, height) or resize by proportion(percentage).
    * based on these params resizing the image using PIL library.
    * saved the same in destination folder.

**4.**  **Image Cropper** that can crop bulk images with these features: 

    i. Center square/rectangle crop by user-determined pixels crp_px
    ii. Centre square/rectangle crop by user-determined percentage (crop to 50%/70%) crp_p
    iii. It let's user know which all images were not cropped due to size mismatches

Procedure:

    * First, checked the crop input params, whether it's crop by pixels or crop by proportion(percentage).
    * Validated the input dimensions and percentage values.
    * Cropped the images according to the arguments passed in,except some which couldn't get cropped due to size mismatch






# TEST CASES


* test_readme_exists(): Checks if the README File exists or not.

* test_readme_contents(): Checks if the README has atleast 300 words.

* test_readme_proper_description(): Checks if the README has relevant keywords in it.

* test_readme_file_for_formatting(): Checks if it has relevant number of '#'

* test_function_name_had_cap_letter(): Checks if the Function name was starting with a Capital Letter.

* test_class_name_had_cap_letter(): Checks if the Class name was starting with a Capital Letter.

## FUNCTION TEST CASES


* test_path_convert(): Checks if the input path is valid or not for convert module

* test_path_resize():Checks if the input path is valid or not for resize module

* test_h(): Checks if the height passed is valid or not.

* test_w(): Checks if the width passed is valid or not.

* test_pct_resize: Checks if the percentage value passed is valid or not for resize module.

* test_path_cc(): Checks if the input path is valid or not for center_crop module.

* test_pct_cc(): Checks if the percentage value passed is valid or not for center_crop module.

* test_dim_cc(): Checks if the dimension passed is of valid or not for center_crop module.

* test_files(): Checks if all modules are present or not(Ideally saved them in the same directory.)

* test_convert_exec(): Checks if the convert.py file is executable in cmd.

* test_resize_exec(): Checks if the resize.py file is executable in cmd.

* test_center_crop_exec(): Checks if the center_crop.py file is executable in cmd.

* test_annotations(): Checks if the functions have annotations or not. 

* test_docstrings(): Checks if the functions have docstring or not. '

* test_invalid_docstrings(): Checks if the docstrings contain any irrelevant symbols. 






