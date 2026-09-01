"""Put the repository root on sys.path so `import counting` works."""

from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
root = str(REPO_ROOT)
if root not in sys.path:
    sys.path.insert(0, root)
