import sys
import cv2

def set_blue_to_zero(input_filename):
    # Read the input image
    img = cv2.imread(input_filename)

    if img is None:
        print("Error: Could not read the file. Make sure the file exists.")
        return

    # Set the blue channel to 0 for each pixel
    img[:, :, 0] = 0  # 0 corresponds to the blue channel in OpenCV's BGR format

    # Get the output filename
    output_filename = input_filename.replace('.jpg', '_RED.jpg')

    # Save the modified image
    cv2.imwrite(output_filename, img)

    print(f"Image saved as {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python set_blue.py [input filename].jpg")
    else:
        input_filename = sys.argv[1]
        set_blue_to_zero(input_filename)