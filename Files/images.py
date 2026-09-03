import cv2

image_path = '../Images/Image1.png' 

image = cv2.imread(image_path)

if image is not None:
    print("Image loaded successfully!")
    
    cv2.imshow('Computer Vision - Image Viewer', image)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Error: Could not load the image from {image_path}. Please check the file name and path.")
