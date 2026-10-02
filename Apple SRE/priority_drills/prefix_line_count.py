"""AP3 (P0): find files by filename prefix and count their lines."""

from pathlib import Path


def count_prefix_lines(directory: str | Path, prefix: str) -> dict[str, int | None]:
    """Count matching immediate files; record file read errors as None."""
    dir_path = Path(directory)

    if not dir_path.exists():
        raise FileNotFoundError(f"Directory does not exist: {dir_path}")
    if not dir_path.is_dir():
        raise NotADirectoryError(f"Not a directory: {dir_path}")

    result = {}
    match_files = []

    for child in dir_path.iterdir():
        if child.is_symlink():
            continue
        if child.is_file() and child.name.startswith(prefix):
            match_files.append(child)

    match_files.sort(key=lambda path: path.name)

    for file in match_files:
        try:
            with open(file, "r", encoding="utf-8") as f:
                lines = 0
                for _ in f:
                    lines += 1
                result[file.name] = lines
        except (OSError, UnicodeError):
            result[file.name] = None
    return result

def run_tests() -> None:
    from tempfile import TemporaryDirectory
    from unittest.mock import patch

    with TemporaryDirectory() as temporary:
        root = Path(temporary)
        (root / "app-z.log").write_text("first\n\nlast", encoding="utf-8")
        (root / "app-a.log").write_text("", encoding="utf-8")
        (root / "other.log").write_text("one\ntwo\n", encoding="utf-8")
        (root / "App-case.log").write_text("one\n", encoding="utf-8")
        nested = root / "app-directory"
        nested.mkdir()
        (nested / "app-hidden.log").write_text("nested\n", encoding="utf-8")
        (root / "app-link.log").symlink_to(root / "app-z.log")
        (root / "app-broken.log").symlink_to(root / "missing")
        (root / "app-invalid.log").write_bytes(b"valid\n\xff\n")

        expected = {"app-a.log": 0, "app-invalid.log": None, "app-z.log": 3}
        result = count_prefix_lines(root, "app-")
        assert result == expected, result
        assert list(result) == sorted(expected), "Return sorted filename order"
        assert count_prefix_lines(str(root), "absent-") == {}
        assert count_prefix_lines(root, "App-") == {"App-case.log": 1}
        all_files = count_prefix_lines(root, "")
        assert all_files == {**expected, "other.log": 2, "App-case.log": 1}
        assert list(all_files) == sorted(all_files)

        empty = root / "empty"
        empty.mkdir()
        assert count_prefix_lines(empty, "") == {}
        for bad_directory, error in ((root / "missing", FileNotFoundError),
                                     (root / "other.log", NotADirectoryError)):
            try:
                count_prefix_lines(bad_directory, "")
            except error:
                pass
            else:
                raise AssertionError(f"Expected {error.__name__} for {bad_directory}")

        # Simulate denied reads reliably even when tests run with elevated permissions.
        original_open = Path.open

        def guarded_open(path, *args, **kwargs):
            if path.name == "app-z.log":
                raise PermissionError("simulated unreadable file")
            return original_open(path, *args, **kwargs)

        # Path.open delegates to io.open; cover built-in open as well.
        import builtins
        original_builtin_open = builtins.open

        def guarded_builtin_open(path, *args, **kwargs):
            if Path(path).name == "app-z.log":
                raise PermissionError("simulated unreadable file")
            return original_builtin_open(path, *args, **kwargs)

        with patch.object(Path, "open", guarded_open), patch("builtins.open", guarded_builtin_open):
            assert count_prefix_lines(root, "app-") == {**expected, "app-z.log": None}

    print("All Prefix Line Count checks passed")


if __name__ == "__main__":
    run_tests()
