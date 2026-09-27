import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from wsgiref.util import setup_testing_defaults

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

import app


class FleetOpsTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.original_database = app.DATABASE
        app.DATABASE = Path(self.temp_dir.name) / "fleet-test.sqlite3"
        app.initialise_database()

    def tearDown(self):
        app.DATABASE = self.original_database
        self.temp_dir.cleanup()

    def call_app(self, path: str, query: str = ""):
        environ = {}
        setup_testing_defaults(environ)
        environ.update(PATH_INFO=path, REQUEST_METHOD="GET", QUERY_STRING=query)
        result = {}

        def start_response(status, headers):
            result["status"] = status
            result["headers"] = dict(headers)

        raw = b"".join(app.application(environ, start_response))
        result["body"] = raw
        if result["headers"].get("Content-Type", "").startswith("application/json"):
            result["json"] = json.loads(raw.decode("utf-8"))
        return result

    def test_demo_dataset_shape(self):
        data = app.dashboard_data()
        self.assertEqual(data["vehicles"]["vehicles"], 18)
        self.assertEqual(data["vehicles"]["cargo_lifts"], 3)
        self.assertEqual(data["rentals"]["contracts"], 21)
        self.assertEqual(data["leases"]["leases"], 11)
        self.assertEqual(len(data["trend"]), 7)

    def test_seed_is_repeatable_without_duplicates(self):
        app.initialise_database()
        data = app.dashboard_data()
        self.assertEqual(data["vehicles"]["vehicles"], 18)
        self.assertEqual(data["rentals"]["contracts"], 21)

    def test_vehicle_filter_by_status(self):
        rows = app.vehicle_rows(status="Serwis")
        self.assertEqual(len(rows), 2)
        self.assertTrue(all(row["status"] == "Serwis" for row in rows))

    def test_vehicle_search_matches_type_or_fuel(self):
        rows = app.vehicle_rows(query="Hybryda")
        self.assertGreaterEqual(len(rows), 1)
        self.assertTrue(all("Hybryda" in (row["fuel"], row["vehicle_type"]) for row in rows))

    def test_health_endpoint(self):
        response = self.call_app("/api/health")
        self.assertEqual(response["status"], "200 OK")
        self.assertEqual(response["json"]["status"], "ok")
        self.assertEqual(response["json"]["service"], "fleet-ops-desk")
        self.assertEqual(response["json"]["data_class"], "synthetic")

    def test_dashboard_endpoint(self):
        response = self.call_app("/api/dashboard")
        self.assertEqual(response["status"], "200 OK")
        self.assertEqual(response["json"]["vehicles"]["vehicles"], 18)

    def test_vehicle_endpoint_filters(self):
        response = self.call_app("/api/vehicles", "status=W%20najmie")
        self.assertEqual(response["status"], "200 OK")
        self.assertGreaterEqual(len(response["json"]), 1)
        self.assertTrue(all(row["status"] == "W najmie" for row in response["json"]))

    def test_unknown_route_returns_404(self):
        response = self.call_app("/api/not-existing")
        self.assertEqual(response["status"], "404 Not Found")
        self.assertEqual(response["body"], b"Not found")

    def test_static_path_cannot_escape_static_directory(self):
        response = self.call_app("/static/../README.md")
        self.assertEqual(response["status"], "404 Not Found")

    def test_dataset_does_not_contain_obvious_personal_identifiers(self):
        serialised = json.dumps(app.dashboard_data(), ensure_ascii=False).lower()
        for forbidden in ("pesel", "@gmail.com", "@wp.pl", "@onet.pl"):
            self.assertNotIn(forbidden, serialised)


if __name__ == "__main__":
    unittest.main()
