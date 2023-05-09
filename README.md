# Parse Directory



**Short project description**

The aim is to develop a Python program that parses a specific directory and writes a html file to easily navigate the directory structure and inspect the files that are in there.

This Python script should become part of CORE to navigate the File System Structure (FSS)



**Date:** 9 May 2023

**Your Name:** Prof. dr. Antoine van Kampen

**Operating System(s) / version(s) used during development: ** Windows 11

**Specific hardware requirements:** None

**Software environment:** Python 3 / Anaconda





------

**FILES**

------

* ParseDirectory_v1.py   (can be renamed to Navigate.py for the default FSS template)
* Input:
  * 0_PROJECT.md  (generation description of project)
  * 0_GETTINGSTARTED.html  (introducing a new researcher to the project)
  * Navigation.conf  (configuration file)
* Output:
  * Navigation.html (open in web-browser to navigate the project)

------



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

The output of the Python program can be configured by changing the settings in \20230508_ParseDirectory\Processing\20230508_ParseDirectory\Code\\**Navigation.conf**.

In this configuration file you can specify which files and subdirectories to include/exclude. 



------

**PYTHON PROGRAM**

------

\20230508_ParseDirectory\Processing\20230508_ParseDirectory\Code\\**ParseDirectory_v1.py**

This Python program parses a complete File System Structure (FSS) starting from its root. 

The final navigation file **Navigation.html** that is produced by this script is written to \20230508_ParseDirectory\Processing\20230508_ParseDirectory\Results\Navigation.html

This navigation file is a copy of the **navigation-template.html** in the \20230508_ParseDirectory\Processing\20230508_ParseDirectory\Results\\**.navigate** directory. This template defines four iframes that hold all content of the FSS.

The files required to navigate the FSS are also written to the **\.navigate** directory:

* 0_gettingstarted.html (copied from 0_GETTINGSTARTED.html in the root of the FSS)
* 0_project.html (copied from 0_PROJECT.md in the root of the FSS)
* fss.html the directory structure of the FSS and relevant files



There should be a **0_GETTINGSTARTED.html**, which is used to introduce new researchers to the project and its structure. E.g., indicating the main data files, main processing scripts, and main results. This file can be made in any editor and then converted to an html file.



**Note**: this script is used for development and testing



------

For the final Python script that can be used with a real FSS template several changes need to be made:

* The Python program needs to be **compiled** and placed in the root of the FSS

* The **paths** in the Python program should be changed. These are all located at the beginning of the program:

  * ```
    # Specify location of FSS
    FSSpath = "F:\\Cloud\\Dropbox\\BioLab\\FSS Projects\\20210617_TNF_Modelling\\"
    
    # Location of .navigate directory
    navDir  = ".navigate\\"   # in root of FSS
    
    # Location of output HTML file (Navigate.html)
    navigateDir = ""          # root of FSS
    
    # Location of configuration file
    confDir = ""             # root of FSS
    ```
* **FSSpath** (location of the FSS) should become a command line argument to the compiled program instead of being specified in the Python file itself.
* The directory **\.navigate** with its included template **navigate-template.html** should be moved to the root of the FSS
* The configuration file **Navigation.conf** should be moved to the root of the FSS.
* There should be a **0_GETTINGSTARTED.html** in the root of the FSS

------





------

**WARNINGS** 

------

* If the structure of the FSS changes in the future then it may be necessary to update the paths in the Python program.
* The Python program assumes a strict naming of the pre-defined files in the FSS according as outlined in the usage rules of the FSS.



------

**BUGS** 

------

* Directories starting with a dot (e.g., .git) are not recognized as a directory.  Not really a problem but needs to be solved. 
* The construct 'item in' searches for substrings. Therefore, if you have a file test.abc and in the configuration file you specify filesInclude = xtest.abc, then test.abc is also included in the tree.
* If the markdown file contains images then the conversion to html does not yet work correctly (i.e., the html doesn't contain the images)
* Links in the 0_PROJECT.md file do not work once this file is embed as an html file in Navigate.html. 
* The parsing of 0_PROJECT.md may go wrong if the title is not formatted in a specific way. This should be made more general.
