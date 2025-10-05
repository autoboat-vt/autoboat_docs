# <p style="text-align: center;">Object Detection</p>

## Summary

This node detects **buoys** and **boats** on the water and estimates their **bearing (angle)** and **range (distance)**.  
Detection is powered by an Ultralytics **YOLOv11** model. We use the
[Ultralytics `results` object](https://docs.ultralytics.com/modes/predict/#working-with-results)
to retrieve bounding boxes, classes, and confidences.

The node runs on **ROS 2** and publishes:
- **Bearing to target (angle)** — relative to the camera/boat frame.
- **Range to target (depth distance)** — from depth data or geometric approximation.
- **Per-detection metadata** — confidence score, relative x/y of the bounding box, etc.

### What it publishes
- `sensor_msgs/msg/Image`
- `sailbot_msgs/msg/ObjectDetectionResults`
  - `detections[]`: `{ confidence value, x_postion, y_position}`
  

> QoS is configurable via `QoSProfile` and should be tuned to match the camera publisher
> (e.g., `RELIABLE` vs `BEST_EFFORT`, `KEEP_LAST` depth, etc.).

<br/>

## Repository (Models & Dataset)

The code, models, and dataset live on Hugging Face (handles large files better than GitHub):

**Object Detection – Hugging Face Repository:**  
[https://huggingface.co/datasets/Aanimated/autoboat_vt_object_detection/tree/main](https://huggingface.co/datasets/Aanimated/autoboat_vt_object_detection/tree/main)

> We use a Hugging Face *dataset repo* because it supports large images and model weights via Git LFS.  
> You can clone it and pull all LFS-tracked files locally.

### Quick start
```bash
# Install Git LFS, clone, and pull large files
sudo apt update && sudo apt install -y git-lfs
git lfs install

git clone https://huggingface.co/datasets/Aanimated/autoboat_vt_object_detection
cd autoboat_vt_object_detection
git lfs pull
```