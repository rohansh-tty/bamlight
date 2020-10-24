# bamlight

Simple Image Editor using cmd

## Motivation:

When I was working on MODEST, a lot of Image Augmentation had to be done, mostly some kind of basic PMDA(Poor Man's Data Augmentation). I used seperate python scripts which could do the job, but I needed something powerful which would be easy, simple and robust. This is my effort to create the same. 

 
## Usage

If you want to use the whole app, then modify values in main.py, all the directory paths, resize and crop variables.

Open CMD and run this.

``
 
    cd to/the/cloned/directory/

    python ImageApp.zip
``

Now if you want to use indiviual functions like crop or resize or image conversion, follow this

``

     cd to/the/cloned/directory
     
     python convert.py --type '<mention type of conversion either ('j2p', 'p2j')>' --convert '<pass in the source and final output directory path>'

     python resize.py --type '<mention type of conversion either ('prop', 'prop_w', 'prop_h')>' --val '<pass in the value>' --resize '<pass in the source and final output directory path>'
     
     python center_crop.py --type '<mention type of conversion either ('px', 'p')>' --val '<pass in the value>' --crop '<pass in the source and final output directory path>'
   
  
``
 
## Features
 
**1 & 2. JPG/JPEG to PNG conversion** (use PIL library) **j2p** & **PNG to JPG conversion** (use PIL library) **p2j**


    * a single function which does both conversions
    * extracted file extension and found it's counterpart.
    * Used .convert() to modify input image to RGB and then converted image file to png or jpg depending on input file extension.
    * converted files in destination folder.

**3**. **Image Resizer** that can resize bulk images with these features: 

    i. resize by user determined percentage (say 50% for height and width) (proportional) res_p
    ii. resize by user determined width (proportional) res_w
    iii. resize by user determined height (proportional) res_h


Procedure:

    * First, the resize input params are checked, whether it's resize by (width, height) or resize by proportion(percentage).
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
