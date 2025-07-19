# <p style="text-align: center;"> **Telemetry Server API Routes** </p>



## <p style="text-align: center;"> **How to Access and Test These Routes** </p>

If you would like to manually test some of these routes to see if they are working without having to make any extra scripts, then you should use an API tester like [Postman](https://www.youtube.com/watch?v=MFxk5BZulVU). This will allow you to specify an IP, port, route, and json payload to send the route (for the "set" routes).


<br>


You can also test all of the "get" routes by typing something like the following in a web browser, but replace "current_ip_address" with the current telemetry server IP address:

```sh
<current_ip_address>:5000/boat_status/get
```

You can do similar things with the other "get" or "get_new" routes, but this is just a small example. We wouldn't be able to do this for any of the "set" routes because you can't really send a json payload through just your browser, and you would have to use an external tool.





## <p style="text-align: center;"> **Route Definitions** </p>


### <p style="text-align: center;"> **Boat Status Routes** </p>

The boat status contains all of the useful telemetry that we can receive from the boat to understand what the boat is thinking. This can include sensor readings, state variables, or any other thing that would be useful to display to the user in real time. This relatively large JSON is being sent back and forth constantely, and if you want to reduce the LTE data that the boat is using, this would be the main place to focus on and optimize.

The boat status has a very specific format whenever you are receiving or sending a "boat status". A boat status must be in the form of a dictionary with all of the following entries. This all must be wrapped in a "value" dictionary specifically because we need to be able to send the waypoints (a list) over json, and I wanted the format to be consistent among every route. We can change this in the future, the "value" dictionary was really just a bad decision that I just rolled with honestly. The motorboat needs to send the entries under General and Motorboat Specific and the sailboat needs to send the entries under General and Sailboat Specific:

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


------------------------------------------------------------------------

```/boat_status/get```
Accessing this route will allow you to get the current status of the boat as a dictionary. This will be the last dictionary that has been sent to the telemetry server.

This route is primarily accessed by the groundstation


------------------------------------------------------------------------

<br>




```/boat_status/get_new```
Gets latest boat status dictionary if the latest boat status hasn't already been seen. If the latest boat status has been seen, then simply send an empty dictionary. This helps save on LTE data since we aren't sending data to the groundstation it has already seen it.

This route is primarily accessed by the groundstation


------------------------------------------------------------------------

<br>




```/boat_status/set``
Sets the boat status of the boat with the JSON thats passed to the route as a JSON payload.

This route is primarily accessed by the telemetry node on the Jetson on the boat

------------------------------------------------------------------------

<br>

<br>




### <p style="text-align: center;"> **Autopilot Parameter Routes** </p>

These autopilot parameters represent everything about the boat's behaviour that we may want to tweak from the groundstation while the boat is on the water. If we did not have autopilot parameters, then to slightly tweak some small parameters, we would need to ssh into the boat, change the code, and restart the main systemctl process.

The default autopilot parameters are primarily defined in the src/autopilot/autopilot/config folder, which is what the boat uses whenever a new autopilot parameter hasn't been specified through this route. The following is what a JSON message to the telemetry server would look like if you would like to set new parameters:

```json
{
    "sail_lookup_table_wind_angles":    [0,    45,   90,   135,   180,   225,   270,   315,   360],
    "sail_lookup_table_sail_positions": [70.0, 50.0, 30.0, 10.0,  0.0,   10.0,  30.0,  50.0,  70.0],

    "perform_forced_jibe_instead_of_tack": true,
    "waypoint_accuracy": 5,
    "tack_distance": 100 
}
```

This JSON will only contain the parameters that you would like to change, and you can only change the parameters that exist in the src/autopilot/autopilot/config folder. If you are reading parameters off of the /autopilot_parameters/get route, then you will receive all of the parameters including the ones that the groundstation has not manually changed. If you are reading parameters off of the /autopilot_parameters/get_new route, then you will only receive the parameters that have most recently changed (if they have not already been read already). No matter which route you are pulling the parameters off of, however, the format will be pretty much identical.

------------------------------------------------------------------------


```/autopilot_parameters/get```
Accessing this route will allow you to get all of the parameters that the boat is currently using. This is useful if on the groundstation you would like to pull all of the parameters that the boat is currently using so that you can show the user what the boat is thinking. You can also use this as a more data intensive version of /autopilot_parameters/get_new on the telemetry node.


This route can be accessed by either the groundstation or the telemetry node on the Jetson on the boat

------------------------------------------------------------------------

<br>




```/autopilot_parameters/get_new```
Accessing this route will allow you to get the autopilot_parameters of the boat as a dictionary. This will be equivalent to the last JSON that has been sent to the telemetry server through the /autopilot_parameters/set route if it has not already been read. If the /autopilot_parameters/get_new route has already been read from and no new autopilot parameters were set, then this route will just return an empty JSON to save on LTE data.

This route is primarily accessed by the telemetry node on the Jetson on the boat

------------------------------------------------------------------------

<br>



```/autopilot_parameters/set```
Sets the autopilot parameters for the boat with the JSON thats passed to the route. You can send a JSON with just one autopilot parameter that you would like to change or you can change all of the autopilot_parameters at once. It is up to you.


This route is primarily accessed by the groundstation

------------------------------------------------------------------------

<br>



```/autopilot_parameters/set_default```
Sets the default parameters that the telemetry node is using. These are the same parameters that are in the src/autopilot/autopilot/config folder and should only be set once while the telemetry node is booting up and gives the telemetry server and the groundstation an idea of what parameters the boat is using if you haven't manually set certain parameters. This also tells you which parameters that you can set via /autopilot_parameters/set, since you can't add any other parameters other than the default parameters.

This route is primarily accessed by the telemetry node on the Jetson on the boat

------------------------------------------------------------------------

<br>


```/autopilot_parameters/get_default```
Views the default parameters that the telemetry node has been using. This is the same JSON as the JSON sent by the /autopilot_parameters/set_default route.

This route is primarily accessed by the groundstation

------------------------------------------------------------------------

<br>
<br>





### <p style="text-align: center;"> **Waypoint Routes** </p>

This route is how we send waypoints to the boat from the groundstation. Once the boat receives the waypoints, it will attempt to capture those waypoints in order. Capturing a waypoint means that the boat has gotten a certain amount of meters away from the waypoint; the exact number of meters away from the waypoint the boat has to be is defined in the "waypoint_accuracy" autopilot parameter. If the boat is sent another waypoint while it still hasn't finished its current mission, then it will abandon its previous route and start again at waypoint 1 on the route it was just sent. 

```json
{
    "waypoints": [
        [0.1221313, 0.21312],    # latitude, longitude of waypoint 1
        [0.3213121, -0.313111],    # latitude, longitude of waypoint 2
        # .... etc etc
    ]
}
```

------------------------------------------------------------------------



```/waypoints/get```
Gets the current waypoint route that the boat should be currently trying to follow. This would be the same JSON as the last JSON that has been sent by the /waypoints/set route.

This route is primarily accessed by the telemetry node on the Jetson on the boat via a GET request.

------------------------------------------------------------------------


<br>



```/waypoints/get_new```
Gets latest waypoints if the latest waypoints haven't already been seen. If the latest waypoints have been seen, then simply send an empty dictionary. This helps save on LTE data since we aren't sending data to the boat if it has already seen it.


This route is primarily accessed by the telemetry node on the Jetson on the boat via a GET request.

------------------------------------------------------------------------


<br>



```/waypoints/set```
Sets the waypoints via a JSON payload. Make sure that you use the format provided above for the JSON that you send to the telemetry server or else the boat/ the telemetry node will not understand what to do.

This route is primarily accessed by the groundstation as a POST request.

------------------------------------------------------------------------

<br>


```/waypoints/delete```
This is a deprecated route that is no longer required and is probably bad practice to use. But what it used to do was delete the last waypoint entry so that /waypoints/get would return an empty set until you set new waypoints, but this is almost always better done using /waypoints/get_new, so you shouldn't really bother with this.

This route would be accessed via a POST request.
<br>
<br>



## <p style="text-align: center;"> **FAQ** </p>

### <p style="text-align: center;"> **I am still confused about the get_new routes** </p>

This is likely best explained with an example: If you set the waypoints once from the groundstation, then those waypoints get stored in the telemetry server. How we have it set up right now, the telemetry node will constantly poll every 0.5 seconds for the new waypoints. You can imagine that if we are always sending back a large list of data, that would eat up our LTE data and cost us more money, so to optimize that, we would only like to send the waypoints to the telemetry node if there is something new for it to see. If there isnt, then we should just send an empty JSON because that uses the least amount of LTE data.

The autopilot parameters are slightly different because we have 1 extra distinction when using get vs get_new for the autopilot parameters. When using get on the autopilot parameters, it will send all of the parameters regardless of if they were changed in the last call to set. However, if you use get_new it will only return the JSON payload in the last call to "set" and if you access it more than once, it will send over an empty JSON.
