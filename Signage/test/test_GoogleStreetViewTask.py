import os
import unittest
from Signage.src.google_street_view_etl import GoogleStreetViewTask as GSVE
import geopandas as gpd
import numpy as np


class MyGoogleStreetViewTaskTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        _st_shp = gpd.read_file(
            "/Users/sunghoonyang/PycharmProjects/groundwork-detection/asset/geo_export_ed93e72f-6d55-4e70-b1a6-05df5dd171e7.shp")
        mh_sts = \
            _st_shp[(_st_shp["borocode"] == "1") & (_st_shp["st_width"] > 20) & (_st_shp["st_width"] < 30)][
                'geometry']
        cls.x, cls.y = None, None
        for street in mh_sts.get_values()[range(10)]:
            for i in np.arange(0, len(street.xy[0]), 5):
                cls.x = street.xy[0][i]
                cls.y = street.xy[1][i]
                break
            break

    def setUp(self):
        self.gsve = GSVE(
            MyGoogleStreetViewTaskTestCase.x
            , MyGoogleStreetViewTaskTestCase.y
            , '/Users/sunghoonyang/PycharmProjects/groundwork-detection/tmp'
        )

    @unittest.skip('2018/12/26 13:28 PM;' +
                   'init works;' +
                   'comment this out if __init__ method undergoes changes'
                   )
    def test_init(self):
        gsve = GSVE(
            MyGoogleStreetViewTaskTestCase.x
            , MyGoogleStreetViewTaskTestCase.y
            , '/Users/sunghoonyang/PycharmProjects/groundwork-detection/tmp'
        )
        self.assertEquals(gsve._api_key, os.environ['GOOGLE_API_KEY'])
        print(gsve._target_paths)

    # @unittest.skip('')
    def test_get_imgs(self):
        res = self.gsve.get_imgs()
        print(res)


if __name__ == '__main__':
    unittest.main()
