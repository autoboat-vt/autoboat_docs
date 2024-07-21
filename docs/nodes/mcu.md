# <p style="text-align: center;"> MCU (Micro Controller Unit) </p>

## **Summary**
This node is responsible for communicating back and forth between our MCU, also known as just micro-controllers. micro-controllers are devices like arduinos that help our jetson communicate with the motors and some very specific sensors on board that we would rather route through the micro-controller (Please refer to the electrical the electrical schematic in for what we are routing through our micro-controller of choice). Primarily, this node's responsibility is to communicate with the MCU through a USB serial connection and whatever format that we decided to send our data in.

*Side Note*: There is an odd story behind us using a microcontroller to speak with everything. A while back (before even Chris's time) we used to control the motors and stuff directly with our on-board computer, but someone fried the on-board computer and ever since we were told to not control motors directly with the on-board computer. Its strange because there should never be a high voltage running through back to the on-board computer, so I don't quite know what happened there. Either way, I like it better this way because it allows us to easily unplug and replug everything into the jetson (since it is all plugged in via USB).


<br>
## **Command to Run the Node**
``` sh
ros2 run mcu mcu
```

<br>
## **Listens to the Following Topics**
- /actions/sail_angle (Float32 from std_msgs)
- /actions/rudder_angle (Float32 from std_msgs)