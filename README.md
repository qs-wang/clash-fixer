Clash config fixer
==========================


### Create a Virtual Environment

After cloning or downloading the repo, create a Python virtual environment with:

```
python -m venv .virtualenv
```

if the `pyvenv` command does not exist on your system.

### Activate the Virtual Environment

Now activate the virtual environment. on macOS, Linux and Unix systems, use:

```
source .virtualenv/bin/activate
```

On Windows:

```
.virtualenv\Scripts\activate.bat
```

### Install the Development Environment

Now run:

```
pip install -e .[dev]
```

This will install the packages the project depends on in production as well as packages needed during development.

### Run the script
python src/main.py