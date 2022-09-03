from pathlib import Path
import argparse

from templates import RUN_DEFAULT, INPUT_DEFAULT, TEST_DEFAULT


def validate_date(year: str, day: str) -> None:
    "Ensures year and day fit between expected ranges"
    if not 2015 <= int(year) <= 2021:
        raise Exception(
            "Year is out of range. \
            Valid range (inclusuive): 2015-2021"
        )
    if not 1 <= int(day) <= 25:
        raise Exception(
            "Day is out of range. \
            Valid range (inclusive): 1-25"
        )


def create_file(p_obj: Path, content: str) -> None:
    "Create a file with its contents if it doesn't exist"
    if not p_obj.is_file():
        p_obj.write_text(content)


def create(year: str, day: str) -> None:
    "Create the appropriate directories and files for given day"
    src_dir = "advent_of_code"
    test_dir = "tests"
    year = f"year_{year}"
    day = f"day_{day}"

    year_dir = Path(f"{src_dir}/{year}")
    year_test = Path(f"{test_dir}/{year}")
    day_dir = year_dir / day

    year_dir.mkdir(exist_ok=True)
    year_test.mkdir(exist_ok=True)
    day_dir.mkdir(exist_ok=True)

    create_file(day_dir / "run.py", RUN_DEFAULT.format(year, day))
    create_file(day_dir / "input.txt", INPUT_DEFAULT)
    create_file(year_test / f"{day}_test.py", TEST_DEFAULT.format(year, day))


if __name__ == "__main__":
    """Cli interface for direct execution"""
    parser = argparse.ArgumentParser(
        description="""Setup given day with default run and test files""",
    )

    parser.add_argument(
        "-y",
        "--year",
        required=True,
        help="Year to setup",
    )

    parser.add_argument(
        "-d",
        "--day",
        required=True,
        help="Day to setup",
    )

    args = parser.parse_args()
    validate_date(args.year, args.day)
    create(args.year, args.day)
