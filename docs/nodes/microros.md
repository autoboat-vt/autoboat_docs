# <p style="text-align: center;"> Microros </p>

This is the main package for MicroROS development. Due to the nature of microcontrollers, only one package can be run on a Pi Pico. However, there are few limitations as to how many nodes can be run. Since the RP2040 chip installed on Pi Pico has two cores, we can even run some of the nodes in parallel, taking full advantage of multithreading. All of the nodes will be documented in this file. To get started with microros development, check out **Installing MicroROS** in **misc**.

All the nodes, their common resources, execution order, and scheduling are managed in the main.c file in the src folder. If you want to add a .c file with a node, as well as in add_executable section in CMakeLists.txt. Depends on if you include new libraries you might want to add them in CMakeLists.txt too. Important libraries and ports are located in common_microros_libs.h, which is preferable to include in each file within src folder. If you need to define ports or pins, UART for example, you do it there.
To build an already existing project, execute the following commands inside `/microros/` (not `/microros/src/`):
```sh
    mkdir build && cd build
    cmake ..
    make
```
From here on, after making changes to the code, you can build it simply by running `make`. Next steps, such as opening communication with ROS or flashing Pico are detailed in **Installing MicroROS**. 

# <p style="text-align: center;"> sensor_transmission </p>
The node that obtains data from the VESC and the magnetometer and publishes it for Jetson to see. Uses another file called magnetometer_read.c to read I2C data. Runs on core0. Currently partially implemented.

# <p style="text-align: center;"> sail_control </p>
The node that implements PID control for the sail stepper motor. Intended to run on core0. Currently unimplemented.

# <p style="text-align: center;"> rudder_control </p>
The node that implements PID control for the rudder stepper motor. Intended to run on core1. Currently unimplemented.

# <p style="text-align: center;"> manual_mode </p>
The node that implements RC control of the boat. Intended to run on core1. Currently unimplemented.
