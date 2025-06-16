# <p style="text-align: center;"> RC (Remote Controller) </p>


## **Summary**
This node is responsible for communicating back and forth between our RC (remote controller). The remote controller that we use is the Radiomaster TX12 and the receiver that we use is the Radiomaster ER6. The communication protocol that we use is called CRSF with ExpressLRS, and we use the crsf_parser pip package to help us parse the crsf frames (frames are just a fancy way to say message packets).

<br>

## **Publishes to the Following Topics**
- /rc_data (RCData from sailbot_msgs)