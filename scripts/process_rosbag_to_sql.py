import rosbag
import sqlite3
import sys


def process_rosbag_to_sql(bag_filename):
   # Connect to the SQL database (SQLite for simplicity)
   conn = sqlite3.connect('rosbag_data.db')
   c = conn.cursor()


   # Function to create table if it doesn't exist
   def create_table(topic):
       c.execute(f"""
       CREATE TABLE IF NOT EXISTS `{topic.replace('/', '_')}` (
           timestamp REAL,
           data TEXT
       )
       """)


   # Open the rosbag
   bag = rosbag.Bag(bag_filename)


   for topic, msg, t in bag.read_messages():
       create_table(topic)
       msg_str = str(msg)
       c.execute(f"INSERT INTO `{topic.replace('/', '_')}` (timestamp, data) VALUES (?, ?)", (t.to_sec(), msg_str))


   # Commit changes and close connection
   conn.commit()
   conn.close()
   bag.close()


if __name__ == "__main__":
   if len(sys.argv) != 2:
       print("Usage: python3 process_rosbag_to_sql.py <rosbag_filename>")
       sys.exit(1)


   rosbag_filename = sys.argv[1]
   process_rosbag_to_sql(rosbag_filename)



 
