# Resources
> This is our Resources document, where we'll make all notes of helpful resources, notes, & commands

1. [Git Commands](https://github.com/meganthoang/uberanalytics/blob/main/docs/RESOURCES.md#git-commands)
2. [Command Line Tips](https://github.com/meganthoang/uberanalytics/blob/main/docs/RESOURCES.md#command-line-tips)
3. [General Housekeeping](https://github.com/meganthoang/uberanalytics/blob/main/docs/RESOURCES.md#general-housekeeping)
4. [Helpful Links](https://github.com/meganthoang/uberanalytics/blob/main/docs/RESOURCES.md#some-helpful-links)

## Git Commands
We'll be using GitHub for Source/Version Control. Some basic Git commands:
  ``` 
  git status 
  git pull # pulls any updates or changes from the online repo
  git add filename.py  # or 'git add -A' or 'git add .' for "all"
  git commit -m "add a message here" # be sure to add a descriptive message
  git push # pushes your commits to the remote repo

  git checkout -b branchname # creates a branch named branchname
  git checkout branch # move between branches - replace branch with the name of the branch you're moving to
  git checkout -d branchname  # -D is force delete
  git merge (name of the branch you wanna merge to)
  git push origin branchname
  ```

You'll need to clone this repo using the command
  ```
  git clone https://github.com/meganthoang/covid_pharm_data
  ```

## Command Line Tips

To run your programs at the command line, type `cmd` into your Windows search bar   to pull up your command prompt and use the following commands to navigate to and run your file. 
  ```nb
  cd - change directory (use cd .. to navigate out of your current folder)
  dir - view what's in the directory (the mac/linux version of this is 'ls')
  python filename.py - run your python script (replace 'filename' with the actual
  file name)
  ```
 
## Some Helpful Links!
  1. [Kaggle Project Link](https://www.kaggle.com/hugomenz/uber-data-visualization)
  2. [Git Commands Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
  3. [Git Tutorial Video](https://youtu.be/0fKg7e37bQE)
  4. [README Editing Instructions](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
  5. [Python Basics](https://www.pythoncheatsheet.org/)
  6. [Cheat Sheet for Pandas Module](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
  7. [Cheat Sheet for NumPy Module](http://datacamp-community-prod.s3.amazonaws.com/da466534-51fe-4c6d-b0cb-154f4782eb54)
  8. [Cheat Sheet for Matplotlib](http://datacamp-community-prod.s3.amazonaws.com/e1a8f39d-71ad-4d13-9a6b-618fe1b8c9e9)
  9. [More Git Shortcuts](https://www.youtube.com/watch?v=ecK3EnyGD8o)
