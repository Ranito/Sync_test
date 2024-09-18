import logging

def setup_logging(log_file):
   
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(message)s",
        filemode='a'
    )
    
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)

