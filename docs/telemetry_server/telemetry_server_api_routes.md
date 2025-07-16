## <p style="text-align: center;"> **Telemetry Server API Routes** </p>


label certain routes as specifically used by the groundstation or specifically used by the telemetry node


## <p style="text-align: center;"> **How to Access and Test These Routes** </p>

If you would like to manually test some of these routes to see if they are working without having to make any extra scripts, then you should use an API tester like [Postman](https://www.youtube.com/watch?v=MFxk5BZulVU). TODO TODO TODO

TODO TODO TODO TODO


## <p style="text-align: center;"> **Route Definitions** </p>


### <p style="text-align: center;"> **Boat Status Routes** </p>

The boat status has a very specific format whenever you are receiving or sending a "boat status". A boat status must be in the form of a dictionary with all of the following entries. The motorboat needs to send the entries under General and Motorboat Specific and the sailboat needs to send the entries under General and Sailboat Specific:

```json
{

    # General
    "position": [0.0, 0.0],          # longitude, latitude
    "state": "WAYPOINT_MISSION",   # a string that describes the autopilot mode that the boat is in. This can be Full_RC, Waypoint_Mission, Hold_Heading, etc etc. This depends heavily on how the specific autopilot sets it up though and these are just examples 
    "speed": 0.0,    # speed in meters/second
    "velocity_vector": [0.0, 0.0], # global velocity vector in m/s. [true east, true north]
    "bearing": 0.0, # the angle to the next waypoint in degrees
    "heading": 0.0, # describes the way the boat is rotated in degrees ccw from true east
    "rudder_angle": 0.0, # the desired rudder angle in degrees
    "current_waypoint_index": 0, # the index of the current waypoint. The autopilot is given a list of waypoints, and the autopilot will attempt to follow them one by one. This variable tracks that and how many waypoints the autopilot has completed in the current route
    "distance_to_next_waypoint": 0.0, # the distance to the next waypoint in meters

    # Sailboat Specific: 
    "full_autonomy_maneuver": "CW_TACKING", # mainly used for the sailboat to describe whether or not we are tacking and how we are tacking (ccw or cw tack) 
    "true_wind_speed": 0.0, # true wind speed in m/s 
    "true_wind_angle": 0.0, # true wind angle in degrees
    "apparent_wind_speed": 0.0, # apparent wind speed in m/s
    "apparent_wind_angle": 0.0, # apparent wind angle in degrees
    "sail_angle": 0.0, # the desired sail angle in degrees

    # Motorboat Specific:
    "vesc_telemetry_data_rpm": self.vesc_telemetry_data_rpm,
    "vesc_telemetry_data_duty_cycle": self.vesc_telemetry_data_duty_cycle,
    "vesc_telemetry_data_amp_hours": self.vesc_telemetry_data_amp_hours,
    "vesc_telemetry_data_amp_hours_charged": self.vesc_telemetry_data_amp_hours_charged,
    "vesc_telemetry_data_current_to_vesc": self.vesc_telemetry_data_current_to_vesc,
    "vesc_telemetry_data_voltage_to_motor": self.vesc_telemetry_data_voltage_to_motor,
    "vesc_telemetry_data_voltage_to_vesc": self.vesc_telemetry_data_voltage_to_vesc, 
    "vesc_telemetry_data_wattage_to_motor": self.vesc_telemetry_data_wattage_to_motor,
    "vesc_telemetry_data_time_since_vesc_startup_in_ms": self.vesc_telemetry_data_time_since_vesc_startup_in_ms,
    "vesc_telemetry_data_motor_temperature": self.vesc_telemetry_data_motor_temperature,
    "vesc_telemetry_data_vesc_temperature": self.vesc_telemetry_data_vesc_temperature


}
```



```/boat_status/get```
Accessing this route will allow you to get the current status of the boat as a dictionary.

TODO
<br>

```/boat_status/get_new```
TOD
<br>

```/boat_status/set``



This route is primarily accessed by the groundstation.
<br>
<br>


### <p style="text-align: center;"> **Autopilot Parameter Routes** </p>



```/autopilot_parameters/get```
Gets latest entry if the latest entry hasn't already been seen. If the latest entry has been seen, then simply send an empty dictionary. This helps save on LTE data since we aren't sending data to the boat if it has already seen it.


This route is primarily accessed by the telemetry node.
<br>

```/autopilot_parameters/get_new```
Gets latest entry if the latest entry hasn't already been seen. If the latest entry has been seen, then simply send an empty dictionary. This helps save on LTE data since we aren't sending data to the boat if it has already seen it.

This route is primarily accessed by the telemetry node.
<br>

```/autopilot_parameters/set```
Sets the autopilot parameters for the boat with the json thats passed to the route.


This route is primarily accessed by the groundstation
<br>
<br>



### <p style="text-align: center;"> **Waypoint Routes** </p>



```/waypoints/get```
TODO

This route is primarily accessed by the telemetry node.

<br>

```/waypoints/get_new```
TODO

This route is primarily accessed by the telemetry node.

<br>

```/waypoints/set```
TODO

This route is primarily accessed by the groundstation.

<br>

```/waypoints/set```
TODO

This route is primarily accessed by the telemetry node.

<br>
<br>