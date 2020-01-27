
# lintw.lang

English-Lintwese converter and Lintwese Fonts.

Included are the two variants of the converter: the original JavaScript one, written by [nkymtky](https://github.com/nkymtky), and the Python one, that is adapted from the JavaScript version and partially modified by [cafuneandchill](https://github.com/cafuneandchill). The Python version also contains the Lintwian dictionary viewer (WIP), and PySimpleGUI interfaces for the converter and the dictionary viewer, all of which were written *de novo* by [cafuneandchill](https://github.com/cafuneandchill).

# What is Lintw

https://web.archive.org/web/20180708121040/http://lintw.net/top.en.html

# Converter

http://nkymtky.github.io/lintw.lang/converter.html

## How to use this converter

NOTE: To use the Python version of the converter or the dictionary viewer, it is required to install one of the fonts located in the [fonts](./fonts/) directory to your computer. [LintwBasic 1.13](./font/LintwBasic/1.13/) or [1.20](./font/LintwBasic/1.20/) are recommended.

### JavaScript

```
<script src="path/to/lintw.lang.js"></script>
```

```
var word = lintw.lang.getWord("water");
console.log(word.lintwese + " [" +word.latin + "]");
```

### Python

Run [converter.py](./python_version/converter.py) in a Python environment (executables or shell scripts are not implemented yet).

# Lintwian Dictionary Viewer

Besides the English-Lintwian converter/translator, there are also files for the Lintwian dictionary viewer included in this repository. The viewer is still in the works, so it may not work properly or work at all.

## How to use the dictionary viewer

Run [lintwDictViewer.py](./python_version/lintwDictViewer) in the same way as the converter itself.

# Fonts

http://nkymtky.github.io/lintw.lang/fonts.html
