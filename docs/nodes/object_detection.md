# <p style="text-align: center;"> Object Detection </p>

## **Summary**

This node is responsible for detecting buoys and baoats while in the water, which includes calculating the angle and distance. To detect the buoys, our system uses a computer vision model based on Ultralytics Yolo11. We use the <a href="https://docs.ultralytics.com/modes/predict/#working-with-results" target="_blank">Ultralytics  results</a> object to retrieve any information about object detections. We also use ROS2 to publish the angle to the buoy, the depth distance to the buoy as well as a list of detection results that involve the cnofidence value, relative x-position, and relative y-position of the detrected bounding boxes.


<br>

## **Listens to the Following Topics**


- /camera/camera/aligned_depth_to_color/image_raw (Image from sensor_msgs)
- /camera/camera/color/image_raw (Image from sensor_msgs)


## **Publishes to the Following Topics**
- /buoy_angle (Float32 from std_msgs)
- /buoy_depth_pixel (Float32 from std_msgs)
- /object_detection_results (ObjectDetectionResultsList from sailbot_msgs)