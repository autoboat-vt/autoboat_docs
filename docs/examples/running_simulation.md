# <p style="text-align: center;"> Running the Simulation </p>

To run the simulation, run the following commands in order **after setting up the development container**:


```sh
sudo docker pull autoboatvt/autoboat_simulation:latest
```

This command will pull the simulation docker image, which is where all of the simulation work is actually taking place! **This command only needs to be run once. Once the docker image has been pulled, you shouldn't need to repull**. The command may take a while, but once it is finished, run the following command:

```sh 
ros2 launch /home/ws/src/launch/simulation.launch.py
```

This command will then start the simulation and autopilot. Initially, however they won't do anything because they don't have any waypoint commands, so what you will need to do is to type in the following command:  


```sh
cd /home/ws/ground_station
```

``` sh
./run.sh
```

Next, click on "zoom to boat". This should show you where the boat is currently located (likely longitude 0 and latitude 0 since this is the default location)

Now, click somewhere on the map and then click "Send Waypoints". This should cause the boat on screen to start moving and indicates that you have correctly set everything up!  
  