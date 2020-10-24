# bamlight
Simple Image Editor using cmd

 
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
