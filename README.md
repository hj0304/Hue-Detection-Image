# Color Detection Program with OpenCV
---
### Color Detection using OpenCV and Python

This project is a color detection program implemented with OpenCV and Python. Special thanks to Adrian Rosebrock from pyimagesearch for providing excellent tutorials, and this project is inspired by his blog. The implementation includes both the author's code and additional code I have written.

## **Key Points**  
---
1. **Steps involved**:  
    1.Color Detection in Image: Identify colors in the image.
    2.Find Color Regions: Locate regions in the image corresponding to the specified color range.
    3.Highlight Detected Colors: Emphasize the regions of the found colors in the image.

2. **Assumptions**:  
    1.The image contains a readily identifiable reference object, and the color of this object is known to us.
    2.Size is calculated based on the "Pixel Per Metric" ratio using the given reference object.

3. **Reference Object Properties**:  
    1.We should know the color of the reference object.
    2.The reference object should be easily identifiable in the image.

4. **Reference Object Used**:  
    1.For example, a red circle.

5. **Implementation Details**:  
    1.Use OpenCV's `inRange` method to detect colors in the image.

## **Requirements** (Versions Tested):  
---
- Python (3.7.3)
- OpenCV (4.1.0)
- NumPy (1.61.4)
- imutils (0.5.2)

## **Commands to Run the Detection**:  
---
```
python color_detection.py --image images/example_01.png --color red
```
## **Results**:  
---
The results display the highlighted areas of the detected color in the image. The accuracy of color detection may vary depending on the image characteristics and environment.

## **The limitations**
---
Image Quality: The accuracy of color detection may be influenced by the quality of the image.
Lighting Conditions: Inappropriate lighting conditions can lead to distortion in color detection.