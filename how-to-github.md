How to use Git/Github for a data scientist - basic level to start

## Prerequisites : Git
## Steps
1. **Create a GitHub repository**:
   - Go to GitHub and log in to your account.
   - Click on the "+" sign in the top-right corner and select "New repository."
   - Give your repository a name, add a description if you want, choose if it's public or private, and then click "Create repository."

2. **Initialize your local project as a Git repository**:
   - Navigate to your project directory using the command line.
   - Run `git init` to initialize the directory as a Git repository.

3. **Add your project files to the Git repository**:
   - Run `git add .` to stage all files in your project directory for the next commit.
   - Alternatively, you can use `git add <file>` to stage individual files.

4. **Commit your changes**:
   - Run `git commit -m "Initial commit"` to commit the staged files with a commit message.

5. **Link your local repository to the GitHub repository**:
   - Copy the URL of your GitHub repository.
   - Run `git remote add origin <repository URL>` to link your local repository to the GitHub repository.

6. **Push your changes to GitHub**:
   - Run `git push -u origin master` to push your committed changes to the GitHub repository. If you're using a different branch, replace "master" with the name of your branch.

After completing these steps, your local project files will be added to your GitHub repository, and you'll be able to see them on GitHub's website. Make sure to commit and push changes regularly to keep your local and remote repositories in sync.
