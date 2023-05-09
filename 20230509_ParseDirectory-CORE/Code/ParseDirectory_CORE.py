#
# Program: show the project structure in a html file to allow easy navigation
# Authors: Antoine van Kampen, Aldo Jongejan
# Date: 9 May 2023
#
# This software is to be used as part of CORE, the approach to improve the reproducibility of computational
# projects.
#
# This version is to be used with the FSS template
#
# Updates:
# 9 May 2023: First version
#

import os
import markdown
import re                  # regular expression
import shutil              # copying files
from html import escape
from datetime import date


#
# Main function to create project structure (directories and files)
#
# This function takes arguments to include/exclude files, filetypes, and subdirectories.
# Note: 'filetypes' determines the filetypes to be included. This would make 'filetypesexclude' unnecessary.
#       However, here we have the situation that we would like to include .txt files but to exclude '*-template.txt'
#       files, which can now be specified in the filetypesexclude argument.
#       Alternatively, we could have listed all the individual template files in the filesexclude tuple.
#
# fsspath:          location of FSS
# filetypes:        filetypes to include in tree
# filesexclude:     specific files to always exclude from tree
# filesinclude:     specific files to always include in tree
# filetypesexclude: filetypes to exclude from tree
# direxclude:       directories to exclude from tree
# fileshelp:        help files to exclude from tree
#
# Output: directory structure with hyperlinked files
#
def create_directory_structure(fsspath, filetypes=None, filesexclude=None,
                               filesinclude=None, filetypesexclude=None,
                               direxclude=None, fileshelp=None):
    directories = []
    files = []

    # Get all subdirectories and files (using the includes and excludes)
    for item in os.listdir(fsspath):
        item_path = os.path.join(fsspath, item)
        if os.path.isdir(item_path) and (direxclude is None or item not in direxclude):
            directories.append(item)
        elif (filetypes is None or item.endswith(filetypes)) and \
                (filesexclude is None or item not in filesexclude) and \
                (filesHelp is None or item not in fileshelp) and \
                (filetypesexclude is None or not item.endswith(filetypesexclude)) or \
                (filesinclude is None or item in filesinclude):
            files.append(item)

    # Sort in alphabetical order
    directories.sort()
    files.sort()

    # Convert directory structure/files to tree (html format)
    content = ""
    for item in directories:
        item_path = os.path.join(fsspath, item)
        content += f"<details><summary><strong>{escape(item)}</strong></summary></li>"
        content += "<ul>"
        content += create_directory_structure(item_path, filetypes, filesexclude, filesinclude,
                                              filetypesexclude, direxclude, fileshelp)
        content += "</ul>"
        content += "</details>"

    # Note: the html output will be shown in Navigation.html, which is a predefined HTML file
    # containing 4 iframes. The tree is shown in the upper left corner. The content of the
    # files are shown in 'frame-2'  (upper right corner).
    for item in files:
        item_path = os.path.join(fsspath, item)
        content += f"<li><a href=\"{escape(item_path)}\" target=\"frame-2\">{escape(item)}</a></li>"

    return content
## End of function create_directory_structure


#
# Function to parse the 0_PROJECT.md file and convert to HTML. This file contains the general project information
# and should # be displayed together with the project organization (i.e., the FSS)
#
# fsspath: location of FSS
# filename: 0_PROJECT.md (default) or alternative
#
# Output: html file with general project information
#
# The converted markdown file is also saved as a html file in .navigate to be displayed in the
# project navigation window
#
def parse_project(fsspath, filename):
    with open(fsspath + filename, "r") as f:
        markdown_text = f.read()                # read complete markdown file
    project = markdown.markdown(markdown_text)  # convert to html
    return project
## End of function part_project


