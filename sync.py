import os
import shutil
from file import files_are_identical
import logging


def sync_folders(source, replica):
  
    try:
        
        if not os.path.exists(replica):
            os.makedirs(replica)
            logging.info(f"Created replica directory: {replica}")
        
        
        for root, dirs, files in os.walk(source):
            rel_path = os.path.relpath(root, source)  
            replica_root = os.path.join(replica, rel_path)  

            
            for dir_ in dirs:
                replica_dir = os.path.join(replica_root, dir_)
                if not os.path.exists(replica_dir):
                    os.makedirs(replica_dir)  
                    logging.info(f"Created directory: {replica_dir}")

            
            for file_ in files:
                source_file = os.path.join(root, file_)
                replica_file = os.path.join(replica_root, file_)

                if not os.path.exists(replica_file):
                    
                    shutil.copy2(source_file, replica_file)
                    logging.info(f"Copied file: {source_file} to {replica_file}")
                else:
                    
                    if not files_are_identical(source_file, replica_file):
                        
                        shutil.copy2(source_file, replica_file)
                        logging.info(f"Updated file: {source_file} to {replica_file}")

        
        for root, dirs, files in os.walk(replica):
            rel_path = os.path.relpath(root, replica)  
            source_root = os.path.join(source, rel_path)  

            
            for file_ in files:
                replica_file = os.path.join(root, file_)
                source_file = os.path.join(source_root, file_)
                if not os.path.exists(source_file):
                    os.remove(replica_file)  
                    logging.info(f"Removed file: {replica_file}")

            
            for dir_ in dirs:
                replica_dir = os.path.join(root, dir_)
                source_dir = os.path.join(source_root, dir_)
                if not os.path.exists(source_dir):
                    shutil.rmtree(replica_dir)  
                    logging.info(f"Removed directory: {replica_dir}")
    
    except Exception as e:
        logging.error(f"Error on synchronizing folders: {e}")
        raise
