# Importing all the essential libraries
import cv2
import time
from google.colab.patches import cv2_imshow

# Load YOLO weights and configuration
arc = cv2.dnn.readNet("yolov4.weights", "yolov4.cfg")
arc.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
arc.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA_FP16)

# Load class names
class_names = []
with open("coco.names", "r") as f:
    class_names = [cname.strip() for cname in f.readlines()]

# Load image
img = cv2.imread("Swiss.jpeg")

# Create YOLO model
model = cv2.dnn_DetectionModel(arc)
model.setInputParams(size=(640, 640), scale=1/255, swapRB=True)

# Set confidence and NMS threshold
confidence = 0.6
Nms = 0.3

# Perform object detection
classes, scores, boxes = model.detect(img, confidence, Nms)

# Draw bounding boxes and labels
for (classid, score, box) in zip(classes, scores, boxes):
    label = class_names[classid[0]]
    confidence = str(round(score[0], 2))
    cv2.rectangle(img, box, color=(255, 200, 10), thickness=2)
    cv2.putText(img, f'{label} {confidence}', (box[0], box[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (25, 55, 255), 2)

# Display the image with detections
cv2_imshow(img)
