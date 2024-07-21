# <p style="text-align: center;"> RC (Remote Controller) </p>


## **Summary**
This node is responsible for communicating back and forth between our RC (remote controller). I believe the RC we use is one in the Radiomaster RP series but I am not entirely sure about the specific model since it has been a while since I have looked at it (I'll hopefully update this when school starts again). The communication protocol that we use is called CRSF with ExpressLRS, and we use the crsf_parser pip package to help us parse the crsf frames (frames are just a fancy way to say message packets).

<br>

## **Command to Run the Node**
``` sh
ros2 run rc rc
```

<br>

## **Publishes to the Following Topics**
- /rc_data (RCData from sailbot_msgs)