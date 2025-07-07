# <p style="text-align: center;"> Running the Simulation </p>

To run the simulation, run the following commands in order **after setting up the development container**:


```sh
sudo docker pull aanimated/autoboat_simulation:latest
```

```sh 
ros2 launch /home/ws/src/launch/simulation.launch.py
```

This command will then start the simulation and autopilot. Initially, however they won't do anything because they don't have any waypoint commands, so what you will need to do is go into your ground station folder in another terminal (not in the dev container) and type in the following command:  


```sh
cd ground_station
```

``` sh
./run.sh
```

Next, click on "zoom to boat". This should show you where the boat is currently located (likely longitude 0 and latitude 0 since this is the default location)

Now, click somewhere on the map and then click "Send Waypoints". This should cause the boat on screen to start moving and indicates that you have correctly set everything up!  
  