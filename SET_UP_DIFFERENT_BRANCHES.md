# How to Set up Different Branches with in a Repository

### Prerequisites:
- Have Git Bash on your system

## Getting Started:

- ### Clone The Repository
    ``` git clone https://github.com/SingletLinkage/DSII_Group_Assignment_Case_7.git```

- ### Check if you have origin setup
    ```git remote add origin https://github.com/SingletLinkage/DSII_Group_Assignment_Case_7.git```

- ### Add your Branch 
    ```git branch -M <name of branch>```
    For example : git branch -M Arka

Now you're ready to make commits!

## How to make commits:

- ### Make Some Changes etc
- ### Add those Changes
    ```git add *```
- ### Commit Changes
    ```git commit -m <message>```
    For example: git commit -m "First Commit"
- ### Push to your branch
    ```git push -u origin <you branch name>```
    For Example : git push -u origin Arka

## Pulling from a Branch:
```git pull origin <branch name>```  For Example: git pull origin Arka