# <p style="text-align: center;"> Connecting a USB Device to WSL </p>


!!!NOTE
	If you are on Linux or Mac, USB devices should *just work* in the dev containers, so you do not need any additional steps


Sometimes, we want to test usb devices and their respective ROS nodes before we run them with the Jetson such as the GPS, RC receiver, wind sensor, Raspberry Pi Pico, VESC, etc. Most people run Windows for their personal computer, and unfortunately we have to do some slightly jank things to get everything working on windows like it would work on the Jetson. One of which is giving USB devices to WSL so that WSL can have full access to read/ write to those USB devices. Unfortunately with how WSL works, USB devices have to belong to either WSL *or* Windows, so you have to manually give access over to WSL and by default, access is given to Windows.

<br>

Back in the day, we used to have to use a command line tool called [usbipd-win](https://github.com/dorssel/usbipd-win), but to put it bluntly, this tool sucks. You have to interact with powershell, manually bind and attach specific devices, and figuring out which device is mounted to which bus were all just annoying. Nowadays, there exists a GUI called WSL USB GUI that simplifies all of the process of binding and attaching a USB device between Windows and WSL.


## **How to Install WSL USB GUI**

- Go to the following releases page for the WSL USB GUI Tool: [Link to WSL USB GUI Releases Page](https://gitlab.com/alelec/wsl-usb-gui/-/releases/).

- Click on the .msi release option for Windows:

![WSL USB GUI Releases Image](../images/wsl_usb_gui_releases.png)


**TODO TODO**