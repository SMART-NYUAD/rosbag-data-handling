# rosbag-data-handling
Scripts for recording ROSbag data and processing it into an SQL database. Includes a shell script for recording data from ROS topics and a Python script for storing the data in an SQL database.

### Recording ROSbag Data
1. Navigate to the `scripts` directory:
    ```sh
    cd scripts
    ```

2. Run the `record_rosbag.sh` script with the desired ROSbag name:
    ```sh
    ./record_rosbag.sh [rosbag_name]
    ```
    (Note: The extension is not necessary)

### Processing ROSbag Data into SQL
The `record_rosbag.sh` script automatically calls the `process_rosbag_to_sql.py` script after recording the data.

### Customizing Recording Settings
You can tweak the recording settings such as size, split, or topics in the `record_rosbag.sh` file.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
