from django.test import TestCase

class GeoJSONTestCase(TestCase):
    def test_gps_point(self):
        """
        Generate get request for a GPS point.
        """
        response = self.client.get('/gps/geojson/points/3/')
        self.assertEqual(response.status_code, 200)
