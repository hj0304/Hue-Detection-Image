# Color Detection Program with OpenCV
---
![pitcture1]()
![pitcture2]()
![pitcture3]()
![gif1]()
### Color Detection using OpenCV and Python

This project is a color detection program implemented with OpenCV and Python. In consideration of color weakness patients who cannot see a specific color or the optical illusion effect of colors that see the same color differently depending on the angle of light, a project was carried out to extract the color desired by the user in the image using it

## **Key Points**  
---
1. **Steps involved**:  
    1. Show color pallet consisting of Colors represneted image.
    2. Find color's name or similar color's name.
    3. Color Detection in Image: Identify colors in the image about input colors by client
    4. Find Color Regions: Locate regions in the image corresponding to the specified color range.
    5. Highlight Detected Colors: Emphasize the regions of the found colors in the image.

2. **Assumptions**:  
    1. Size is calculated based on the "Pixel Per Metric" ratio using the given reference object.
    2. The extraction colors are limited to 10 colors such as blue, red, and green.


3. **Implementation Details**:  
    1. It is certain to use an image in which there are many colors that the user wants to extract.
  

## **Requirements** (Versions Tested):  
---
- Python (3.7.3)
- OpenCV (4.8.1.78)
- NumPy (1.24.3)
- extcolors (1.0.0)
- webcolors (1.13)
- matplotlib (3.7.1)

## **Commands to Run **:  
---
**1. Install  necessary packages in terminal**
```
 pip install extcolors
 pip install webcolors
```
**2. Setting img path according to your file storage location**
- Example
```
IMG_PATH = "blue.jpg"
```

## **Results**:  
---
The result is a color palette composed of the main colors of the image and a name of the corresponding color, and an image output from which the color selected by the user is extracted.

## **The limitations**
---
Image Quality: The accuracy of color detection may be influenced by the quality of the image.
Lighting Conditions: Inappropriate lighting conditions can lead to distortion in color detection.
Limited Color Name : Only 140 unique color names used for CSS2 can be presented because webcolor module is used

## **Refernece**:  
---
- [https://velog.io/@nayeon_p00/OpenCV-Python-HSV-색공간에서-이미지의-특정색-추출하기](https://velog.io/@nayeon_p00/OpenCV-Python-HSV-색공간에서-이미지의-특정색-추출하기)
- [https://webcolors.readthedocs.io/en/1.13/index.html](https://webcolors.readthedocs.io/en/1.13/index.html)
- [https://github.com/CairX/extract-colors-py#22input---script](https://github.com/CairX/extract-colors-py#22input---script)
- [https://gogetem.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-RGB-]( https://gogetem.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-RGB-%EC%88%AB%EC%9E%90%EB%A1%9C-%EC%83%89%EA%B9%94-%EC%9D%B4%EB%A6%84-%ED%94%84%EB%A6%B0%ED%8A%B8%ED%95%98%EA%B8%B0-feat-webcolors)
- [https://stickode.tistory.com/577](https://stickode.tistory.com/577)
```
Thank you
