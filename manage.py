#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from pathlib import Path


def main():
    """Run administrative tasks."""
    base_dir = Path(__file__).resolve().parent

    # Ensure project root is importable
    if str(base_dir) not in sys.path:
        sys.path.insert(0, str(base_dir))

    # Load environment variables from .env if python-dotenv is available
    try:
        from dotenv import load_dotenv  # optional
        load_dotenv(dotenv_path=base_dir / ".env")
    except Exception:
        pass

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecommerce.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Activate your venv and install dependencies:\n"
            "  .\\.venv\\Scripts\\activate\n"
            "  python -m pip install -r requirements.txt\n"
            "Or verify your interpreter in VS Code (Python: Select Interpreter)."
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
