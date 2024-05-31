# import cv2
# import numpy as np
# from matplotlib import pyplot as plt

# def canny_edge_detection(image_path, low_threshold=25, high_threshold=35):
#     # Load the image in grayscale
#     image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    
#     # Check if image is loaded properly
#     if image is None:
#         print("Error: Unable to load image.")
#         return
    
#     # Apply Gaussian Blur to reduce noise
#     blurred_image = cv2.GaussianBlur(image, (5, 5), 1.4)
    
#     # Apply Canny edge detection
#     edges = cv2.Canny(blurred_image, low_threshold, high_threshold)
    
#     # Display the original and edge-detected images
#     plt.figure(figsize=(10, 5))
    
#     plt.subplot(1, 2, 1)
#     plt.title('Original Image')
#     plt.imshow(image, cmap='gray')
#     plt.axis('off')
    
#     plt.subplot(1, 2, 2)
#     plt.title('Canny Edges')
#     plt.imshow(edges, cmap='gray')
#     plt.axis('off')
    
#     plt.tight_layout()
#     plt.show()

# # Example usage
# image_path = 'UBIRIS_800_600\Sessao_1/3/Img_3_1_2.jpg'
# canny_edge_detection(image_path)


######################################################################

# import sys
# import cv2 as cv
# import numpy as np
# def main(argv):

#     default_file = 'UBIRIS_800_600\Sessao_1/2/Img_2_1_1.jpg'
#     filename = argv[0] if len(argv) > 0 else default_file
#     # Loads an image
#     src = cv.imread(cv.samples.findFile(filename), cv.IMREAD_COLOR)
#     # Check if image is loaded fine
#     if src is None:
#         print ('Error opening image!')
#         print ('Usage: hough_circle.py [image_name -- default ' + default_file + '] \n')
#         return -1


#     gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)


#     gray = cv.medianBlur(gray, 5)


#     rows = gray.shape[0]
#     circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, rows/8,
#     param1=60, param2=100,
#     minRadius=10, maxRadius=400)


#     if circles is not None:
#         circles = np.uint16(np.around(circles))
#         for i in circles[0, :]:
#             center = (i[0], i[1])
#             # circle center
#             cv.circle(src, center, 1, (0, 100, 100), 3)
#             # circle outline
#             radius = i[2]
#             cv.circle(src, center, radius, (255, 0, 255), 3)


#     cv.imshow("detected circles", src)
#     cv.waitKey(0)

#     return 0
# if __name__ == "__main__":
#     main(sys.argv[1:])

##########################################################
###########################################################
###########################################################             here
import cv2
import numpy as np
from matplotlib import pyplot as plt

def preprocess_image(image_path):
    # Load the image in grayscale
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Apply Gaussian Blur to reduce noise
    blurred_image = cv2.GaussianBlur(image, (5, 5),1.2)
    return blurred_image

def detect_iris(image):
    # # #Apply Canny edge detection
    # edges = cv2.Canny(image,40, 60)
    # # Display the original and edge-detected images
    # plt.figure(figsize=(10, 5))
    
    
    # plt.subplot(1, 2, 2)
    # plt.title('Canny Edges')
    # plt.imshow(edges, cmap='gray')
    # plt.axis('off')
    
    # plt.tight_layout()
    # plt.show()
    # # Detect circles using Hough Transfor
    for r in range(30,500,10):
        circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, 1, 4000,
        param1=40, param2=60,
        minRadius=r, maxRadius=r+10)
        
        print(circles)
        
        if circles is not None:
            circles = np.round(circles[0, :]).astype("int")
            for (x, y, r) in circles:
                # Draw the circle in the output image
                cv2.circle(image, (x, y), r, (255, 0, 0), 2)
                # Draw a small circle (of radius 3) to show the center
                cv2.circle(image, (x, y), 3, (0, 255, 0), 3)
            return image, circles
        return image, None

def plot_images(original, processed, title1='Original Image', title2='Processed Image'):
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title(title1)
    plt.imshow(original, cmap='gray')
    
    plt.subplot(1, 2, 2)
    plt.title(title2)
    plt.imshow(processed, cmap='gray')
    plt.show()

# Example usage
# image_path = 'UBIRIS_800_600\Sessao_1/1/Img_1_1_2.jpg'

import os

#loop for mmu database
for i in range(1,238):
    folder_path = "UBIRIS_800_600/Sessao_1/{}/".format(i)
    # folder_path_left = folder_path+"/"+"left"+"/"
    # folder_path_right = folder_path+"/"+"right"+"/"
    fs =os.listdir(folder_path)
    for f in fs:
        if f=="Thumbs.db":
            continue
        image_path = folder_path+f
        print(image_path)
    # file_namesl = [f for f in os.listdir(folder_path_right)]
    # print(file_namesr)
    # print(file_namesl)

        original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        preprocessed_image = preprocess_image(image_path)
        localized_image, circles = detect_iris(preprocessed_image)

        # Plot the results
        plot_images(original_image, localized_image, title2='Iris Localization')

        # If circles are detected, print their coordinates and radii
        if circles is not None:
            for (x, y, r) in circles:
                print(f'Iris detected at x: {x}, y: {y} with radius: {r}')
        else:
            print('No iris detected.')
###################################################################
#not detected correctly 6,14,18,19,20,25,42,51,55,60,64,68,70,74,81,83,91,95,100,106,111,117,161,162,168,173,180,191,199,201,212,214,222,227,240
# 3,4,18,19,20,21,22