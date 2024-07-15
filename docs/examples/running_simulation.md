# Running the Simulation  

To run the simulation, all you need to do is run the following command:

`ros2 launch /home/ws/src/launch/simulation.launch.py`

This command will then start the simulation and autopilot. Initially, however they won't do anything because they don't have any waypoint commands, so what you will need to do is go into your ground station folder in another terminal (not in the dev container) and type in the following command:  

`python send_desired_parameters_and_waypoints.py`

Doing this should make the boat in the visualization move around the pop up screen!  

The boat might be kind of slow though, so be sure to go check out how to run a custom simulation in the examples. With the custom simulations we can accelerate the speed of the simulation by a landslide!