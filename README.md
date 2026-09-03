# Computer Vision

Welcome to my Computer Vision repository! This project is dedicated to storing basic Python scripts and image resources for exploring computer vision concepts using OpenCV.

## Directory Structure

* **`Files/`**: Contains the Python source code.
* **`Images/`**: Contains the sample images used for processing and testing.

## About the Script (`images.py`)

Located in the `Files` directory, `images.py` is a beginner-friendly script that demonstrates the fundamental task of loading and displaying an image using the OpenCV library. 

**How it works:**
1. It imports the `cv2` module.
2. It targets a specific image file located in the `Images` directory using a relative file path (`../Images/Image1.png`).
3. It utilizes `cv2.imread()` to read the image file from the disk into a NumPy array.
4. It uses `cv2.imshow()` to open a graphical UI window to display the image.
5. It pauses execution using `cv2.waitKey(0)` so the window remains open until the user presses any key.

## About the Images

The `Images` folder contains sample `.png` files used to test the OpenCV scripts. Currently, it contains:
* **`Image1.png`**
* **`Image2.png`**

## How to Run

To run the script locally on your machine, ensure you have Python and the OpenCV library installed.

1. Install OpenCV (if you haven't already):
```bash
pip install opencv-python
