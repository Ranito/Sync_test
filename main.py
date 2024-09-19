import argparse
import time
from sync import sync_folders
from logger import setup_logging


def main():
    
    parser = argparse.ArgumentParser(description="Sync two folders.")
    parser.add_argument("source", help="Path to the source folder")
    parser.add_argument("replica", help="Path to the replica folder")
    parser.add_argument("interval", type=int, help="Sync interval in seconds")
    parser.add_argument("log_file", help="Path to the log file")

    sync_file = parser.parse_args()

    setup_logging(sync_file.log_file)

    while True:
        sync_folders(sync_file.source, sync_file.replica)  
        
        time.sleep(sync_file.interval)  

if __name__ == "__main__":
    
    main()
