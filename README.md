## MathKeyboardEngine for Python

MathKeyboardEngine for Python provides the logic for a highly customizable virtual math keyboard. It is intended for use together with any LaTeX typesetting library (for example ...).

Also available:

- [MathKeyboardEngine for C#](https://github.com/MathKeyboardEngine/MathKeyboardEngine.CSharp).
- [MathKeyboardEngine for JavaScript](https://github.com/MathKeyboardEngine/MathKeyboardEngine).

#### An execution timeline

todo

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

For installing a specific version - for example `0.1.0-alpha.11` - run the following command in the `VS Code` Terminal:
```
py -m pip install mathkeyboardengine==0.1.0a11
```
Then create a new folder 'MathKeyboardEngineTest' and open it in `VS Code`. Add a file `main.py` with the following content:
```
from mathkeyboardengine import KeyboardMemory, LatexConfiguration, getEditModeLatex, AscendingBranchingNode, DigitNode, insert, insertWithEncapsulateCurrent, StandardLeafNode

k = KeyboardMemory()
latexConfiguration = LatexConfiguration()

insert(k, DigitNode('2'))
insertWithEncapsulateCurrent(k, AscendingBranchingNode('', '^{', '}'))
insert(k, StandardLeafNode('x'))

print(getEditModeLatex(k, latexConfiguration))
```
Press the play button in the upper-right corner of `VS Code`. The result that is displayed in the Terminal:
```
2^{x\blacksquare}
```

## Documentation

todo

## How to use this repo

Follow these steps to set up (and verify) a development environment for this repository:

1. Install the latest version of Python via [https://www.python.org/downloads](https://www.python.org/downloads/). The download includes `pip`.
1. Open the Terminal in VS Code and run `py -m pip install -U pytest`.
1. Run all tests via `py -m pytest`.
1. See code coverage: `py -m pip install pytest-cov` + `py -m pytest --cov=src --cov-report term-missing`.

## Ask or contribute

- [ask questions](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/discussions) about anything that is not clear or when you'd like help.
- [share](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/discussions) ideas or what you've made.
- [report a bug](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/issues).
- [request an enhancement](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/issues).
- [open a pull request](https://github.com/MathKeyboardEngine/MathKeyboardEngine.Python/pulls).