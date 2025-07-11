# <p style="text-align: center;"> Welcome to the Virginia Tech AutoBoat Documentation!</p>
This document will outline how to set up the software stack on theoretically any modern computer. All of our code is contained in [this Github repository](https://github.com/autoboat-vt), so if you want to check this out then feel free! All of the code is open source and we have a commitment to keeping all of our stuff open source for the forseable future.

<br>
## *<p style="text-align: center;"> What Is the Purpose of This Document? </p>*
The purpose of this document is to be an installation guide, overview of all of the technologies that we use, a description of how the software works, and a guide to how to use the software all in one! This is basically, in professional terms, an [ICD](https://en.wikipedia.org/wiki/Interface_control_document), and the upkeep of this document is of paramount importance as this is the best and most efficient way to facilitate knowledge transfer between senior members of the club and newer members.

<br>
## *<p style="text-align: center;"> How Do I Get Started? </p>*
Head over to the *Getting Started* part of the documentation and complete the installation steps over at *Installing Docker* to install Docker. Then, complete the installation steps found in *Setting Up the Development Container*, and once you have the development container all set up, you should be ready to test everything! To get a simple simulation scenario up and running, then please visit *Examples*. 

<br>
## *<p style="text-align: center;"> What Frameworks and Tools Should I Learn? </p>*

!!!NOTE
	**TLDR**: You should absolutely be familiar with ROS2 Humble and Git before you start working on this codebase. You may also want to learn Docker since it is extremely widely used and may be useful to know, but this is not necessary to work on the codebase.


**ROS2**: Our techstack utilizes ROS2 (The Robotics Operating System) at its core. Unlike its name implies, it is not an actual operating system, but rather a middleware wrapper that makes concurrency and communication between sensor, actuators, autopilots, and telemetry super easy! This is the industry standard for projects just like this one so if you ever want to do anything in robotics, then this is the framework to learn! The specific version we are using is ROS2 Humble Hawksbill or ROS2 Humble for short, and the documentation for it can be found right here: [ROS2 Humble Documentation](https://docs.ros.org/en/humble/index.html). Specifically, I would recommend heading to the *Tutorials* and *Concepts* sections as those are the most useful for beginners. In addition, there is a really good video series outlining how to get started and do stuff with ROS in addition to the concepts, which can be found here: [ROS2 Tutorial Series EP1](https://www.youtube.com/watch?v=0aPbWsyENA8).

**Git**: This should be fairly self explanatory, but git and github are extremely important to learn if you want to work on any codebase. Make sure you specifically understand the concepts behind and how to stage, commit, push, pull, clone, merge, resolve merge conflicts, reset to a previous commit, and setup new branches. 


**Docker**: While this isn't much of a framework, it is still an important tool and understanding how it works and the concepts behind it, will make troubleshooting if you ever run into problems a bit easier. Docker is seen pretty much everywhere in software nowadays because its a super streamlined and fast way to create custom virtual machines. It really doesn't matter which part of the software industry you would like to work in in the future, I guarantee you that you will run into docker into some point. So it's better to learn it sooner rather than later! Heres some links to documentation and videos:  
- [Docker Overview](https://docs.docker.com/guides/docker-overview/)  
- [Docker Video Explanation 1](https://www.youtube.com/watch?v=0Rq1aw8ppMk&t=216s)  
- [Docker Video Explanation 2](https://www.youtube.com/watch?v=WoZobj2Ruj0&t=313s)   

It turns out that Docker can be used for more than just deployment though. Relatively recently, Docker introduced full support for something called Docker Development Environments (Or Docker Development Containers), which allows us to do all of our development through a Docker container right inside VSCode! Thats great because getting ROS2 and our entire project working on everyone's computers and operating systems was a nightmare to orchestrate and setup, now everyone can just install Docker and our custom development container and start developing instantly! Additionally, there are plenty of other IDEs that support integration with development containers in case you use something other than VSCode; however, VSCode is what we will focus on in this document's setup instructions.
