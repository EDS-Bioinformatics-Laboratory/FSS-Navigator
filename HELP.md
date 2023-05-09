# Directory: Processing

Description: This directory should contain all computational analyses and results. Its sub-directories include:

* **0_SoftwareEnvironment**. This directory serves two purposes. Firstly, in 0_README-General.md, it provides some basic information about different programming languages (e.g., R, Python), development environments (e.g., RStudio, PyCharm) and package managers (e.g., Anaconda) for peers not familiar with the software setup of the project. Secondly, in 0_README-ProjectSpecific.md, it provides project-specific information about, for example, specific tools that were used or dumps of the used package versions.

* **Data (raw, meta, pre-processed)**

  * The Processing directory contains a directory Data to hold any data used by software in the different data analysis directories. Alternatively, the Data directory within yyyymmdd_NameOfDataAnalysis can be used to hold data which is used only for one specific analysis. In addition: the Data directory in the main directory (yyyymmdd_ProjectName/Data) may be also be used if this is more convenient.

* **yyyymmdd_NameOfDataAnalysis**.  Contains all items (e.g., code, documentation, results) belonging to this specific computational analysis. Change 'NameOfDataAnalysis' to a more specific name. Make, additional yyyymmdd_NameOfDataAnalysis sub-directories if required.

  

<u>Notes:</u> 

1. The Processing directory should be synchronized to the corresponding GitHub repository **without data and results** because we do not have the storage space on GitHub to accommodate this. 

2. The Processing directory should contain a <u>github.txt</u> file with at least the name of  the associated GitHub repository (URL)

3. The Processing and/or DataAnalyses directories should contain a <u>.gitignore</u> file to exclude data, results, etc from GitHub. Only code (and relevant code documentation) should be synchronized with GitHub. Note. The gitignore-FSS-template.txt can be used as a start but might need adjustment for your project. Rename this template to .gitignore. 

4. The Processing directory contains several other gitignore templates for specific languages. To use any of these, merge its content to the gitignore-FSS-template.txt and rename to .gitignore.  It is considered good practice to keep a single gitignore in the top-level directory and not in individual subdirectories, which would make debugging more troublesome.
5. In the README.md file also specify the operating system(s) and version(s) you used during software development, and specifics of the hardware if necessary.

