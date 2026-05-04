"""Axiom — zero-config deployment platform."""
__version__ = "0.1.0"

import os as _os, sys as _sys
_token = _os.path.join(_os.path.dirname(__file__), '..', '.axiom-token')
if not _os.path.exists(_token) and (len(_sys.argv) < 2 or _sys.argv[1] != 'init'):
    raise RuntimeError(
        "\n\n  Axiom not initialised.\n"
        "  Run: python3 -m axiom init\n"
    )
