# <p style="text-align: center;"> What is Systemctl?</p>

Systemctl is essentially a way to schedule scripts to run when a machine starts up, and this is super useful on the Jetson on the actual boat, because it allows us to start up the autopilot ROS nodes without SSH'ing into the Jetson all of the time. Before we started using systemctl, every single time we power cycled the boat, we would have to SSH into the boat and manually run `ros2 launch ......`, but now with systemctl, this command automatically runs for us everytime the boat starts up.



## <p style="text-align: center;"> Some Useful Stuff to Know How to Do in Systemctl</p>

Theres a whole bunch of things that are very useful to know how to do with systemctl processes. For example, how to create a new .service file, how to use `sudo systemctl enable myservice` (which enables the service to start on boot), how to use `sudo systemctl start myservice` (which starts the service right now), how to use `sudo systemctl stop myservice` (which stops the service from running right now), `sudo systemctl disable myservice` (which disables the service to start on boot), and `sudo journalctl -u myservice` (which shows you the print logs from a specific service).



## <p style="text-align: center;"> Example of a Systemctl File That We Have Used</p>
TODO TODO TODO TODO



## <p style="text-align: center;"> Extra Resources to Learn More About Systemctl</p>


Making a new systemctl process: https://askubuntu.com/questions/919054/how-do-i-run-a-single-command-at-startup-using-systemd

Using journalctl: https://www.digitalocean.com/community/tutorials/how-to-use-journalctl-to-view-and-manipulate-systemd-logs 