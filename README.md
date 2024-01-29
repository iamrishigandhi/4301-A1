# Image Processing with OpenCV

This repository contains Python programs for basic image processing tasks using the OpenCV library. Each program addresses a specific task, and the details are outlined below.

## Installation

To get started, make sure you have Python 3.x (your preferred version) installed. Follow these steps to install OpenCV:

```bash
pip install opencv-python
```

## Task 1: Install OpenCV : test_opencv_version.py

Ensure that OpenCV is installed successfully by running the following Python code:

```python
import cv2 as cv

print(cv.__version__)
```

Capture a screen image of the code execution in your terminal and the resulting output to verify the successful installation.

## Task 2: Basic Pixel Editing : set_blue.py

The `set_blue.py` program takes a .jpg image as a command-line argument and outputs a modified .jpg file. In the output image, the red channel for each pixel is set to 0. Execute the program as follows:

```bash
python set_blue.py <input_image>.jpg
```

The modified image will be saved as `<input_image>_RED.jpg`.

## Task 3: Convert Image to Greyscale : gs_convert.py

The `gs_convert.py` program converts a .jpg image to greyscale using a luma-based method. Execute the program with the following command:

```bash
python gs_convert.py <input_image>.jpg
```

The greyscale image will be saved as `<input_image>_GREY.jpg`.

## Task 4: Shift Color and Clamp : shift_color.py

The `shift_color.py` program adds a constant factor to the RGB components of each image pixel. Execute the program as follows:

```bash
python shift_color.py <input_image>.jpg <0-255> <0-255> <0-255>
```

The output image will be saved as `<input_image>_CLAMP.jpg`.

Feel free to explore and experiment with different images and parameter values.

---

