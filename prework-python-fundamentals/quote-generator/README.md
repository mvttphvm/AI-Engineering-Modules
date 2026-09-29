Quote Generator

This is a small Python project I made that gives you a random inspirational quote every time you run it.

How to set it up

1. Make the project folder

If you don't already have the folder, run:

mkdir quote-generator
cd quote-generator

2. Make a virtual environment

For Mac/Linux:

python3 -m venv .venv
source .venv/bin/activate

For Windows Command Prompt:

python -m venv .venv
.venv\Scripts\activate

For Windows PowerShell:

python -m venv .venv
.venv\Scripts\Activate.ps1

If it worked, you should see (.venv) in the terminal.

3. Install the dependencies

There aren't really any extra Python packages needed for this project since it uses built-in Python stuff.

But I still used:

pip install -r requirements.txt

4. Run the program

Run:

python main.py

You should get a quote like:

"Believe you can and you're halfway there." — Theodore Roosevelt

Testing it from scratch

I also tested making the environment again from scratch.

First deactivate the virtual environment:

deactivate

Then delete the old .venv folder:

rm -rf .venv

On Windows CMD you can use:

rmdir /s /q .venv

Then make the virtual environment again:

python3 -m venv .venv
source .venv/bin/activate

Then install the requirements and run the program:

pip install -r requirements.txt
python main.py

If a quote shows up, it worked.

Files

main.py - has the quotes and picks one randomly

requirements.txt - project dependencies (there might not be any)

.gitignore - ignores things like the virtual environment and cache files

README.md - this file