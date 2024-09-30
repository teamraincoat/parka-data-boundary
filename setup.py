#!/usr/bin/env python

import glob
from pathlib import Path

from setuptools import setup


def data_files(target, srcglb):
    retval = []
    for fpath in glob.glob(srcglb, recursive=True):
        if Path(fpath).is_dir():
            continue
        split = fpath.split("//", maxsplit=1)
        assert len(split) == 2
        subpath = Path(split[1])
        retval.append((f"{target}/{str(subpath.parent)}", [str(fpath)]))
    return retval


setup(data_files=data_files("share/parka", "data//boundary/**/*.*"))
