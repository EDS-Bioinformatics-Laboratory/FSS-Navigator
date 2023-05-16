# Navigate standardized file system structure (FSS) (parse directory)



**Short project description**

Development of Python program that parses the standardized File System Structure (FSS) and writes a html file to easily navigate this directory structure and to inspect the files that are in there.


This Python script is part of **ENCORE** (Enhancing Computational Research) to navigate the File System Structure (FSS)

>>>>>>> 

**Date:** 9 May 2023  
**Last update**: 16 May 2023  
**Developed by:** Prof. dr. Antoine van Kampen, Dr. Aldo Jongejan, Utkarsh Mahamune (www.bioinformaticslaboratory.eu)  
**Operating System(s) / version(s) used during development:** Windows 11  
**Language**: Python 3  
**Tested:** on Mac and Windows  
**Specific hardware requirements:** None. Should work on Mac, Windows and *nix.  
**Software environment:** Python 3 / Anaconda      

   



------

**FILES AND DIRECTORIES**

------

* **Navigate.py**. Main program
* **Test_Navigate_model.py**. Python program to test if Navigate.py can be imported and executed as a module. Note: this works from command line but for unknown reason not from within DataSpell.
* Input:
  * **0_PROJECT.md**.  General description of project. This file is one of the pre-defined files of CORE and should be present in the root of the FSS.
  * **0_GETTINGSTARTED.docx.**  This template document should describe the most important aspects of your project to introduce it to your peers. This file should be in the root of the FSS and manually converted to an html file. Alternatively, you can use any other document type (e.g., LaTex).
  * **0_GETTINGSTARTED.html**.  This file should be in the root of the FSS. 
  * **Navigation.conf**.  Configuration file that determines the content of Navigation.html. This file should be in the root of the FSS.
  * __**navigate-template.html__**. (template that will be copied to Navigation.html). This file should be present in the directory .navigate
* Output:
  * **Navigation.html**. This file is generated by Navigate.py and will be written in the root of the FSS. Open this file in your web-browser to navigate the project.
* Directories
  * **\.navigate** This directory contains temporary files (generated by Navigate.py) that are used by Navigation.html. In addition, it should contain navigate-template.html. This directory should be located in the root of the FSS.


------



------

**INSTALLATION AND EXECUTION IN EXISTING FSS** 

------

All files mentioned in the previous section are found in https://github.com/EDS-Bioinformatics-Laboratory/ParseDirectory/tree/main/20230508_ParseDirectory/Code

  

1. Copy the files and .navigate to the locations indicated in the previous section.
2. Enter the title of the projection Navigation.conf and change any of the other settings if necessary.  
3. Run the Python program from the command line. For example:
   * python.exe Navigate.py
   * python.exe Navigate.py -h
   * python.exe Navigate.py -C myconf.txt
4. Open Navigation.html in web-browser



<u>Notes:</u> 

* If the content of the FSS is changed then you need to rerun the Python program. Navigation.html is not automatically (magically) updated.
* A compiled version of this program will become available in the future to prevent that Python should be installed on your computer.
* Navigate.py can also be imported as a module:

  ```
  import Navigate
  
  Navigate.create_navigate()
  ```

​	Note: for unknown reason, using this import does not work if executed from DataSpell/PyCharm. It does 	work if the script is executed from the command line

------

**CONFIGURING NAVIGATION**

------

The output of the Python program can be configured by changing the settings in **Navigation.conf**.

In this configuration file you can specify 

* Title of the project
* Files and subdirectories to include/exclude in the directory tree



<u>Notes:</u> 

* The project title is also in 0_PROJECT.md. However, since there is no standardized way of formatting this title or to have it one the first or second line of the file it is difficult to extract and re-format. Consequently, it should now also be specified in the configuration file. The code to parse it from 0_PROJECT.md is still in the Python program.



------

**TESTING**

------

The code is located in \20230508_ParseDirectory\Processing\20230508_ParseDirectory\Code\\**Navigate.py**

To test the program, copy **Navigate.py** to the root of the FSS **\20230508_ParseDirectory** and run the Python program. 



This Python program parses a complete File System Structure (FSS) starting from its root. 



The final navigation file **Navigation.html** that is produced by this program is written to the root of the FSS. This navigation file is a copy of the **__navigation-template.html__** in the \20230508\\**.navigate** directory. This template defines four iframes that hold content of the FSS.



The files required to navigate the FSS are also written to the **\.navigate** directory. E.g., 

* 0_gettingstarted.html (copied from 0_GETTINGSTARTED.html in the root of the FSS)

* 0_project.html (copied from 0_PROJECT.md in the root of the FSS)
* fss.html the directory structure of the FSS and relevant files

In addition, the .navigate directory will hold html copies of all markdown files (*.md) in the FSS. Markdown files do not render correctly in a html iframe. Therefore, if during parsing a markdown file is encountered it will be converted to html. The html file is copied to .navigate. To prevent that files are overwritten, the filename of the html file contains a randomly generated string. In the browser (Navigation.html) you will still see the filename of the markdown file, but the href link points to the corresponding html file in .navigate. 

All files in the .navigate directory are deleted (except navigate-template) if the Python program is executed.



There should be a **0_GETTINGSTARTED.html**. This file can be made in any editor (Microsoft Word, LaTex, etc) and then converted to an html file.



------

**KNOWN ISSUES** 

------

* If the structure of the FSS changes in the future then it may be necessary to update the paths in the Python program.
* The Python program assumes a strict naming of the pre-defined files in the FSS according as outlined in the usage rules of the FSS.
* Directories starting with a dot (e.g., .git) are not recognized as a directory.  Not really a problem but needs to be solved. 
* The construct 'item in' searches for substrings. Therefore, if you have a file test.abc and in the configuration file you specify filesInclude = xtest.abc, then test.abc is also included in the tree.
* Figures are shown in a separate browswer tab since these are not automatically scaled to the size of the iframe in navigate-template.html
* To run Navigate.py it requires Python to be installed on your computer. A compiled version will be made available later in order to run the program without a Python installation.
