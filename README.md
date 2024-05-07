# Waste-Wizard
Senior Design II Capstone Project 

<div align=center>
  <img src="https://github.com/azuhayer/Waste-Wizard/assets/80214490/80991f70-e360-47d7-8ac8-bd193b61d118" width="460px" height="250px"/>
</div>

Project Members: 
- Zuhayer Alvi
- Shakir Hossain
- Kenneth Rosario
- Riaz Ahmed

### To Run Application Locally
- Clone the repository and open via VSCODE
- Download and install Anaconda: https://www.anaconda.com/download
- Open Anaconda Prompt (terminal) and create a python env: `conda create env-name`
- Activate the python env: `conda activate env-name`
- Install all dependencies as listed within the requirements.txt file
- On VSCODE click `crtl + shift + p` and type `python:select interpreter`. Click on the new python env created. 
- Run `cd Waste-Wizard` on anaconda prompt
- Run `python app.py` and click on the local host link 

### Create branch

If you didn't fork and will be using the main repo, use branches. (Essentially making a separate folder so it does not interfere with main branch)

To create a new branch: 
- Run `git branch your-branch`
- Checkout into that branch, `git checkout your-branch`

OR
- Run `git checkout -b your-branch` to make the branch and switch to it

If you forgot to make a branch before making changes, use the following command:
- Run `git switch -c your-branch`

### Pushing

- Add your changes, run `git add .`
- If you want to add only particular changes then 'git add file-name'

OR

- Use 'git add -i' for an interactive way to select files to commit
  
- Commit your changes `git commit -m "commit-message"` (Note: the message after -m must be in quotes so it is read as a string)
- To push run, `git push origin your-branch-name`

### Pulling 

- Use `git pull origin dev` to pull all the new content in the 'dev' branch into a new branch

### Delete branch locally

- Run `git branch -d your-branch`
- Note: "-d" can be changed to "-D" for force delete

### View branch

View all branches:

- Run `git branch` to see all local branches

View current branch:

- Run `git branch --show-current`

OR

- Run `git rev-parse --abbrev-ref HEAD`
