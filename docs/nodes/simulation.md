# <p style="text-align: center;"> Simulation </p>

## **Summary**


*talk about building your own simulation gui and how to build sailboat-gym pip package from source
*talk about building your own gazebo simulation situation through the other repo

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