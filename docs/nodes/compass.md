# <p style="text-align: center;"> Compass </p>

## **Summary**
This node is responsible for communicating back and forth between our tilt-compensating compass ([CMPS14](https://www.robotshop.com/products/tilt-compensated-magnetic-compass-cmps14)) which give us data on where our current heading is. We employ various filtration techniques to ensure that the data we get back contains as little noise as possible.

Since our compass can only communicate through I2C, we created a ustom I2C to USB UART converter out of a spare arduino nano (its surprisingly hard to find good ones of these off of Amazon). The code for this converter is found in the arduino repository.


*Side Note*: Funny story, at the 2024 Sailbot competition, we were scrambling because our compass didn't work. We didn't have time to fully integration test as a team because the hull got finished super late into the school year and by the time we were ready to integration test Chris had already left back home, so we were forced to do all of our testing (yes even on-water testing) over teamviewer and discord calls with the MechE lead, Adam, and our Navarch team lead, Michio who had stayed in Blacksburg. That was an interesting time, but the main point is that we hadn't really found the time to make sure the compass worked inside the boat since we had only tested it outside the boat and assumed it would just work. Now I am not naming names, but someone on the Mech team decided to make the mounting bracket for the compass out of metal and put it in a place that was kind of obscured and hard to see/ take out. The first time we went to test our compass was giving us crazy and inconsistant values and we didn't know why. Sometimes it was really right and sometimes it was wrong, so after like 2 days (AT COMP) of trying to debug every point of failure possible, recallibrating, and reflashing the I2C to UART converter, that the issue was the metal bracket, and we eventually had another one 3D printed (thank God we brought our 3D printer lol). Moral of the story, always integration test and never make the compass mounting bracket out of metal!

## **Command to Run the Node**
``` sh
ros2 run compass compass
```

<br>
## **Publishes to the Following Topics**
- /heading (Float32 from std_msgs)
