# <p style="text-align: center;"> Object Detection </p>

## **Summary**

This node is responsible for detecting buoys and baoats while in the water, which includes calculating the angle and distance. To detect the buoys, our system uses a computer vision model based on Ultralytics Yolo11. We use the <a href="https://docs.ultralytics.com/modes/predict/#working-with-results" target="_blank">Ultralytics  results</a> object to retrieve any information about object detections. We also use ROS2 to publish the angle to the buoy, the depth distance to the buoy as well as a list of detection results that involve the cnofidence value, relative x-position, and relative y-position of the detrected bounding boxes.
