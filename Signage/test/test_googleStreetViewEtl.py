from unittest import TestCase
from Signage.src.google_street_view_etl import GoogleStreetViewEtl as GSVE
import geopandas as gpd
import numpy as np


class TestGoogleStreetViewEtl(TestCase):
    @classmethod
    def _get_iter(cls):
        _st_shp = gpd.read_file(
            "/Users/sunghoonyang/PycharmProjects/groundwork-detection/Signage/asset/geo_export_ce677b00-822e-465b-8b4f-aacaff026101.shp")
        mh_sts = \
            _st_shp[(_st_shp["borocode"] == "1") & (_st_shp["st_width"] > 20) & (_st_shp["st_width"] < 30)][
                'geometry']
        for street in list(mh_sts.get_values()).__reversed__():
            for i in np.arange(0, len(street.xy[0]), 5):
                x = street.xy[0][i]
                y = street.xy[1][i]
                yield x, y

    def test_work(self):
        GSVE.work(
            TestGoogleStreetViewEtl._get_iter()
            , r'/Users/sunghoonyang/Google Drive/Argo/groundwork-detection/img'
        )