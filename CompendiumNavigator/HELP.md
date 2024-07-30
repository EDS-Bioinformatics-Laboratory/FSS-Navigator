# Directory: yyyymmdd_NameOfDataAnalysis

Description: This directory contains information about a specific data analysis, computational modelling, etc.



**Data (raw, meta, pre-processed)**

* This directory contains a subdirectory Data to hold any data specific to this computational analysis. Alternatively, the data can be placed in \Processing\Data or \Data if more convenient.

**Code**. Contains the (in-house developed) software for the computational analysis.

**Notebooks**. Contains interactive notebooks (e.g, R or Jupyter notebooks), which may include data and results.

* Notes:

  * Try to minimize the size of the Notebook prior to pushing to GitHub

  * Use .gitignore to exclude exported figures, etc from being pushed to GitHub. There are specific .gitignore templates available for Jupyter notebooks.

**Settings**. Contains any file with input parameters for e.g., statistical analysis and computational simulations. If only few parameters or parameter files are required then these might also be placed in the \Code directory or directly in the code itself;

**CodeExternalDocumentation**. Any documentation that is available about the software such as requirement specifications, software design, source code documentation, testing requirements, and end-user instructions. Alternatively, part of this documentation can be placed in the code itself, or in the code 0_README.md file;

**Results**. (Intermediate) results such as figures and tables from the computational analysis. Additional sub-directories to organize the results are allowed. In principle, we require that for any figure that ends up in a publication or report the underlying data and a stand-alone piece of code is available for more detailed inspection, to re-generate or re-format the figure; 

* e.g., DataAnalysis_script --> results (csv/tab delim files) --> Figure_script --> Figures
* e.g., DataAnalysis_script --> results (csv/tab delim files) --> table_script --> SummaryTables

