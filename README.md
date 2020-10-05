# gitmodules_example_a
This is the first example for the
<a href=https://github.com/KuYaki/gitmodules>gitmodules</a> project.

## Dependencies
This project is assumed to be used with the <a href=https://github.com/KuYaki/gitmodules>gitmodules</a> dependency

```
pip install gitmodules
```

Also <a href=https://github.com/KuYaki/gitmodules_example_b>gitmodules_example_b</a> and 
<a href=https://github.com/KuYaki/gitmodules_example_c>gitmodules_example_c</a> should be updated as well

```
git submodule update --recursive --init
```

## Description
<a href=https://github.com/KuYaki/gitmodules_example_c>gitmodules_example_c</a> can be executed as a main script 
but if you will try to import it in any other project as a git submodule
you will be forced to append its path to the <b>sys.path</b>:

```python
# in b.py from gitmodules_example_b
import sys
sys.path.append("gitmodules_example_c")
from gitmodules_example_c import c
```

The same problem will occurs if you will try to import 
<a href=https://github.com/KuYaki/gitmodules_example_b>gitmodules_example_b</a> into any other project.
But even if you will append it via <b>sys.path.append</b> problem will not be solved for
<a href=https://github.com/KuYaki/gitmodules_example_c>gitmodules_example_c</a>:

```python
# in a.py from gitmodules_example_a
import sys
sys.path.append("gitmodules_example_b")
from gitmodules_example_b import b
```

And you will be forced to append all the submodules for <b>b</b> as well:

```python
# in a.py from gitmodules_example_a
import sys
import os
sys.path.append("gitmodules_example_b")
sys.path.append(os.path.join("gitmodules_example_b", "gitmodules_example_c"))
from gitmodules_example_b import b
```

Or you can simply use <a href=https://github.com/KuYaki/gitmodules>gitmodules</a> instead:

```python
# in a.py from gitmodules_example_a
import gitmodules
from gitmodules_example_b import b
```

This method allows you to import git submodule as an ordinary module or as a standard library.
So that if you will decide to upload your git submodules to PyPi you will not be forced to change your scripts. 
