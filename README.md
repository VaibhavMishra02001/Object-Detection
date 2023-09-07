# Object-Detection

Devised an algorithm for the detection and tracking of red colored objects in Python and MATLAB.

## Implementation

Developed a color-filtering algorithm to extract objects of interest and implemented centroid tracking for real-time object tracking.

#### MATLAB
Stored the centroid points of the object for tracking. In Matlab first applied the median filter and then converted the image into binary. Then, used regionprops to find the centroid.

#### Python
Converted RGB image to HSV and then used Contours for object tracking.


## Results

![coour_detection](https://user-images.githubusercontent.com/102024497/229204009-0c255e18-7acc-4ee9-a8f4-5a3c1f8af242.png)


