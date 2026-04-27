Git Ignore and .gitignore

## What is .gitignore?

The `.gitignore` file tells Git which files and folders to ignore (not track).

This is useful for keeping log files, temporary files, build artifacts, or personal files out of your repository.

-   Examples of files to ignore: log files, temporary files, hidden files, personal files, OS/editor files, etc.

The `.gitignore` file itself **is** tracked by Git, so everyone using the repository ignores the same files.

---

## When to Use .gitignore

-   When you want to keep sensitive, local, or unnecessary files out of your repository
-   When sharing a project with others and want to avoid cluttering Git history
-   When working with build tools or editors that create extra files

---

## Create a .gitignore File

1.  Go to the root of your local Git repository.
2.  Create a file named `.gitignore`:

### Example

```shell
touch .gitignore
```

---

## Ignoring Folders

To ignore a folder and everything inside it, use a trailing slash:

temp/ 

This ignores any folder named `temp` anywhere in your project.

---

[REMOVE ADS](https://order.w3schools.com/plans)

---

## Wildcards & Patterns

Wildcards let you match many files or folders at once:

-   `*` matches any number of characters
-   `?` matches a single character
-   `[abc]` matches any character in the set
-   `[!abc]` matches any character **not** in the set

\*.tmp      # all .tmp files
my?ile.txt # matches my1ile.txt, myAile.txt, etc.
log\[0-9\].txt # log1.txt, log2.txt, ... log9.txt 

---

## Negation (!)

Use `!` to **not** ignore something that would otherwise be ignored. This is called an exception:

\*.log
!important.log 

This ignores all `.log` files except `important.log`.

---

## Comments and Blank Lines

Lines starting with `#` are comments and are ignored by Git. Blank lines are also ignored. Use comments to explain your rules:

\# Ignore log files
\*.log

# Ignore temp folders
temp/ 

---

## Local & Personal Ignore Rules

If you want to ignore files only for yourself (not for everyone who uses the repository), add them to `.git/info/exclude`. This works just like `.gitignore` but is not shared.

---

## Global .gitignore (User Level)

You can set up a global `.gitignore` file for all your projects. This is great for ignoring OS or editor files everywhere (like `.DS_Store` or `Thumbs.db`):

```shell
git config --global core.excludesfile ~/.gitignore_global
```

Then add your patterns to `~/.gitignore_global`.

---

## How to Stop Tracking a File

If you add a file to `.gitignore` but Git is still tracking it, you need to tell Git to stop:

```shell
git rm --cached filename.txt
```

This removes the file from the repository but keeps it on your computer. Next time you commit, Git will ignore it.

---

## Tips & Troubleshooting

-   Check for typos-`.gitignore` is case-sensitive!
-   If a file is already tracked, use `git rm --cached` to stop tracking it.
-   Use comments (`#`) to explain tricky rules for your teammates.
-   Use `git status` to see if your ignored files are being tracked.
-   Remember: `.gitignore` only affects files that are **not** already tracked by Git.

---

## Python .gitignore template
Source [github/gitgnore](https://github.com/github/gitignore)

```gitignore 
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[codz]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#   Usually these files are written by a python script from a template
#   before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py.cover
*.lcov
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
# Pipfile.lock

# UV
#   Similar to Pipfile.lock, it is generally recommended to include uv.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
# uv.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
# poetry.lock
# poetry.toml

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#   pdm recommends including project-wide configuration in pdm.toml, but excluding .pdm-python.
#   https://pdm-project.org/en/latest/usage/project/#working-with-version-control
# pdm.lock
# pdm.toml
.pdm-python
.pdm-build/

# pixi
#   Similar to Pipfile.lock, it is generally recommended to include pixi.lock in version control.
# pixi.lock
#   Pixi creates a virtual environment in the .pixi directory, just like venv module creates one
#   in the .venv directory. It is recommended not to include this directory in version control.
.pixi/*
!.pixi/config.toml

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule*
celerybeat.pid

# Redis
*.rdb
*.aof
*.pid

# RabbitMQ
mnesia/
rabbitmq/
rabbitmq-data/

# ActiveMQ
activemq-data/

# SageMath parsed files
*.sage.py

# Environments
.env
.envrc
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#   JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#   be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#   and can be added to the global gitignore or merged into this file.  For a more nuclear
#   option (not recommended) you can uncomment the following to ignore the entire idea folder.
# .idea/

# Abstra
#   Abstra is an AI-powered process automation framework.
#   Ignore directories containing user credentials, local state, and settings.
#   Learn more at https://abstra.io/docs
.abstra/

# Visual Studio Code
#   Visual Studio Code specific template is maintained in a separate VisualStudioCode.gitignore 
#   that can be found at https://github.com/github/gitignore/blob/main/Global/VisualStudioCode.gitignore
#   and can be added to the global gitignore or merged into this file. However, if you prefer, 
#   you could uncomment the following to ignore the entire vscode folder
# .vscode/
# Temporary file for partial code execution
tempCodeRunnerFile.py

# Ruff stuff:
.ruff_cache/

# PyPI configuration file
.pypirc

# Marimo
marimo/_static/
marimo/_lsp/
__marimo__/

# Streamlit
.streamlit/secrets.toml
```

### syntax in markdown
gitgnore is also part of the supported markdown languages for code blocks
```gitignore
your code here
```

from jincheng9/markdown_supported_languages(https://github.com/jincheng9/markdown_supported_languages)