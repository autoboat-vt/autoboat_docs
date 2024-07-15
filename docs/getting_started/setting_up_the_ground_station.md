# <p style="text-align: center;"> Setting Up the Ground Station </p>
 
The ground station is the main way to give the boat (or simulation) waypoint commands and autopilot parameters.  

!!!NOTE "NOTE: Do not Install in the Docker Development Container for Now"
    Please do not install this or the other repositories in the docker development container. Currently the development container is only meant for the ros workspace, however technically in the future we could have it support all of our repositories in a nice way. This just isn't supported at the moment and will be very annoying if you eventually try to push code back to our github

In order to use the code you need to open up a WSL terminal and type the following in a directory you would like to have this in:  
``` sh
git clone https://github.com/sailbot-vt/ground_station
cd ground_station
pip install -r requirements.txt 
```

This will install all of the requirements for the ground station code into your computer. We aren't currently using the Docker Dev Environment for this but technically you could do this in your Docker Dev Environment if you wanted.

!!!NOTE "NOTE: Groundstation Code Has Mostly Only Been Tested for Python 3.10"
    Most of this code has been tested for python 3.10, so if you have an issue on another version of python please let an officer know although there aren't many reasons why the code wouldn't work on other versions unless they are very old versions of python (like before python 3.7).
