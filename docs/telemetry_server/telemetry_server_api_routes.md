## <p style="text-align: center;"> **Telemetry Server API Routes** </p>


label certain routes as specifically used by the groundstation or specifically used by the telemetry node


## <p style="text-align: center;"> **How to Access and Test These Routes** </p>



## **Route Definitions**

```/boat_status/get```
This route is primarily accessed by the groundstation.

TODO
<br>

```/boat_status/get_new```
TODO
<br>

```/boat_status/set``
This route is primarily accessed by the groundstation.
`
TODO
<br>
<br>




```/autopilot_parameters/get```
Gets latest entry if the latest entry hasn't already been seen. If the latest entry has been seen, then simply send an empty dictionary. This helps save on LTE data since we aren't sending data to the boat if it has already seen it.


This route is primarily accessed by the telemetry node.
<br>

```/autopilot_parameters/get_new```
Gets latest entry if the latest entry hasn't already been seen. If the latest entry has been seen, then simply send an empty dictionary. This helps save on LTE data since we aren't sending data to the boat if it has already seen it.

This route is primarily accessed by the telemetry node.
<br>

```/autopilot_parameters/set```
This route is primarily accessed by the groundstation

Sets the autopilot parameters 

<br>
<br>




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