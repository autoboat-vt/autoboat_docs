# <p style="text-align: center;"> **Telemetry Server API Routes** </p>



## <p style="text-align: center;"> **How to Access and Test These Routes** </p>

If you would like to manually test some of these routes to see if they are working without having to make any extra scripts, then you should use an API tester like [Postman](https://www.youtube.com/watch?v=MFxk5BZulVU). This will allow you to specify an IP, port, route, and json payload to send the route (for the "set" routes).


<br>


You can also test all of the "get" routes by typing something like the following in a web browser, but replace "current_ip_address" with the current telemetry server IP address:

```sh
<current_ip_address>:5000/boat_status/get
```

You can do similar things with the other "get" or "get_new" routes, but this is just a small example.




## <p style="text-align: center;"> **Route Definitions** </p>


### <p style="text-align: center;"> **Boat Status Routes** </p>

The boat status has a very specific format whenever you are receiving or sending a "boat status". A boat status must be in the form of a dictionary with all of the following entries. The motorboat needs to send the entries under General and Motorboat Specific and the sailboat needs to send the entries under General and Sailboat Specific:

```json
{

    # General
    "position": [0.0, 0.0], # longitude, latitude
    "state": "WAYPOINT_MISSION", # a string that describes the autopilot mode that the boat is in. This can be Full_RC, Waypoint_Mission, Hold_Heading, etc etc. This depends heavily on how the specific autopilot sets it up though and these are just examples 
    "speed": 0.0, # speed in meters/second
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
    "vesc_telemetry_data_rpm": self.vesc_telemetry_data_rpm, # the current revolutions per minute of the motor
    "vesc_telemetry_data_duty_cycle": self.vesc_telemetry_data_duty_cycle, # the duty cycle from 0 to 1 of the motor
    "vesc_telemetry_data_amp_hours": self.vesc_telemetry_data_amp_hours, # the amount of battery life (measured in amp hours) that have been used since the VESC booted up
    "vesc_telemetry_data_amp_hours_charged": self.vesc_telemetry_data_amp_hours_charged, # the amount of battery life (measured in amp hours) that the battery still has? I am actually not too sure about this but whatever. 
    "vesc_telemetry_data_current_to_vesc": self.vesc_telemetry_data_current_to_vesc, # the average current in amps that is being transmitted to the VESC from the battery
    "vesc_telemetry_data_voltage_to_motor": self.vesc_telemetry_data_voltage_to_motor, # the average voltage in volts that is being transmitted to the motor from the VESC
    "vesc_telemetry_data_voltage_to_vesc": self.vesc_telemetry_data_voltage_to_vesc, # the average voltage in volts that is being transmitted to the VESC from the battery
    "vesc_telemetry_data_wattage_to_motor": self.vesc_telemetry_data_wattage_to_motor, # the power in watts that is being transmitted to the motor
    "vesc_telemetry_data_time_since_vesc_startup_in_ms": self.vesc_telemetry_data_time_since_vesc_startup_in_ms, # the time since the VESC has booted up
    "vesc_telemetry_data_motor_temperature": self.vesc_telemetry_data_motor_temperature, # The current temperature of the motor 
    "vesc_telemetry_data_vesc_temperature": self.vesc_telemetry_data_vesc_temperature # The current temperature of the VESC
}
```



```/boat_status/get```
Accessing this route will allow you to get the current status of the boat as a dictionary. This will be the last dictionary that has been sent to the telemetry server.

This route is primarily accessed by the groundstation
<br>


```/boat_status/get_new```
Gets latest boat status dictionary if the latest boat status hasn't already been seen. If the latest boat status has been seen, then simply send an empty dictionary. This helps save on LTE data since we aren't sending data to the groundstation it has already seen it.

This route is primarily accessed by the groundstation
<br>


```/boat_status/set``



This route is primarily accessed by the telemetry node.
<br>
<br>


### <p style="text-align: center;"> **Autopilot Parameter Routes** </p>

These autopilot parameters represent everything about the boat's behaviour that we may want to tweak from the groundstation while the boat is on the water. If we did not have autopilot parameters, then to slightly tweak some small parameters, we would need to ssh into the boat, change the code, and restart the main systemctl process.

The default autopilot parameters are primarily defined in the src/autopilot/config folder, which is what the boat uses whenever a new autopilot parameter hasn't been specified through this route. 

TODO TODO TODO


```/autopilot_parameters/get```
Accessing this route will allow you to get the autopilot_parameters of the boat as a dictionary. This will be the last dictionary that has been sent to the telemetry server.


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
Gets the current waypoint route

This route is primarily accessed by the telemetry node.

<br>

```/waypoints/get_new```
Gets latest waypoints if the latest waypoints haven't already been seen. If the latest waypoints have been seen, then simply send an empty dictionary. This helps save on LTE data since we aren't sending data to the boat if it has already seen it.


This route is primarily accessed by the telemetry node.

<br>

```/waypoints/set```
TODO

This route is primarily accessed by the groundstation.

<br>

```/waypoints/delete```
This is a deprecated route that is no longer required and is probably bad practice to use. But what it used to do was delete the last waypoint entry so that /waypoints/get would return an empty set until you set new waypoints, but this is almost always better done using /waypoints/get_new, so you shouldn't really bother with this.

<br>
<br>