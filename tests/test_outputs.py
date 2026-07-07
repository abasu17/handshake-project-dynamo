import json
from pathlib import Path

EXPECTED = {"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}


def test_report_exists_and_has_required_fields():
    """Criterion 1: the report is a JSON object with exactly the required fields."""
    report_path = Path("/app/report.json")
    assert report_path.exists(), "report.json was not created"
    data = json.loads(report_path.read_text(encoding="utf-8"))
    assert set(data) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests():
    """Criterion 2: the report records the correct total number of requests."""
    data = json.loads(Path("/app/report.json").read_text(encoding="utf-8"))
    assert data["total_requests"] == 6


def test_unique_ips():
    """Criterion 3: the report records the correct number of unique IP addresses."""
    data = json.loads(Path("/app/report.json").read_text(encoding="utf-8"))
    assert data["unique_ips"] == 3


def test_top_path():
    """Criterion 4: the report records the most common request path."""
    data = json.loads(Path("/app/report.json").read_text(encoding="utf-8"))
    assert data == EXPECTED
