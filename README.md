# File Sync Test
This script synchronizes the contents of a source folder with a replica folder, ensuring the replica becomes an exact copy of the source. The synchronization happens periodically, and all file operations are logged on the console and on the file.

## Deeping in the Code 
Firstly, I implemented a parser to divide the string in arguments for the synchronization (folder paths,interval and the log file).
For the synchronization, i implemented a function sync_folders, that checked:
- The replica directory exists, if not create a directory with that name;
- Ensure the same files exists in the replica,if not copy the files from source to replica;
- If the source and replica files are identical, the function files_are_identical is called, to compare the two files;
- If the files are not identical, the replica file is updated;
- If replica directory have extra files or directories compared to source directory, the content is removed.

For the function files_are_identical, i compared the two files size and the last modification times, if the files are still identical, the function does MD5 hash comparison.
To print on the console and the selected log file, was used the setup_logging function.
