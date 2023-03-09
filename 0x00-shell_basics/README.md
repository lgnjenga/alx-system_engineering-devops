## Shell Basics Tasks Files

### Task 0. Where am I?
> Write a script that prints the absolute path name of the current working directory.
> **Script File:** [0-current_working_directory](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/0-current_working_directory)

### Task 1. What’s in there?
> A script file to display the contents list of your current directory.
> **Script File:** [1-listit](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/1-listit)

### Task 2. There is no place like home
> A script file that changes the working directory to the user’s home directory.
> You are not allowed to use any shell 
> **Script File:** [2-bring_me_home](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/2-bring_me_home)

### Task 3. The long format
> A script file to display current directory contents in a long format
> **Script File:** [3-listfiles](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/3-listfiles)

### Task 4. Hidden files
> A script file to display current directory contents, including hidden files (starting with .). Use the long format.
> **Script File:** [4-listmorefiles](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/4-listmorefiles)

### Task 5. I love numbers
> Display current directory contents.
- Long format
- with user and group IDs displayed numerically
- And hidden files (starting with .)
> **Script File:** [5-listfilesdigitonly](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/5-listfilesdigitonly)

### Task 6. Welcome
> Create a script that creates a directory named my_first_directory in the /tmp/ directory.
> **Script File:** [6-firstdirectory](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/6-firstdirectory)


### Task 7. Betty in my first directory
> Move the file betty from /tmp/ to /tmp/my_first_directory.
> **Script File:** [7-movethatfile](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/7-movethatfile)

### Task 8. Bye bye Betty
> Delete the file betty.
> The file betty is in /tmp/my_first_directory.
> **Script File:** [8-firstdelete](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/8-firstdelete)

### Task 9. Bye bye My first directory
> Delete the directory my_first_directory that is in the /tmp directory.
> **Script File:** [9-firstdirdeletion](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/9-firstdirdeletion)

### Task 10. Back to the future
> Write a script that changes the working directory to the previous one.
> **Script File:** [10-back](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/10-back)

### Task 11. Lists
> Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
> **Script File:** [11-lists](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/11-lists)

### Task 12. File type
> Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
> **Script File:** [12-file_type](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/12-file_type)

### Task 13. We are symbols, and inhabit symbols
> Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
> **Script File:** [13-symbolic_link](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/13-symbolic_link)

### Task 14. Copy HTML files
> Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
You can consider that all HTML files have the extension .html
> **Script File:** [14-copy_html](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/14-copy_html)

### Task 15. Let’s move
> Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.
> You can assume that the directory /tmp/u will exist when we will run your script
> **Script File:** [100-lets_move](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/100-lets_move)

### Task 16. Clean Emacs
> Create a script that deletes all files in the current working directory that end with the character ~.
> **Script File:** [101-clean_emacs](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/101-clean_emacs)

### Task 17. Tree
> Create a script that creates the directories welcome/, welcome/to/ and welcome/to/school in the current directory.
> You are only allowed to use two spaces (and lines) in your script, not more.
> **Script File:** [102-tree](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/102-tree)

### Task 18. Life is a series of commas, not periods
> Write a command that lists all the files and directories of the current directory, separated by commas (,).
- Directory names should end with a slash (/)
- Files and directories starting with a dot (.) should be listed
- The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
- Only digits and letters are used to sort; Digits should come first
- You can assume that all the files we will test with will have at least one letter or one digit
- The listing should end with a new line
> **Script File:** [103-commas](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/103-commas)

### Task 19. File type: School
> Create a magic file school.mgc that can be used with the command file to detect School data files. School data files always contain the string SCHOOL at offset 0.
> **Script File:** [school.mgc](https://github.com/lgnjenga/alx-system_engineering-devops/blob/master/0x00-shell_basics/school.mgc)


