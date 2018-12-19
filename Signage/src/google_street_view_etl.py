import numpy as np
import geopandas as gpd
import shapely
import os
import shutil

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
        for i, _hdg in enumerate(self.headings):
            _url = GoogleStreetViewTask.__API_URL__.format(
                x=self.x
                , y=self.y
                , heading=_hdg
                , api_key=self._api_key
            )
            target_fn = self._target_paths[i]
            res.append(urlretrieve(_url, target_fn))
        return res


class GoogleStreetViewEtl:
    @classmethod
    def work(cls, it, target_dir):
        """
        takes in an iterator of tuples of x, y coordinates
        :param it: an iterator (x, y) where x and y are floats(?)
        :return: 0 if program runs without an error
        """
        for x, y in it:
            res = GoogleStreetViewTask(x, y, target_dir).get_imgs()
            print(res)
