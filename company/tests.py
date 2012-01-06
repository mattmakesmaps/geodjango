from django.test import TestCase

class GeoJSONTestCase(TestCase):
    def test_company_boundary(self):
        """
        Get request for a boundary.
        """
        response = self.client.get('/company/geojson/boundary/1/')
        self.assertEqual(response.status_code, 200)

class ReportTestCase(TestCase):
    def test_report_detail(self):
        """
        Get report status and map page.
        """
        response = self.client.get('/company/reports/')
        self.assertEqual(response.status_code, 200)
