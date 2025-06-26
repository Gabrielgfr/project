import sys
from pathlib import Path

# Configura o path antes de qualquer import
sys.path.insert(0, str(Path(__file__).parent.parent))

import pytest

if __name__ == "__main__":
    pytest.main(["-v", "--html=relatorio.html", "--self-contained-html"])