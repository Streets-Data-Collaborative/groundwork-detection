from unittest import TestCase
from Signage.src.google_street_view_etl import GoogleStreetViewEtl as GSVE
import geopandas as gpd
import numpy as np
import random

class TestGoogleStreetViewEtl(TestCase):
    @classmethod
    def _get_iter(cls):
        _st_shp = gpd.read_file(
            "/Users/sunghoonyang/PycharmProjects/groundwork-detection/Signage/asset/geo_export_ce677b00-822e-465b-8b4f-aacaff026101.shp")
        mh_sts = \
            _st_shp[(_st_shp["borocode"] == "2") & (_st_shp["st_width"] > 20) & (_st_shp["st_width"] < 30)][
                'geometry']
        for street in list(mh_sts.get_values()).__reversed__():
            for i in np.arange(0, len(street.xy[0]), 5):
                x = street.xy[0][i]
                y = street.xy[1][i]
                yield x, y

    @classmethod
    def _get_puma_iter(cls):
        _raw = gpd.read_file(
            r"/Users/sunghoonyang/Google Drive/Argo/groundwork-detection/intersection_dta/StreetsOnlyGCSNA1983/OnStreetOnlyGCSNA1983.shp")
        # random sampling from the population of intersection coordinates
        # in the below set up each coordinate pair will create 6 * 2 = 12 images
        _x_shp = _raw.loc[random.sample(range(0, _raw.size), 2000), :]
        for ix, _row in _x_shp.iterrows():
            puma, pt = _row
            if pt is np.nan:
                continue
            yield pt.x, pt.y, {'puma': puma, 'fov': [30, 90], 'heading': list(np.arange(0, 360, 60))}

    def test_iter_work(self):
        GSVE.work(
            TestGoogleStreetViewEtl._get_iter()
            , r'/Users/sunghoonyang/Google Drive/Argo/groundwork-detection/img'
        )

    def test_puma_iter_work(self):
        GSVE.work(
            TestGoogleStreetViewEtl._get_puma_iter()
            , r'/Users/sunghoonyang/Google Drive/Argo/groundwork-detection/img'
        )