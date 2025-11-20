# <p style="text-align: center"> Before Installing Deepstream </p>

Make sure that you have set up the dev container prior to attempting install.

!!!NOTE "General"
    In order to run inference, an NVIDIA 30x series GPU or newer is required.
    
    This will not work on macOS and ARM systems.

# <p style="text-align: center"> Installing Deepstream </p>

Inside the dev container, make sure your current working directory is `/home/ws/`.

Execute this script to start the installation.

```sh
bash install_deepstream_yolo_dev_container.sh
```

This installation can take a long time.

# <p style="text-align: center"> Connecting the Camera </p>

In order to run the object detection module, the Intel RealSense D457 camera must be connected and forwarded to WSL

To forward the camera device to WSL, a GUI can be used like [WSL USB](https://gitlab.com/alelec/wsl-usb-gui) or [these instructions](https://learn.microsoft.com/en-us/windows/wsl/connect-usb) can be followed in Windows Powershell.

!!!Note "Making sure the camera is seen in WSL"
    To verify the connection, run this command in the dev container
    
    ```sh
    v4l2-ctl --list-devices
    ```

    A properly connected camera will have an output similar to this (the numbers may be different)

    ```sh
    autoboat_user@docker-desktop:/home/ws$ v4l2-ctl --list-devices
    Intel(R) RealSense(TM) Depth Ca (usb-0000:00:14.0-1):
            /dev/video0
            /dev/video1
            /dev/video2
            /dev/video3
            /dev/video4
            /dev/video5
            /dev/media1
            /dev/media2
    ```

# <p style="text-align: center"> Building a Model </p>

To build a model, navigate to the deepstream_yolo directory. This can be done without a camera connected.

```sh
cd /home/ws/src/object_detection/object_detection/deepstream_yolo/
```

Place the .pt model file in this directory.

Run this script to build a .engine model file based on the .pt file. This will take a while.

```sh
bash build_engine_file.sh <name_of_pt_file>
```

!!!NOTE "What this does"
    In order, what this script does is:

    1. Convert .pt file to .onnx

    2. Modify `config_infer_primary_yolo11.txt` to point to the created .onnx file

    3. Create the .engine file

!!!NOTE "Alternative option"
    This can be split up into separate steps and manually completed

    1. Run `python export_yolo11_dev_container.py <name_of_pt_file>`

    2. Manually modify `config_infer_primary_yolo11.txt`.

        Comment out lines by adding a '#' in the front.

    3. Run `python make_model_engine.py`

!!!NOTE "labels.txt"
    The `labels.txt` file is used to tell the vision pipeline what class is which. This is purely a label, and it does not matter if certain classes are missing labels (they will be labeled NULL)

    In creating the .onnx file, this labels.txt file will be overwritten based on the classes in the model. For most models that we'll make, this probably does not matter.

# <p style="text-align: center"> Running the Object Detection Module </p>

After a model file has been created, you can run the ROS2 object detection module.

```sh
ros2 run object_detection object_detection
```

Annotated images will be saved to `/home/ws/src/object_detection/object_detection/frame_results/`

!!!NOTE "Running without inference"
    The steps to build an engine file can be skipped if inference is not required

    To do this, set this environment variable before running the module
    
    ```sh
    export INFERENCE=false
    ```