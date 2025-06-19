import sys
from pathlib import Path

# Ensure tests can import the source packages when run directly
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))


def test_imports():
    import db_scripts
    import app.user_commands
    import app
