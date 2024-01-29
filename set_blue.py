import cv2
import sys

def set_blue(input_filename, output_filename):
    # Read the image
    image = cv2.imread(input_filename)

    if image is None:
        print(f"Error: Unable to read image from {input_filename}")
        return

    # Set the red channel to 0
    image[:, :, 2] = 0  # Red channel index is 2 (0-based index)

    # Save the modified image
    cv2.imwrite(output_filename, image)

    print(f"Blue channel set successfully. Output saved to {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python set_blue.py [input filename].jpg")
    else:
        input_filename = sys.argv[1]
        output_filename = f"{input_filename.split('.')[0]}_RED.jpg"
        set_blue(input_filename, output_filename)