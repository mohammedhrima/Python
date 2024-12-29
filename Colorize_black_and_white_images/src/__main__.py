from colorize_it import colorize
import cv2

# List of images
image_list = ["003.jpeg", "004.jpg", "005.jpg", "006.jpg", "007.jpg"]

# Iterate through the list of images
for image_path in image_list:
    # Read the grayscale image
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Colorize the image using the Colorize-it library
    colorized_image = colorize(img)

    # Save and display the colorized image
    output_path = f"colorized_{image_path}"
    cv2.imwrite(output_path, colorized_image)
    print(f"Colorized image saved to {output_path}")
    cv2.imshow('Colorized Image', colorized_image)
    cv2.waitKey(0)  # Wait for a key press to move to the next image
    cv2.destroyAllWindows()
