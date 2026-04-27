IPython Cheat Sheet

**Full Documentation:** [https://ipython.readthedocs.io](https://ipython.readthedocs.io)

-----

## Object Introspection and Documentation

| Command | Description |
| :--- | :--- |
| `obj?` or `?obj` |Show a brief description of obj, such as its signature and "doc string" (documentation).  |
| `obj??` or `??obj` | Show the source code of obj. |
| `obj.<TAB>` | List the attributes of obj.  |
| `obj(<TAB>` | List allowed keyword arguments, and also file and directory names in the current directory.  |

-----

## Command History and Output Cache 
| Command | Description |
| :--- | :--- |
| `<UP ARROW>` and `<DOWN ARROW>` | Scroll through recent commands.  |
| `text<UP ARROW>` | Commands that began with text.  |
| `<CTRL+R>text` | Search commands that contained text.  |
| `_`, `__`, or `___` | First, second, or third most-recent outputs.  |
| `_5` | Output from prompt number 5.  |
| `_i5` | Input string from prompt number 5.  |
| `%history` or `%hist` | Show complete history of current session.  |
| `%history ~2/` | Complete history of two sessions ago.  |
| `%history ~2/5-10` | Lines 5-10 from history of two sessions ago.  |
| `%history -g search_term` | Search all sessions' history for search\_term.  |

-----

## Python Variables and System Environment Variables 

| Command | Description |
| :--- | :--- |
| `%who` | Show names of all "interactive" variables.  |
| `%who <type>` | Filter by type (e.g., `%who ophyd.Device` or `%who function str`).  |
| `%whos` | Show a short description for each variable.  |
| `%env` | List all environment variables.  |
| `%env <VAR>` | Get the value of a specific environment variable (e.g., `%env HOME`).  |
| `%env <VAR> <VAL>` | Set an environment variable (e.g., `%env http_proxy http://proxy:8888`).  |

-----

## Startup Scripts 
Starting IPython with the option `ipython --profile=foo` executes any scripts in the directory `~/.ipython/profile_foo/startup/` with filenames ending in `.py` or `.ipy`. If no `--profile` option is specified, the `profile_default` is used.

-----

## Editing and Running Scripts 

| Command | Description |
| :--- | :--- |
| `%edit` | Create a new temporary file, edit it, and execute the code in the local namespace.  |
| `%edit filename` | Edit a Python script. Execute it upon exiting.  |
| `%edit -x filename` | Edit a file but do not execute it.  |
| `%edit obj` | Edit the file where obj or its class was defined.  |
| `%edit 0/` | Open command history of current session as a text file.  |
| `%run filename` | Run a Python script in a fresh namespace, then export variables to local namespace.  |
| `%run -i filename` | Run a Python script in the local namespace.  |

-----

## System Shell Commands 
| Command | Description |
| :--- | :--- |
| `!cp a.txt b.txt` | Execute text after `!` as a shell command.  |
| `%cd` | Change directory. (Note: `!cd` does not work).  |
| `files = !ls` | Capture the output of a shell command into a variable.  |
| `$f1='a.txt'` <br> `!cp $f1 $f2` | Substitute Python variables into shell commands. Use `$$` for a literal `$`.  |

-----

## Debugging 

After an exception, type `%debug` to activate "post-mortem" debugging mode.
| Debugger Command | Description |
| :--- | :--- |
| `l` or `ll` | "List" some or all source code lines in the current frame.  |
| `u`, `d` | Move up or down between frames.  |
| `p varname` | Print `varname`.  |
| `pp varname` | Pretty-print `varname`.  |
| `exit` | Quit the interactive debugger and return to IPython.  |

-----

## Basic Profiling 

| Command | Description |
| :--- | :--- |
| `%timeit x=5` | Time code execution (averaged over loops).  |
| `%%timeit x=5` | Execute the first line (setup) without timing, then time all following lines.  |

*See also `%prun` and `%lprun` (requires `line_profiler` package).*