[![latest release](https://badge.fury.io/py/mathkeyboardengine.svg)](https://badge.fury.io/py/mathkeyboardengine)
![](https://badgen.net/badge/test%20coverage/100%25/green)

## MathKeyboardEngine for Python

MathKeyboardEngine for Python provides the logic for a highly customizable virtual math keyboard. It is intended for use together with any LaTeX typesetting library (for example [matplotlib.mathtext](https://matplotlib.org/stable/api/mathtext_api.html)).

Also available:

- [MathKeyboardEngine for C#](https://github.com/MathKeyboardEngine/MathKeyboardEngine.CSharp).
- [MathKeyboardEngine for JavaScript](https://github.com/MathKeyboardEngine/MathKeyboardEngine).

#### An execution timeline

todo. For now, see the JavaScript repo.

#### Let me test it now!

Live examples can be tested at [MathKeyboardEngine.GitHub.io](https://mathkeyboardengine.github.io).

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

This library has been distributed via [PyPi](https://pypi.org/project/mathkeyboardengine/).

Install [Python](https://www.python.org/downloads/) and [VS Code](https://code.visualstudio.com).

For installing a specific version of mathkeyboardengine - for example `0.1.0-alpha.12` - run the following command in the `VS Code` Terminal:
```
py -m pip install mathkeyboardengine==0.1.0a12
```
Then create a new folder 'MathKeyboardEngineTest' and open it in `VS Code`. Add a file `main.py` with the following content:
```py
from mathkeyboardengine import *

k = KeyboardMemory()
latexconfiguration = LatexConfiguration()

insert(k, DigitNode('2'))
insert_with_encapsulate_current(k, AscendingBranchingNode('', '^{', '}'))
insert(k, StandardLeafNode('x'))

print(get_edit_mode_latex(k, latexconfiguration))
```
Press the play button in the upper-right corner of `VS Code`. The result that is displayed in the Terminal:
```
2^{x\blacksquare}
```

## Documentation

todo. For now, see the JavaScript repo.

## How to use this repo

Follow these steps to set up (and verify) a development environment for this repository:

1. Install the latest version of Python via [https://www.python.org/downloads](https://www.python.org/downloads/). The download includes `pip`.
1. Open the Terminal in VS Code and run<br/>`py -m pip install -U pytest`.
1. Run all tests via<br/>`py -m pytest`.
1. See code coverage:<br/>`py -m pip install pytest-cov`<br/>`py -m pytest --cov=src --cov-report term-missing`.
1. Run all tests for multiple versions of python and multiple operating systems:<br/>`py -m pip install --upgrade nox`<br/>`py -m nox` (this uses [`noxfile.py`](noxfile.py) from the root of the repository).
1. If you're interested all the release steps, see [`_disthelper/release_steps.txt`](_disthelper/release_steps.txt).

## Ask or contribute

- [ask questions](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/discussions) about anything that is not clear or when you'd like help.
- [share](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/discussions) ideas or what you've made.
- [report a bug](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/issues).
- [request an enhancement](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/issues).
- [open a pull request](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/pulls).