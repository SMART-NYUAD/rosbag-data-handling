#!/bin/bash


# Check if a filename was provided
if [ -z "$1" ]; then
 echo "Please provide a filename for the rosbag."
 exit 1
fi


FILENAME="$1.bag"


# Record the rosbag with the specified filename
rosbag record /robot/os_cloud_node/imu /robot/os_cloud_node/points /robot/os_cloud_node/scan /robot/front_rgbd_camera/rgb/image_raw/compressed /robot/os_cloud_node/scan_filtered /robot/front_rgbd_camera/rgb/image_raw/compressedDepth /robot/front_rgbd_camera/ir/image /robot/front_rgbd_camera/ir/image/compressed /robot/front_rgbd_camera/depth_registered/points /robot/front_laser/scan /robot/front_laser/scan_filtered /robot/battery_estimator/data_stamped /robot/battery_estimator/data /robot/robotnik_base_hw/voltage /robot/robotnik_base_hw/state /robot/mavros/imu/static_pressure /robot/mavros/imu/data /robot/mavros/altitude --size=20400 —split -O $FILENAME


# Run the Python script to process the rosbag data into SQL database
python3 process_rosbag_to_sql.py $FILENAME
