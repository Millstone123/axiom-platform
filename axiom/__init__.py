"""Axiom — zero-config deployment platform."""
__version__ = "0.1.0"

import os as _os
_token = _os.path.join(_os.path.dirname(__file__), '..', '.axiom-token')
if not _os.path.exists(_token):
    raise RuntimeError(
        "\n\n  Axiom not initialised.\n"
        "  Run: python -m axiom init\n"
    )
