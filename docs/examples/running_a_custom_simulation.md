# Running A Custom Simulation


!!!NOTE "NOTE: Do Not Clone the Code into Your Docker Development Environment"
    Make sure you clone this repository outside of the docker development environment, because Docker gets a little fussy with building Docker images inside of a Docker Container, and I would rather not have to deal with that. If you are on windows, this means that you should do the rest of the setup steps in WSL.


Before we can build a custom simulation, first we need to clone the sailbot_simulation repository.

Open up a terminal in the folder you would like to place the code to build a new simulation in. Next type the following commands:

------

```
git clone https://github.com/sailbot-vt/sailbot_simulation 
cd sailbot_simulation
```

------


Now that you have all of the code on your computer, there is only 1 dependency for working with the simulation and that is docker-buildx. You can install it like this on Windows WSL and Ubuntu:

-----

```
sudo apt install docker-buildx
```

-----  



Now, all you have to do to build the simulation now is type in the following command:

-----

```
sudo bash build_sim.sh
```

-----


And thats it! Now automatically, the simulation node will instead use the new, custom simulation instead of the default. The simulation itself is quite poorly documented so if you have any questions about it and how to do certain things, please ask Chris.

If you would like to go back to using the default simulation then all you have to do is delete the simulation docker image and by default, the simulation node will pull the default simulation image and build it. 