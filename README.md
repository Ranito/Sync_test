# File Sync Test
This script synchronizes the contents of a source folder with a replica folder, ensuring the replica becomes an exact copy of the source. 
The synchronization happens periodically, and all file operations are logged both in the console and in a specified log file.

## Deeping in the Code 
First, I implemented a parser to handle the arguments for synchronization (folder paths, interval, and log file location).

For the synchronization, i implemented a function ```sync_folders```, that checked:
- The replica directory exists, if not create a directory with that name;
- Ensure the same files exists in the replica,if not copy the files from source to replica;
- If the source and replica files are identical, the function files_are_identical is called, to compare the two files;
- If the files are not identical, the replica file is updated;
- If replica directory have extra files or directories compared to source directory, the content is removed.

For the ```files_are_identical function```, the comparison is made by checking file size and last modification time. If the files are still considered identical after this check, an MD5 hash comparison is performed to confirm they are the same.

## Code Execution

The python version is 3.12.5.

To run the code type these command:

```bash
python main.py ./Source ./Replica 30 ./Log_File
```
The ./Source and ./Replica are the folder paths; 30 is the time interval between synchronizations in seconds, and ./Log_File is log file path, where the name can be changed.
