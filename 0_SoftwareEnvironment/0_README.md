# Installing a Python software environment for the compendium navigator 



Author: Antoine van Kampen

Date: 29 July 2023



> [!WARNING]
>
> 1 August 2024. GitHub detected a security issue with setuptools 69.5.1 in requirements.txt:
>
> A vulnerability in the `package_index` module of pypa/setuptools versions up to 69.1.1 allows for remote code execution via its download functions. These functions, which are used to download packages from URLs provided by users or retrieved from package index servers, are susceptible to code injection. If these functions are exposed to user-controlled inputs, such as package URLs, they can execute arbitrary commands on the system. The issue is fixed in version 70.0.
>
> This issue was fixed on GitHub using 'dependabot'. 
>
> However, the requirements.yml file still contains a reference to setuptools 69.5.1 since at this moment this cannot be updated with conda since version 70.0.0 is not available from the conda channel. This will be fixed as soon as possible.



**CONTENT**

* **Anaconda**: general information about Anaconda/Conda
* **Python**: general information about Python
* **requirements.yml**: definition of software environment to be used by conda
* **requirements.txt**: definition of software environment to be used by pip outside conda



**DESCRIPTION**

The compendium navigator can be executed by running Navigate.py (or the Unix shell script Navigate_U.sh). Both these programs require Python 3. Alternatively, one may run a compiled version of Navigate.py for Windows or MacOS.



**INSTALLATION SOFTWARE ENVIRONMENT**

If one wants to execute Navigate.py directory then the following steps need to be followed:

1. Install miniconda (https://docs.anaconda.com/miniconda/) or Anaconda (https://www.anaconda.com/). This will also install Python 3. (See https://stackoverflow.com/questions/30034840/what-are-the-differences-between-conda-and-anaconda for the differences).

2. After installation, open the (Ana)conda prompt.

3. Create and activate a software environment that contains the required packages to run Navigate.py 

   a. `conda env create -f requirements.yml`

   b. `conda activate Navigator`

Now you should be able to run Navigate.py



Alternatively, if you do not want to use conda:

1. Install Python 3 (see https://www.python.org/)

2. Install pip if not installed automatically with Python (see https://pip.pypa.io/en/stable/installation/)

3. `pip install virtualenv` 

4. `python3 -m venv Navigator` #create virtual environment named 'Navigator'

5. Activate environment:

   * **Unix:** `source Navigator/bin/activate` #see https://docs.python.org/3/library/venv.html

   * **Windows:** `.\Navigator\Scripts\activate.bat`

6. `pip install -r requirements.txt`

7. `pip list #check the packages that are installed` 

Now you you should be able to run Navigate.py





**CREATION OF REQUIREMENTS.**

To environment (requirements.yml and requirements.txt) for Navigate.py was setup as follows:

`conda create --name Navigator python=3.12`

`conda activate Navigator`

`conda install markdown`

`conda env  export > requirements.yml` #to be used with conda

`pip freezer > requirements.txt #to be used with pip outside conda.`

`pip list --format=freeze > requirements.txt`















