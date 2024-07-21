# <p style="text-align: center;"> Sailbot Messages </p>

## **Summary**
This package contains various custom messages types that nodes would need to send to each other! Try to add messages to the custom messages library sparingly as we would like most nodes to only publish/ listen with a message type in the base ros2 messages. This keeps our code easily compatible with other peoples' drivers so we can just drop in other peoples' drivers if we ever need to.

<br>

## **Contains the Following Messages**
**RCData**  
&nbsp;&nbsp;&nbsp;&nbsp;  float32 joystick_left_x  
&nbsp;&nbsp;&nbsp;&nbsp;  float32 joystick_left_y  
&nbsp;&nbsp;&nbsp;&nbsp;  float32 joystick_right_x  
&nbsp;&nbsp;&nbsp;&nbsp;  float32 joystick_right_y  
&nbsp;&nbsp;&nbsp;&nbsp;  bool button_a  
&nbsp;&nbsp;&nbsp;&nbsp;  uint8 toggle_b  
&nbsp;&nbsp;&nbsp;&nbsp;  uint8 toggle_c  
&nbsp;&nbsp;&nbsp;&nbsp;  bool button_d  
&nbsp;&nbsp;&nbsp;&nbsp;  uint8 toggle_e  
&nbsp;&nbsp;&nbsp;&nbsp;  uint8 toggle_f  

**WaypointList**  
&nbsp;&nbsp;&nbsp;&nbsp;  sensor_msgs/NavSatFix[] waypoints  