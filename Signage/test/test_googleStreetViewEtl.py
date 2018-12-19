from unittest import TestCase
from Signage.src import GoogleStreetViewEtl as GSVE
import geopandas as gpd
import numpy as np


class TestGoogleStreetViewEtl(TestCase):
    @classmethod
    def _get_iter(cls):
        _st_shp = gpd.read_file(
            "/Users/sunghoonyang/PycharmProjects/groundwork-detection/asset/geo_export_ed93e72f-6d55-4e70-b1a6-05df5dd171e7.shp")
        mh_sts = \
            _st_shp[(_st_shp["borocode"] == "1") & (_st_shp["st_width"] > 20) & (_st_shp["st_width"] < 30)][
                'geometry']
        for street in mh_sts.get_values():
            for i in np.arange(0, len(street.xy[0]), 5):
                x = street.xy[0][i]
                y = street.xy[1][i]
                yield x, y

    def test_work(self):
        GSVE.work(
            TestGoogleStreetViewEtl._get_iter()
            , r'/Users/sunghoonyang/Google Drive/Argo/groundwork-detection/img'
        )