# pre-commit-script by gidra
## Prerequisites
  - Gitleaks
## Installation 
 1. Open a terminal and navigate to your Git repository's local directory.

 2. Create a new file named pre-commit in the .git/hooks directory:
 ```bash
 sudo nano .git/hooks/pre-commit
 ```
 3. Open the pre-commit file in a text editor and add the following content:

 ```bash
Copy code
#!/bin/bash

output=$(gitleaks detect --verbose --redact)

if [[ -n $output ]]; then
    echo "Error: Secrets found in the code:"
    echo "$output"
    exit 1
fi
```
 4. Save the file and exit the text editor.

 5. Make the pre-commit file executable:

```bash
chmod +x .git/hooks/pre-commit
```
Now, whenever you attempt to make a commit, the pre-commit hook will automatically run gitleaks to check for secrets in your code. If any secrets are detected, the commit will be rejected, and an error message will be displayed.
Make sure you have gitleaks installed and accessible in your system's PATH for the script to work correctly.

