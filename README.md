[![latest release](https://badge.fury.io/py/mathkeyboardengine.svg)](https://badge.fury.io/py/mathkeyboardengine)
![](https://badgen.net/badge/test%20coverage/100%25/green)

## MathKeyboardEngine for Python

MathKeyboardEngine for Python provides the logic for a highly customizable virtual math keyboard. It is intended for use together with any LaTeX typesetting library (for example [matplotlib.mathtext](https://matplotlib.org/stable/api/mathtext_api.html), [sympy in combination with the official latex install](https://www.sympy.org) or [Katex in a webview](https://katex.org/)).

Also available:

- [MathKeyboardEngine for C#](https://github.com/MathKeyboardEngine/MathKeyboardEngine.CSharp).
- [MathKeyboardEngine for JavaScript](https://github.com/MathKeyboardEngine/MathKeyboardEngine).
- [MathKeyboardEngine for Swift](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Swift#readme).
- [MathKeyboardEngine for other languages](https://github.com/MathKeyboardEngine).

#### An execution timeline

1. You load a page with your customized virtual math keyboard (based on one of the examples). The keys show typeset LaTeX - loaded form a local png file or rendered on the fly - and a cursor is displayed in a textbox-look-a-like element.
1. On your customized virtual math keyboard, you press a key. The key calls a MathKeyboardEngine function, for example `insert(some_matrix_node)` or `move_up()`, `delete_left()`, etc.
1. Calling `get_edit_mode_latex()` outputs the total of LaTeX you typed, for example `\frac{3}{4}\blacksquare` (if `\blacksquare` is your cursor), which you then feed to the typesetting library for display.
1. Calling `get_view_mode_latex()` outputs the LaTeX without a cursor.

#### Let me test it now!
 
Live (JavaScript) examples can be tested at [mathkeyboardengine.github.io](https://mathkeyboardengine.github.io).

A Python example for the PyQt6 GUI framework can be found in the [examples](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/tree/main/examples) folder. Note that the Python example is limited, because it does not handle physical keyboard input. Also, there are many more GUI frameworks for which there is no example. However, the PyQt6 example might provide insight in how to use MathKeyboardEngine in any project.

#### Pros and cons?

<i>Unique about MathKeyboardEngine:</i>

- it supports (almost?) all math mode LaTeX, including matrices. (Please share if you know anything that is not supported.)
- its syntax tree consists of very few different parts: the `StandardLeafNode`, `StandardBranchingNode`, `AscendingBranchingNode` and `DescendingBranchingNode` can be used for almost all LaTeX, including fractions, powers, combinations, subscript, etc. with ready-to-use up/down/left/right navigation.
- it can be used with any LaTeX math typesetting library you like.

<i>A con:</i>

- this library will never be able to handle setting the cursor with the touch of a finger on a typeset formula. (But it DOES support up/down/left/right navigation and has a selection mode via arrow keys.)

<i>More pros:</i>

- you have full control over what you display on the virtual keyboard keys and what a virtual key press actually does.
- customize the editor output at runtime: dot or comma as decimal separator, cross or dot for multiplication, cursor style, colors, etc.
- this library also supports handling input from a physical keyboard, where - for example - the forward slash "/" key can be programmed to result in encapsulating a previously typed number as the numerator of a fraction. (See the examples.)
- almost forgotten: it's open source, free to use, free to modify (please fork this repo)!


## How to use this library

Install [Python](https://www.python.org/downloads/) and [VS Code](https://code.visualstudio.com).

Run the following command in the `VS Code` Terminal:
```
py -m pip install --upgrade mathkeyboardengine
```
Then use
```py
from mathkeyboardengine import *

k = KeyboardMemory()
latexconfiguration = LatexConfiguration()

# subscribe to button click events of virtual key presses, etc.
```
or
```py
import mathkeyboardengine as mke

k = mke.KeyboardMemory()
latexconfiguration = mke.LatexConfiguration()
```
<i>Note: "mke" is an abbreviation of "MathKeyboardEngine". You can choose something different.</i>


## Documentation

Visit the [documentation](https://mathkeyboardengine.github.io/docs/python/0.2/) and the (latest version of the)* [examples folder](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/tree/main/examples) for more implementation details.

\* If you use a version tag in the url like this: https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/tree/v0.1.1, you can see the git repository as it was for that version. That may not be needed if the [changelog](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/tree/main/CHANGELOG.md) doesn't note any important changes.


## How to use this repo

Follow these steps to set up (and verify) a development environment for this repository:

1. Install the latest version of Python via [https://www.python.org/downloads](https://www.python.org/downloads/). The download includes `pip`.
1. Open the Terminal in VS Code and run<br/>`py -m pip install --upgrade pytest`.
1. Run all tests via<br/>`py -m pytest tests/`.
1. See code coverage:<br/>`py -m pip install --upgrade pytest-cov`<br/>`py -m pytest tests/ --cov=src --cov-report term-missing`.
1. This repository has been developed in a folder structure that helps understanding it. The released package however has a "flat" structure, so that all imports can be done from a single namespace. This is done via [_disthelper/flatpack.py](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/blob/main/_disthelper/flatpack.py) (developed especially for this repository). Files from the [src](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/tree/main/src) folder are recursively copied to a new folder 'mathkeyboardengine' and import statements are automatically updated. It also produces a new version of the tests folder. It is called in [setup.py](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/blob/main/setup.py) and [noxfile.py](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/blob/main/noxfile.py).
1. Run all tests for the flatpacked mathkeyboardengine for multiple versions of python :<br/>`py -m pip install --upgrade nox`<br/>`py -m nox` (this uses [noxfile.py](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/blob/main/noxfile.py) from the root of the repository).
1. If you're interested the release steps, see [_disthelper/release_steps.txt](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/blob/main/_disthelper/release_steps.txt).


## License

The MathKeyboardEngine repositories use the most permissive licensing available. The "BSD Zero Clause License" ([0BSD](https://choosealicense.com/licenses/0bsd/)) allows for<br/>
commercial + non-commercial use, closed + open source, with + without modifications, etc. and [is equivalent](https://github.com/github/choosealicense.com/issues/805) to licenses like:

- "MIT No Attribution License" ([MIT-0](https://choosealicense.com/licenses/mit-0//)).
- "The Unlicense" ([Unlicense](https://choosealicense.com/licenses/unlicense/)).
- "CC0" ([CC0](https://choosealicense.com/licenses/cc0/)).

The "BSD Zero Clause License" ([0BSD](https://choosealicense.com/licenses/0bsd/)) does not have the condition

> (...), provided that the above copyright notice and this permission notice appear in all copies.

which is part of the "MIT License" ([MIT](https://choosealicense.com/licenses/mit/)) and its shorter equivalent "ISC License" ([ISC](https://choosealicense.com/licenses/isc/)). Apart from that they are all equivalent.


## Ask or contribute

- [ask questions](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/discussions) about anything that is not clear or when you'd like help.
- [share](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/discussions) ideas or what you've made.
- [report a bug](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/issues).
- [request an enhancement](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/issues).
- [open a pull request](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/pulls).
