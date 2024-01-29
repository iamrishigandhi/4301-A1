import cv2
import numpy as np
import sys

def shift_color(image, r_shift, g_shift, b_shift):
    shifted_image = image.copy()

    # Shift the RGB components and clamp the values
    shifted_image[:, :, 0] = np.clip(image[:, :, 0] + b_shift, 0, 255)
    shifted_image[:, :, 1] = np.clip(image[:, :, 1] + g_shift, 0, 255)
    shifted_image[:, :, 2] = np.clip(image[:, :, 2] + r_shift, 0, 255)

    return shifted_image

def main():
    if len(sys.argv) != 5:
        print("Usage: python shift_color.py <input_image.jpg> <r_shift> <g_shift> <b_shift>")
        sys.exit(1)

    # Read input image
    input_image_path = sys.argv[1]
    image = cv2.imread(input_image_path)

    if image is None:
        print("Error: Unable to read the input image.")
        sys.exit(1)

    # Parse shift values
    try:
        r_shift = int(sys.argv[2])
        g_shift = int(sys.argv[3])
        b_shift = int(sys.argv[4])
    except ValueError:
        print("Error: Shift values must be integers.")
        sys.exit(1)

    # Apply color shifts and clamp the values
    shifted_image = shift_color(image, r_shift, g_shift, b_shift)

    # Save the output image
    output_image_path = input_image_path.replace('.jpg', '_CLAMP.jpg')
    cv2.imwrite(output_image_path, shifted_image)

    print(f"Image successfully processed. Output saved as {output_image_path}")

if __name__ == "__main__":
    main()