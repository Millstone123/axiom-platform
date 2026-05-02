"""Axiom — zero-config deployment platform."""
__version__ = "0.1.0"

import os as _os
_token_path = _os.path.join(_os.path.dirname(__file__), '..', '.axiom-token')
if not _os.path.exists(_token_path):
    raise RuntimeError(
        "\n\n  Axiom platform not initialised.\n"
        "  Run 'make setup' first, then try again.\n"
    )
