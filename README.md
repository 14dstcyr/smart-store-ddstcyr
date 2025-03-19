# smart-store-ddstcyr
Sales Project Instructions

#### Create a repository in Github for new project
- Make sure to add the README.md while creating the repository

### Add the following files to your root file which are obtained from Dr. Cases' repository  pro-analytics-01 from assignment number 1. 
* .gitignore (copy the contents and paste it in your file)
* requirements.txt (copy the contents and paste it in your file)

### Be sure to git push the new information to your repository in GitHub

### Add the following folders in this specific order
- data/
   - raw/
- scripts/
- utils/
   - logger.py (this is going to be a file)

### Create a virtual environment in VS Code editor if you haven't already
- It should be .venv and again should have been created from the first assignment. If you didn't, this is how to create it.
    - This page provides instructions to create a place in your project repository folder that will hold the Python virtual environment for the project. It provides an isolated Python environment for the project, so we don't mess up the global Python used by our machine.

      This is typically just done once at the beginning of a project. If it gets messed up, we can delete .venv and recreate it at any time.
  #### Before Starting
      - Open your project repository in VS Code.

      - We'll open a new terminal in VS Code and run a single command to create a new .venv folder for the local project virtual environment.

   #### Windows Users - Task 1. Create .venv
      On Windows, Use PowerShell (not cmd):
      - Run the following command from the project root directory.
       py -m venv .venv

   #### Accept VS Code Suggestions
    If VS Code asks: We noticed a new environment has been created. Do you want to select it for the workspace folder? Click Yes
   #### ADVANCED OPTION (Create .venv when an Older Python Version is Required)
   Most projects can use the latest Python 3.x, but some tools (like Apache Kafka or Apache Spark) may require an older version.

   First, see the machine setup instructions to install additional versions of Python.

   Then, specify the required version when creating the virtual environment. For example:
   ##### On Windows, Use PowerShell (not cmd)
   py -3.11 -m venv .venv

### Be sure to git push the new information to your repository in GitHub

### 

