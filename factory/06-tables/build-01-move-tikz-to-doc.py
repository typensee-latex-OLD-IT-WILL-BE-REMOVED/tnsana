#! /usr/bin/env python3

from mistool.os_use import PPath
from mistool.term_use import ALL_FRAMES, withframe


# --------------- #
# -- CONSTANTS -- #
# --------------- #

THIS_DIR = PPath( __file__ ).parent

PROJECT_NAME  = "tnsana"
DIR_DOC_PATH  = THIS_DIR.parent.parent / f"{PROJECT_NAME}"

TIKZ_DIR     = THIS_DIR / 'examples'
TIKZ_DOC_DIR = DIR_DOC_PATH / 'examples'


# ----------- #
# -- TOOLS -- #
# ----------- #

DECO = " "*4

MYFRAME = lambda x: withframe(
    text  = x,
    frame = ALL_FRAMES['latex_pretty']
)


# ------------------------- #
# -- COPYING EXTRA FILES -- #
# ------------------------- #

print(f"{DECO}* Copying tikz files.")

for tkzfile in TIKZ_DIR.walk("file::*.tkz"):
    tkzfile.copy_to(
        TIKZ_DOC_DIR / tkzfile.name,
        safemode = False
    )

    print(f"{DECO*2}+ {tkzfile.stem} copied.")
