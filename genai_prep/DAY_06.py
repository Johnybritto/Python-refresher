# GenAI Prep Day 6 practice
# Write comment notes that show:
# - the command to create a virtual environment
# - the command to activate it in PowerShell
# - the command to install requests
# - the command to create requirements.txt
python -m venv .venv        # venv is the module to create virtual env , 
                            #and .venv is the name of the env you can name  different also
                            #  python -m venv myvirtualenv 


source myvirtualenv/bin/activate  # activate the env 

pip install requests                  

pip freeze #list out the installed packages 


pip freeze > requirements.txt # list out the packages and write it to requirements file


pip install -r requirements.txt