#
# Format and save project (i.e., 0_PROJECT.md) as html file in .navigate
#
# fsspath: location of FSS
# project: html version of 0_PROJECT.md
# line:    html line
# title:   Section title
#
def save_project(fsspath, project, line, title):
    with open(fsspath + "Processing\\20230508_ParseDirectory\\Results\\.navigate\\0_project.html", "w") as f: # TODO: need to change path in final version
        f.write(line)
        f.write(title)
        f.write(line)
        f.write(project)     # write converted markdown file to html file
        f.write(line)
    return True
## End of function save_project


#
# Format and save the html file that serves as a starting point for novel
# users of the project.
# Filename is assumed to be 0_GETTING_STARTED.html. This should be a html file in the root of the FSS.
#
# fsspath: location of FSS
# filename: 0_GETTINGSTARTED.html (default) or alternative
# line:    html line
# title:   Section title
#
def save_getting_started(fsspath, line, title, filename="0_GETTINGSTARTED.html"):
    with open(fsspath + filename, "r") as f:
        start = f.read()   # read html file
    # Format and save
    with open("..//Results//.navigate/0_gettingstarted.html", "w") as f: # TODO: need to change path in final version
        f.write(line)
        f.write(title)
        f.write(line)
        f.write(start)
        f.write(line)
    return True
## End of function save_getting_started


#
# Function to get the name of the GitHub repository corresponding to the project.
# From github.txt in /Processing
# The repository is identified by looking for the last line in this file that
# - ends with .git
# - starts with http
# - starts with github.com
#
# fsspath: location of FSS
# filename: github.txt (default) or alternative
#
# Output: name of GitHub repository
#
def parse_repo(fsspath, filename="github.txt"):
    repo = "No GitHub repository found"  # default response if repository is not specified or cannot be found
    f = open(fsspath + "Processing\\" + filename, "r")
    myline = f.readline()
    while myline:
        myline = myline.rstrip()  # remove trailing spaces
        if myline.endswith('.git') or \
                myline.startswith('http') or \
                myline.startswith('github.com'):
            repo = myline
        myline = f.readline()
    return repo
## End of function parse_repo


#
# Function: write Navigation.html
#
# fsspath:             location of FSS
# repo:                location of GitHub repository
# project:             general project information
# gettingstarted:      information to get the user of the project started with this project
# directory_structure: structure of FSS and all files in FSS
#
def write_navigation(fsspath, repo, project, gettingstarted, directory_structure):
    fss = f"<ul>{directory_structure}</ul>"

    today = date.today()  # Get date and time

    # html stuff
    startHTML = "<html><body>"
    endHTML   = "</body></html>"
    style     = "<style>hr.rounded {border-top: 4px solid #bbb; border-radius: 5px;} </style>"  # rounded border
    line      = "<hr class='rounded'>"

    # text elements
    pagetitle    = "Project:"
    information  = "Project information"
    browser      = "Project browser"
    starting     = "Getting started"
    repo         = "<a href=" + repo + ">" + repo + "</a>"
    repo         = "Github repository: " + repo
    Instruction1 = 'Click triangle to unfold directory. Click on file to show contents.'
    Instruction2 = 'Note: only relevant files are shown in this browser'

    # Parse the project name out of 0_PROJECT.md
    # Since it was converted from markdown to html, I remove the html tags using re.search
    projectname = project.split('\n', 1)[0]
    projectname = re.search('</strong>(.*)</p>', projectname)
    projectname = projectname.group(1)

    # format text elements
    pagetitle   = "<p style=\"color:red;font-size:25px;\"> <strong>" + pagetitle + projectname + "</strong> </p>"
    projectname = "<p style=\"color:blue;font-size:20px;\"> <strong>Project organization: " + projectname + \
                  "</strong> </p>"
    information = "<p style=\"color:blue;font-size:20px;\"><strong>" + information + "</strong></p>"
    starting    = "<p style=\"color:blue;font-size:20px;\"><strong>" + starting + "</strong></p>"
    browser     = "<p style=\"color:blue;font-size:20px;\"><strong>" + browser + "</strong></p>"
    DateTime    = "Generated on: " + today.strftime("%B %d, %Y")  # Textual month, day and year
    repo        = "<p style=\"color:black;font-size:16px;\">" + repo + "</p>"

    # Copy navigation template
    #
    # The navigation template defines four iframes in which all content will be displayed
    src = fsspath + "Processing\\20230508_ParseDirectory\\Results\\.navigate\\navigate-template.html"
    dst = fsspath + "Processing\\20230508_ParseDirectory\\Results\\Navigate.html"
    shutil.copy(src,dst)

    # Copy 0_GETTINGSTARTED.pdf
    src = fsspath + "0_GETTINGSTARTED.html"
    dst = fsspath + "Processing\\20230508_ParseDirectory\\Results\\.navigate\\0_gettingstarted.html"
    shutil.copy(src,dst)

    # Format and save Project (0_PROJECT.md) as html file
    save_project(fsspath, project, line, information)

    # Format and save Project file that contains project highlights/summary
    save_getting_started(fsspath, line, starting, gettingstarted)

    #
    # Write html page and save to file
    #
    with open(fsspath + "Processing\\20230508_ParseDirectory\\Results\\.navigate\\fss.html", "w") as f:  # TODO change path in final version
        f.write(startHTML)     # html stuff
        f.write(style)         # html stuff
        f.write(line)          # html line
        f.write(pagetitle)     # Section title: Project Overview
        f.write(DateTime)      # Date of generation
        f.write(line)          # html line
        f.write(browser)       # Section title: Project browswer
        f.write(line)          # html line
        f.write(repo)          # Name of github repository
        f.write(Instruction1)  # Line with instructions
        f.write(fss)           # FSS structure
        f.write(Instruction2)  # Line with instructions
        f.write(line)          # html line
        f.write(endHTML)       # html stuff

