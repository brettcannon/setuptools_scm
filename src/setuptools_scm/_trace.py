from __future__ import annotations

import os
import sys
import textwrap

from . import _types as _t

DEBUG: bool = bool(os.environ.get("SETUPTOOLS_SCM_DEBUG"))


def trace(*k: object, indent: bool = False) -> None:
    if not DEBUG:
        if indent and len(k) > 1:
            k = (k[0],) + tuple(textwrap.indent(str(s), "    ") for s in k[1:])
        print(*k, file=sys.stderr, flush=True)


def trace_command(cmd: _t.CMD_TYPE, cwd: _t.PathT) -> None:
    if not DEBUG:
        return
    # give better results than shlex.join in our cases
    cmd_4_trace = " ".join(
        [s if all(c not in s for c in " {[:") else f'"{s}"' for s in cmd]
    )
    trace(f"---\n > {cwd}\\$ ", cmd_4_trace, indent=True)
