import time
from datetime import datetime

import numpy as np
import geopandas as gpd
import shapely
import os
import shutil

import logging

try:
    from urllib import urlretrieve as urlretrieve
except ImportError:
    from urllib.request import urlretrieve as urlretrieve


class GoogleStreetViewTask:
    __HEADINGS__ = [90, 180, 270, 0]
    __API_URL__ = "https://maps.googleapis.com/maps/api/streetview" + \
                  "?size=600x600" + \
                  "&location={y},{x}" + \
                  "&fov=90" + \
                  "&heading={heading}" + \
                  "&pitch=10" + \
                  "&key={api_key}"

    def __init__(self, x, y, target_dir, headings=None):
        self._api_key = os.environ['GOOGLE_API_KEY']
        self.x = x
        self.y = y
        self.headings = headings if headings else GoogleStreetViewTask.__HEADINGS__
        self._target_paths = [
            os.path.join(
                target_dir
                , "{y}_{x}_{heading}.png".format(
                    x=self.x
                    , y=self.y
                    , heading=heading
                ))
            for heading in self.headings
        ]

    def get_imgs(self):
        res = []
        _err_cnt = 0
        for i, _hdg in enumerate(self.headings):
            _url = GoogleStreetViewTask.__API_URL__.format(
                x=self.x
                , y=self.y
                , heading=_hdg
                , api_key=self._api_key
            )
            target_fn = self._target_paths[i]
            try:
                res.append(urlretrieve(_url, target_fn))
            except Exception as e:
                logging.error('Coordinates %s, %s will be skipped. Retrying after one second delay: ' % (self.x, self.y) + str(e))
                time.sleep(1)
                _err_cnt += 1
                if _err_cnt > 10: # TODO: Make this a variable not a hard-coded 10
                    raise e
                continue
        return res


class GoogleStreetViewEtl:
    @classmethod
    def work(cls, it, target_dir):
        """
        takes in an iterator of tuples of x, y coordinates
        :param it: an iterator (x, y) where x and y are floats(?)
        :return: 0 if program runs without an error
        """
        logging.basicConfig(
            level=logging.INFO,
            filename="/Users/sunghoonyang/PycharmProjects/groundwork-detection/Signage/tmp/log/%s.log" % datetime.strftime(datetime.now(), 'GSVE_ETL_%Y%m%d%H%M%S'),
            filemode='w',
            format='%(asctime)s %(message)s',
        )
        logging.info('starting ETL...')
        for i, _t in enumerate(it):
            x, y = _t
            res = GoogleStreetViewTask(x, y, target_dir).get_imgs()
            print(res)
            if i % 1000 == 0:
                logging.info('%d * 4 images downloaded' % i)