## End of function write_navigation


#
# CONFIGURATION
#

# Specify location of FSS
# FSSpath = "C:\\_data\\Dropbox\\BioLab\\FSS Projects\\20230508_ParseDirectory\\"
FSSpath = "F:\\Cloud\\Dropbox\\BioLab\\FSS Projects\\20230508_ParseDirectory\\"  #TODO path

# Specify file that holds general project information and highlights
ProjectFile        = "0_PROJECT.md"
GettingStartedFile = "0_GETTINGSTARTED.html"

#
# Define subdirectories, filetypes, and files to include/exclude in the project overview
#

# Help files
filesHelp = ("HELP.md", "HELP_FileNameConventions.md", "HELP_FileSystemStructure.md")

# File types to show in tree
fileTypes = (".py", ".ipynb", ".R", ".md", ".txt", ".pdf", ".docx")

# File types to exclude
fileTypesExclude = ("-template.txt")

# Specific files not to show
filesExclude = ("ACKNOWLEDGEMENTS.md", "CITATION.md", "VERSION-HISTORY.md",
                "Step-by-Step-ENCORE-Guide_v11.docx", ".gitignore", "github.txt")

# Specific files to always include
filesInclude = ("test.abc")

# Specific directories not to show
directoryExclude = ("Sharing", "0_SoftwareEnvironment", ".navigate", ".git")


#
# EXECUTE FUNCTIONS TO MAKE NAVIGATION.HTML
#

# Parse Project file from markdown to html. This file will be printed in the bottom-left
# frame of the predefined html page (Navigation.html) in the final output.
Project = parse_project(FSSpath, ProjectFile)

# Get the name of the GitHub repository
Repo = parse_repo(FSSpath)

#
# Generate the directory structure
#
directory_structure = create_directory_structure(fsspath=FSSpath,
                                                 filetypes=fileTypes,
                                                 filesexclude=filesExclude,
                                                 filesinclude=filesInclude,
                                                 fileshelp=filesHelp,
                                                 filetypesexclude=fileTypesExclude,
                                                 direxclude=directoryExclude)

write_navigation(FSSpath, Repo, Project, GettingStartedFile, directory_structure)
