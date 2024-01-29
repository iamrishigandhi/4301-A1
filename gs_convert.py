import cv2
import sys
import os

def convert_to_grayscale(input_image, output_image):
    # Read the input image
    image = cv2.imread(input_image)

    if image is None:
        print("Error: Unable to read the input image.")
        sys.exit(1)

    # Convert the image to grayscale using the luma-based method
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Save the grayscale image
    cv2.imwrite(output_image, gray_image)

    print(f"Grayscale image saved at {output_image}")

if __name__ == "__main__":
    # Check if the correct number of command line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python gs_convert.py <input_image.jpg>")
        sys.exit(1)

    input_image = sys.argv[1]

    # Check if the input file exists
    if not os.path.isfile(input_image):
        print(f"Error: The file {input_image} does not exist.")
        sys.exit(1)

    # Extract filename and extension
    filename, extension = os.path.splitext(input_image)

    # Check if the file is a JPEG image
    if extension.lower() != ".jpg":
        print("Error: Please provide a .jpg image as input.")
        sys.exit(1)

    # Construct the output image path with "_GREY" appended before .jpg extension
    output_image = filename + "_GREY.jpg"

    # Convert the image to grayscale and save it
    convert_to_grayscale(input_image, output_image)
