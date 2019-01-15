import os
import unittest
from Signage.src.google_street_view_etl import GoogleStreetViewTask as GSVT
import geopandas as gpd
import numpy as np


class MyGoogleStreetViewTaskTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Mock x, y coordinates
        cls.x = -73.95899416299994
        cls.y = 40.62788559400008

    def setUp(self):
        self.gsvt = GSVT(
            MyGoogleStreetViewTaskTestCase.x
            , MyGoogleStreetViewTaskTestCase.y
            , '/Users/sunghoonyang/PycharmProjects/groundwork-detection/Signage/tmp/img'
            , **{'puma': 3701, 'fov': [30, 90], 'heading': list(np.arange(0, 360, 45))}
        )

    @unittest.skip('2019/01/01 14:11 PM;' +
                   'init works;' +
                   'comment this out if __init__ method undergoes changes'
                   )
    def test_init(self):
        gsvt = GSVT(
            MyGoogleStreetViewTaskTestCase.x
            , MyGoogleStreetViewTaskTestCase.y
            , '/Users/sunghoonyang/PycharmProjects/groundwork-detection/Signage/tmp/img'
            , **{'puma': 3701, 'fov': [100, 200], 'heading': list(np.arange(0, 360, 8))}
        )
        self.assertEquals(gsvt._api_key, os.environ['GOOGLE_API_KEY'])
        self.assertEquals(gsvt.demarcation, str(3701))

    # @unittest.skip('')
    def test_get_imgs(self):
        res = self.gsvt.get_imgs()
        print(res)


if __name__ == '__main__':
    unittest.main()
