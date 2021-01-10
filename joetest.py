import cv2
image = cv2.imread('road.jpg')

h, w = image.shape[:2]
print(f"Height= {h}  Width={w}")

#resize = cv2.resize(image, (800, 800))
output = image.copy()

rectangle = cv2.rectangle(output, (1500, 900), (600, 400), (255, 0, 0), 2)
