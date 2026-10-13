
import csv
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from assistant.rules import reply, load_offices


def test_offices_csv_is_valid():
    csv_path = ROOT / "data" / "offices.csv"

    with csv_path.open(encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        assert reader.fieldnames == ["name", "room", "hours"]
        rows = list(reader)

    assert len(rows) == 10

    names = [row["name"].strip().casefold() for row in rows]
    assert all(names)
    assert len(names) == len(set(names))


def test_lookup_graduate_training_office():
    offices = load_offices()

    office = offices["graduate training office"]

    assert office["name"] == "Graduate Training Office"
    assert office["room"] == "Room 8, Building B"


def test_lookup_external_relations_office():
    result = reply("where is office of external relations?")
    assert "Office of External Relations" in result
