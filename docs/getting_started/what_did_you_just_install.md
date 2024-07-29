
# <p style="text-align: center;"> What is Docker and How Does it Work? </p>

Docker is essentially a way to share custom (super fast) virtual machines. A Dockerfile is the instructions to create these virtual machines. These are then compiled into Docker Images which are the virtual machines stopped at whatever point the Dockerfile told it to stop at. When you run a Docker Image, you get a Docker Container. A Docker Container is the actual virtual machine that you can interact with and work with.  

<br>

# <p style="text-align: center;"> What is a Development Container and Why are We Using One? </p>

A Development Container is a just a Docker Container that already has all of the requirements to start developing, so you can skip setup and not worry about operating system specific software. There are a lot of software packages we rely on and some of the software that we use only works on certain versions on Ubuntu and is really hard to get your hands on with other operating systems. Docker Development Containers automate the process of installing everything by creating a Docker Image with everything installed and running that. This allows you to start developing instantely! Additionally this helps automate and streamline deployment on the Nvidia Jetson microprocessor.

<br>

# <p style="text-align: center;"> What About the Ground Station? </p>

This code is supposed to be run on an operator's computer to control the boat while it is on the water by telling a cloud server what we want our boat to do. The boat (specifically the telemetry node) then listens to this cloud server, processes the data, and performs whatever action we told it to do. You can do various things like sending different parameters to the autopilot and sending waypoints. These parameters can look like the PID gains or the tacking distance or the size of the no go zone etc (in other words things that were chosen arbitrarily).

You can also use the ground station code to control the simulation, so if you send waypoints or parameters while a simulation is running then the simulation will automatically listen to the cloud server and navigate to those waypoints/ change specific parameters.

As of right now the code is kind of a mess and the visualization barely works (one of the big things we are trying to do is have an actual ground station app ready by this year's competition)
The primary files you should care about in the groundstation are the following files: desired_parameters.json, desired_waypoints.json, send_desired_parameters_and_waypoints.py, and main.py (although main.py is kind of a mess right now).

The essential functionality is that send_desired_parameters_and_waypoints.py just sends the data from desired_parameters.json and desired_waypoints.json and you can edit those based on what you want to change. Waypoints are simply supplied as a list of [latitude, longitude] (TODO maybe add a picture here). The list of parameters that you can change are found in the autopilot node here: config/default_parameters.yaml

For more information on how the ground station sends parameters, please see the resources section of the documentation.
