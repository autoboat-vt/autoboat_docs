# <p style="text-align: center;"> **How to Start Developing on the Telemetry Server** </p>


## <p style="text-align: center;"> **Installing the Correct Version of Python** </p>


We will assume that if you are Windows, you already have WSL installed. If you are on Windows, then development on the telemetry server will be done on WSL exclusively. We will also assume that you have python version 3.9 installed. If you do not know which python version you currently have then please run the following command:

```sh
python --version
```

If the version is incorrect or the command gives you an error because python is not found, then you will need to install the correct version of python. The easiest way to do this is probably through miniconda which is a tool that allows you to manage multiple different versions of python on the same computer very easily.

To install miniconda, please follow the installation instructions found here: [Miniconda installation instructions](https://www.anaconda.com/docs/getting-started/miniconda/install).

!!!Note "Windows Users"
    If you are on Windows, then make sure that you do this installation for linux in your WSL environment. We would like to develop the telemetry server using a unix environment because it makes everything a whole lot easier, so you need to install the correct version of python through WSL linux.

Once your installation is done and you open up a terminal, then if you run the following command:

```sh
conda activate base
```

Once you right that, you should see the word "(base)" right next to your terminal which means that conda is activated and is correctly installed. In order to install the correct version of python now, please run the following command:

```sh
conda install python=3.9
```



## <p style="text-align: center;"> **Downloading the Codebase for the Telemetry Server** </p>

!!!Note "Windows Users"
    Ensure that you are running the following commands in a WSL terminal in a WSL linux filesystem. If you would like to navigate to your linux filesystem from the WSL terminal then run the following command: `cd ~`, which will take you to the home directory for the linux filesystem. If you do not install this in the linux filesystem, then developing the telemetry server will be noticably laggier.

Run the following commands:

```sh
conda activate base
git clone https://github.com/autoboat-vt/telemetry_server
cd telemetry_server
pip install -r requirements.txt
```

!!!Note "Make Sure You Have Conda Activated When Developing"
    If you do not see the word "(base)" next to your terminal, then conda is not activated and in order to use the correct version of python, you need to make sure you run `conda activate base` before you start running programs.

