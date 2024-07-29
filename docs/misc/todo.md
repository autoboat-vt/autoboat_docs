# <p style="text-align: center;"> TODO </p>

We use todoist to manage all of our current projects and planning. 
If you would like to see what we are currently working on then please visit the following link

## Add the following aliases if they help:
- alias python=python3
- alias 'colcon build'='cd /home/ws && colcon build'

Maybe also add mount /usr/bin/docker `-v "/usr/bin/docker:/usr/bin/docker"` onto the dev container. 
The main problem is that apparently on mac the place where the docker binary is is actually /usr/local/bin/docker so we would have to make a special case for mac at build time
