#!/usr/bin/env python3
"""Validate Android string resources without altering original files."""
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python3 scripts/validate_strings.py path/to/strings.xml")
    path = Path(sys.argv[1])
    if not path.is_file():
        raise SystemExit(f"Missing localization file: {path}")
    root = ET.parse(path).getroot()
    if root.tag != "resources":
        raise SystemExit("Root element must be <resources>")
    seen = set()
    count = 0
    for item in root:
        if item.tag != "string":
            continue
        name = item.attrib.get("name")
        if not name:
            raise SystemExit("String without name")
        if name in seen:
            raise SystemExit(f"Duplicate string name: {name}")
        seen.add(name)
        count += 1
    print(f"Validated {count} unique string resources in {path}")

if __name__ == "__main__":
    main()
