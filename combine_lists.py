#!/usr/bin/env python3

import sys
from itertools import product
from pathlib import Path
from typing import List, Tuple


def parse_args(argv: List[str]) -> Tuple[List[Tuple[Path, bool]], Path]:
    """
    Parse command-line arguments.

    Rule:
    - --optional marks ONLY the next file as optional
    - file order is preserved
    """
    files_with_flags: List[Tuple[Path, bool]] = []
    output_path = Path("output.txt")

    mark_optional = False
    i = 0

    while i < len(argv):
        token = argv[i]

        if token in {"-o", "--output"}:
            if i + 1 >= len(argv):
                raise ValueError("Missing value for output file")
            output_path = Path(argv[i + 1])
            i += 2
            continue

        if token == "--optional":
            mark_optional = True
            i += 1
            continue

        path = Path(token)
        files_with_flags.append((path, mark_optional))
        mark_optional = False
        i += 1

    if mark_optional:
        raise ValueError("--optional must be followed by a file")

    if not files_with_flags:
        raise ValueError("At least one input file is required")

    return files_with_flags, output_path


def read_txt(path: Path) -> List[str]:
    if not path.exists():
        raise FileNotFoundError(path)

    text = path.read_text(encoding="utf-8")

    if text and not text.endswith("\n"):
        text += "\n"
        path.write_text(text, encoding="utf-8")

    return [
        line.strip()
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def generate_combinations(
    ordered_lists: List[Tuple[List[str], bool]],
) -> List[str]:
    prepared_lists = []

    for values, is_optional in ordered_lists:
        if is_optional:
            prepared_lists.append([""] + values)
        else:
            prepared_lists.append(values)

    return [
        " ".join(item for item in combo if item)
        for combo in product(*prepared_lists)
    ]


def main() -> None:
    try:
        files_with_flags, output_path = parse_args(sys.argv[1:])
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    ordered_lists = [
        (read_txt(path), is_optional)
        for path, is_optional in files_with_flags
    ]

    combinations = generate_combinations(ordered_lists)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        "\n".join(combinations),
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
