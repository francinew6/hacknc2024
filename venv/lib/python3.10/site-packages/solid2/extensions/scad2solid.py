#! /usr/bin/env python

from pathlib import Path

from solid2.core.utils import escape_openscad_identifier as escape
from solid2.libs.py_scadparser import scad_parser

headerTemplate = """\
from solid2.core.object_base import OpenSCADObject as _OpenSCADObject,\
                                    OpenSCADConstant as _OpenSCADConstant
from solid2.core.include_manager import addInclude as _addInclude
from pathlib import Path as _Path

if not {builtins}:
    _addInclude(f"{{_Path(__file__).with_suffix('.scad')}}", {use_not_include})

"""

constantTemplate = "{name} = _OpenSCADConstant('{name}')"

callableTemplate = """\
class {name}(_OpenSCADObject):
    def __init__({paramStr}):
       super().__init__({initStr})

"""

def generateStub(scadFile, outputDir, use_not_include, builtins,
                 headerTemplate=headerTemplate,
                 callableTemplate=callableTemplate):

    def generateHeader():
        return headerTemplate.format(use_not_include=use_not_include,
                                     builtins=builtins)

    def generateConstant(c):
        return constantTemplate.format(name=escape(c.name)) + "\n"

    def generateCallable(c):
        name = escape(c.name)
        paramNames = [escape(p.name) for p in c.parameters]
        paramNames = list(dict.fromkeys(paramNames))

        paramStr = ", ".join(["self"] +
                             [f"{p}=None" for p in paramNames] +
                             ["**kwargs"])
        initList = [f'"{p}" : {p}' for p in paramNames]
        initList.append("**kwargs")
        initStr = f'"{name}", {{{", ".join(initList)}}}'
        return callableTemplate.format(name=name, paramStr=paramStr, initStr=initStr)

    modules, functions, global_vars = scad_parser.parseFile(scadFile)

    escaped_filename = escape(scadFile.stem) + ".py"
    with open(outputDir / escaped_filename, "w") as f:
        f.write(generateHeader())

        for c in global_vars:
            f.write(generateConstant(c))

        for c in functions + modules:
            f.write(generateCallable(c))

def makePackage(directory):
    import os
    if not os.path.exists(directory):
        os.mkdir(directory)
    if not os.path.exists(directory / "__init__.py"):
        with open(directory / "__init__.py", "w") : pass

def scad2solid(infile, useNotInclude=True, builtins=False, outdir=None):
    if infile.is_dir():
        if not outdir:
            outdir = infile
        for f in infile.iterdir():
            makePackage(outdir)
            scad2solid(infile / f.name, useNotInclude, builtins,
                       outdir / f.name)
    elif infile.suffix == ".scad":
        outdir = infile.parent
        makePackage(outdir)
        generateStub(infile, outdir, useNotInclude, builtins)


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser(description="generates a solidpython2 extensions "
                                        "from a OpenSCAD library")
    parser.add_argument("infiles",
                        help="directory containing the scad (library) files or a single file")
    parser.add_argument("-i", "--include", action='store_false', default=True,
                        help="use OpenSCADs 'include' to import the library. "
                             "Otherwiese OpenSCADs 'use' is used")
    parser.add_argument("-b", "--builtins", action='store_true', default=False,
                        help="Don't use neither include the scad file, usually"
                             "because it defines builtins")

    args = parser.parse_args()

    scad2solid(Path(args.infiles), args.include, args.builtins)
