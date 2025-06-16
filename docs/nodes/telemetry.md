# <p style="text-align: center;"> Telemetry </p>

## **Summary**
This node is responsible for listening to various topics and sending the data to the telemetry server so that we, on the ground, can view the data. Additionally, this node is also responsible for listening to autopilot parameters and waypoints stored in the telemetry server and sending them to the autopilot node. This allows us to change parameters of the autopilot and change the waypoints the boat needs to follow from the shore.  

The telemetry node listens to data about the boats current state such as the position, velocity, heading, apparent wind vector. It also listens in on data that lets us know what the autopilot is currently thinking such as the current sail/ rudder angle, the heading it is trying to sail towards, a list of all of the waypoints that it is trying to follow, an index that represents what waypoint the autopilot is currently on, the name of the mode the autopilot is currently on (whether it is in RC mode, full autonomy mode, or some semi-autonomous mode), and the maneuver the boat might be trying to perform if it is in full autonomous mode (like tacking/ jibing).



<br>
## **Listens to the Following Topics**
- /position (NavSatFix from sensor_msgs)
- /velocity (Twist from geometry_msgs)
- /heading (Float32 from std_msgs)
- /apparent_wind_vector (Vector3 from geometry_msgs)
- /actions/sail_angle (Float32 from std_msgs)
- /actions/rudder_angle (Float32 from std_msgs)
- /desired_heading (Float32 from std_msgs)
- /waypoints_list (WaypointList from sailbot_msgs)
- /cur_waypoint_index (Int32 from std_msgs)
- /full_autonomy_maneuver (String from std_msgs)
- /autopilot_mode (String from std_msgs)


## **Publishes to the Following Topics**
- /waypoints_list (WaypointList from sailbot_msgs)
- /autopilot_parameters (String from std_msgs)