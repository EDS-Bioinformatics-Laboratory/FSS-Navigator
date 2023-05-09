# Parse Directory



**Short project description**

The aim is to develop a Python program that parses a specific directory and writes a html file to easily navigate the directory structure and inspect the files that are in there.

This Python script should become part of CORE to navigate the File System Structure (FSS)



**Date:** 8 May 2023

**Your Name:** Prof. dr. Antoine van Kampen

**Operating System(s) / version(s) used during development: ** Windows 11

**Specific hardware requirements:** None

**Software environment:** Python 3 / Anaconda





------

**RUNNING THE SOFTWARE**

------

To test the Python program:

1. specify the correct **FSSPath** in the Python file \20230508_ParseDirectory\Processing\20230508_ParseDirectory\Code\\**ParseDirectory_v1.py**. 

2. Execute the full script to write **Navigation.html** in \20230508_ParseDirectory\Processing\20230508_ParseDirectory\\**Results**

3. Open Navigation.html in your browser





------

**CONFIGURING NAVIGATION**

------

In the Python program \\**ParseDirectory_v1.py** you can currently specify which files and subdirectories to include/exclude. 



------

**WARNING** 

------



* If the structure of the FSS changes in the future then it may be necessary to update the paths in the Python program.
* The Python program assumes a strict naming of the pre-defined files in the FSS according as outlined in the usage rules of the FSS.



------

**PYTHON PROGRAMS**

------



\20230508_ParseDirectory\Processing\20230508_ParseDirectory\Code\\**ParseDirectory_v1.py**

This Python program parses a complete File System Structure (FSS) starting from its root. 

The final navigation file **Navigation.html** that is produced by this script is written to \20230508_ParseDirectory\Processing\20230508_ParseDirectory\Results\Navigation.html

This navigation file is a copy of the **navigation-template.html** in the \20230508_ParseDirectory\Processing\20230508_ParseDirectory\Results\\**.navigate** directory. This template defines four iframes that hold all content of the FSS.

The files required to navigate the FSS are also written to the **\.navigate** directory:

* 0_gettingstarted.html (copied from 0_GETTINGSTARTED.html in the root of the FSS)
* 0_project.html (copied from 0_PROJECT.md in the root of the FSS)
* fss.html the directory structure of the FSS and relevant files



**Note**: this script is used for development and testing



------

For the final Python script that can be used with the current FSS template two changes need to be made:

* The paths in the Python program should be changed
* The FSSPath should become a command line argument to the compiled program instead of being specified in the Python file itself.
* The configuration options should also be moved out of the Python program itself
* The directory **\.navigate** should be moved to the root of the FSS

------



