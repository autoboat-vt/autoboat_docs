# <p style="text-align: center;"> Autopilot </p>

## **Summary**
This node is responsible for listening to data about the current state of the boat and a set of waypoints and publishing the desired rudder and sail angles based on our autopilot software. This node runs completely asynchronously on an internal timer, which means that a few times every seconds it runs a *non-blocking* script to calculate what the desired rudder and sail angles should be and publishes them when its done.

Additionally, this node publishes data that is useful for telemetry and debugging such as the the current maneuver it is attempting to perform and what its desired heading is currently.

An important thing to note is that this node also controls basic RC override, which is why it needs to listen into the raw RC data. There are several different types of RC override listed below:  
![Code for Switching Modes](../images/switches_and_autopilot_modes.png)
TODO: make this actually documented lol


<br>
## **The Autopilot Parameters System**

In order for us to be able to control and tune parameters for the autopilot from the groundstation, this node also listens for autopilot_parameters. These are jsons (serialized as strings) which detail all of the new parameters and what their values should be. These values are sent from the groundstation to the telemetry server, then to the telemetry node and then finally to the autopilot. An example of these parameters is shown below:
![Example of Autopilot Parameters JSON](../images/autopilot_parameters_example.png)  

Not all of the parameters need to be included in the json. If only some of the parameters are included, then only those parameters will get changed in the autopilot.



<br>
## **Command to Run the Node**
``` sh
ros2 run autopilot autopilot
```

<br>
## **Listens to the Following Topics**
- /position (NavSatFix from sensor_msgs)
- /velocity (Twist from geometry_msgs)
- /heading (Float32 from std_msgs)
- /apparent_wind_vector (Vector3 from geometry_msgs)
- /autopilot_parameters (String from std_msgs)
- /rc_data (RCData from sailbot_msgs)
- /autopilot_mode (String from std_msgs)
- /waypoints_list (WaypointList from sailbot_msgs)

## **Publishes to the Following Topics**
- /full_autonomy_maneuver (String from std_msgs)
- /desired_heading (Float32 from std_msgs)
- /actions/sail_angle (Float32 from std_msgs)
- /actions/rudder_angle (Float32 from std_msgs)
