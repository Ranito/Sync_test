import os
import hashlib
import logging


def hash_file(filepath, chunk_size=8192):
    
    hash_md5 = hashlib.md5()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(chunk_size), b""):
                hash_md5.update(chunk)
        return hash_md5.hexdigest()
    
    except Exception as e:
        logging.error(f"Failed hash file {filepath}: {e}")
        return None


def files_are_identical(source_file, replica_file):

    try:
        
        if os.path.getsize(source_file) != os.path.getsize(replica_file):
            return False
        
        if os.path.getmtime(source_file) != os.path.getmtime(replica_file):
            return False
       
        return hash_file(source_file) == hash_file(replica_file)
    
    except Exception as e:
        
        logging.error(f"Error on comparing {source_file} with {replica_file}: {e}")
        return False
