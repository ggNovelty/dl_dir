## dl\_dir.py

A Python3 script to download from open web directories.
Downloads any files with a detected 3 or 4 character extension.
Crawls sub-directories, but should not visit parent directories. 
Attempts to copy folder structure of the entire directory.

More powerful tools than this one certainly exist, but I wanted to try making my own.
May not work on all directories, needs more testing.

#To use:

* `cd` to the directory where this script is saved.

* Type `python3 dl_dir.py` into your terminal.

* When prompted, enter the url of the desired web directory.

* A new folder will be created within the current directory, with the contents of the web directory saved within it.
