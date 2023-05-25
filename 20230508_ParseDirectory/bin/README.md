# Executables







* **Navigate_W.exe**. 
  * Windows executable if you don't have Python installed on your computer
  * Compiled with: pyinstaller --onefile --add-binary "c:\path\to\python39.dll;." Navigate.py
  * Compiled under Microsoft Windows 11 Pro. Version 22H2. OS Build 22621.1702
  * Execute: Navigate_W.exe -h
  * Tested on 
    * Windows 10 Enterprise. Version 21H2. OS Build 19044.2846
    * Windows 7





* **Navigate_M**. MacOS executable.





* **Navigate_U.sh**. 
  * Shell script to run Navigate on Unix/Linux systems. 
  * Change the first line (#!/usr/bin/env python) if necessary (e.g., #!/usr/bin/python). Make the script executable using chmod +x
  * Execute: Navigate_U.sh -h
  * Tested on Red Hat Enterprise Linux. Kernel Linux 3.10.0-1160.90.1.e17.x86_64
