# <p style="text-align: center;"> Telemetry </p>

## **Summary**
This node is responsible for listening to various topics and sending the data to the telemetry server so that we, with the groundstation, can view the data. Additionally, this node is also responsible for listening to autopilot parameters and waypoints stored in the telemetry server and sending them to the autopilot node. This allows us to change parameters of the autopilot and change the waypoints the boat needs to follow from the shore.  

The telemetry node listens to data about the boats current state such as the position, velocity, heading, apparent wind vector. It also listens in on data that lets us know what the autopilot is currently thinking such as the current sail/ rudder angle, the heading it is trying to sail towards, a list of all of the waypoints that it is trying to follow, an index that represents what waypoint the autopilot is currently on, the name of the mode the autopilot is currently on (whether it is in RC mode, full autonomy mode, or some semi-autonomous mode), and the maneuver the boat might be trying to perform if it is in full autonomous mode (like tacking/ jibing).

The telemetry node will coalesce all of this information into a single json, and send that json over to the telemetry server. The telemetry server will then pass that data along verbatim to the groundstation, so the groundstation can properly interpret that data.

The reason that this is a separate node from the autopilot nodes is that we would ideally like to have the option to run the autopilot without a wiFi connection, so if the telemetry code is in its own node, then we can just choose to not launch the telemetry node, and it should work perfectly!


If you would like more information on the telemetry node and what information it receives and how it communicates with the telemetry server/ groundstation, please see the ros system diagrams and the system diagram specifically for the groundstation/ telemetry.

<br>

## **How to Run**

```sh
ros2 run autopilot telemetry
```