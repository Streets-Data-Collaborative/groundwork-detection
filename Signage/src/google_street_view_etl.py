import time
from datetime import datetime
from itertools import product
import os
import logging

try:
    from urllib import urlretrieve as urlretrieve
except ImportError:
    from urllib.request import urlretrieve as urlretrieve


class GoogleStreetViewTask:
    __HEADINGS__ = [90, 180, 270, 0]
    __FOV__ = [90]
    __PITCH__ = [10]
    __API_URL__ = "https://maps.googleapis.com/maps/api/streetview" + \
                  "?size=600x600" + \
                  "&location={y},{x}" + \
                  "&fov={fov}" + \
                  "&heading={heading}" + \
                  "&pitch={pitch}" + \
                  "&key={api_key}"

    def __init__(self
                 , x
                 , y
                 , target_dir
                 , **kwargs):
        """
        Creates a task object whose granularity of Image Generation is
            * X coordinates in GCS North American 1983 StatePlane Long Island
            * Y coordinates in GCS North American 1983 StatePlane Long Island
            * FOV, PITCH, HEADING if provided. The default granularity is given as Class Var. above
        :param x: x coordinate for URL request
        :param y: y coordinate for URL request
        :param target_dir: target dir root. if puma is provided to target_dir, puma is the first lvl sub directory
        :param kwargs: supports
            *  fov as an iterable: zoom level
            *  heading as an iterable: orientation of the view
            *  pitch as an iterable: angle of view from the ground
            TODO: Support instantiation with an iterable when the user does not want cartesian product of above kwarg iterables
        """
        self._api_key = os.environ['GOOGLE_API_KEY']
        self.x = x
        self.y = y
        self.target_dir = target_dir
        """
        An Empty string is the default value 
        This is compatible with os.path.join()"
            os.path.join('x', '', 'y')
            Out[34]: 
            'x/y'
        """
        self.puma = ''
        if 'puma' in kwargs.keys():
            self.puma = str(kwargs['puma'])

        """
        Below arguments will be used to create n-d permutation of 
            fov, pitch, headings 
        so the size will be the multiple of the three lists
        """
        if 'fov' in kwargs.keys():
            fov = kwargs['fov']
        else:
            fov = GoogleStreetViewTask.__FOV__
        if 'pitch' in kwargs.keys():
            pitch = kwargs['pitch']
        else:
            pitch = GoogleStreetViewTask.__PITCH__
        if 'heading' in kwargs.keys():
            heading = kwargs['heading']
        else:
            heading = GoogleStreetViewTask.__HEADINGS__

        self._wrk = map(lambda t: dict(zip(('fov', 'pitch', 'heading'), t)), product(fov, pitch, heading))

    def get_imgs(self):
        res = []
        _err_cnt = 0
        for i, d in enumerate(self._wrk):
            _url = GoogleStreetViewTask.__API_URL__.format(
                x=self.x
                , y=self.y
                , api_key=self._api_key
                , **d
            )
            target_dir = os.path.join(
                self.target_dir
                , self.puma
            )
            target_fn = os.path.join(
                target_dir
                , "{y}_{x}_f{fov}_p{pitch}_h{heading}.png".format(
                    x=self.x
                    , y=self.y
                    , **d
                )
            )
            try:
                os.makedirs(target_dir, exist_ok=True)
                res.append(urlretrieve(_url, target_fn)[1])
            except Exception as e:
                logging.error('Coordinates %s, %s will be skipped. Retrying after one second delay: ' % (
                    str(self.x), str(self.y)) + str(e))
                time.sleep(1)
                _err_cnt += 1
                if _err_cnt > 10:  # TODO: Make this a variable not a hard-coded 10
                    raise e
                continue
        return res


class GoogleStreetViewEtl:
    @classmethod
    def work(cls, it, target_dir):
        """
        takes in an iterator of tuples of x, y coordinates, and third element is the kwargs
        :param it: an iterator (x, y) where x and y are floats(?)
        :param target_dir: directory in which images will be written
        :return: 0 if program runs without an error
        """
        logging.basicConfig(
            level=logging.INFO,
            filename="/Users/sunghoonyang/PycharmProjects/groundwork-detection/Signage/tmp/log/%s.log" % datetime.strftime(
                datetime.now(), 'GSVE_ETL_%Y%m%d%H%M%S'),
            filemode='w',
            format='%(asctime)s %(message)s',
        )
        logging.info('Starting ETL @ %s...' % datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S'))
        _t: tuple
        for i, _t in enumerate(it):
            kwargs = {}
            if len(_t) > 2:
                x, y, kwargs = _t
            else:
                x, y = _t

            _ = GoogleStreetViewTask(x, y, target_dir, **kwargs).get_imgs()
            if i % 1000 == 0:
                logging.info('%d * 4 images downloaded' % i)

        logging.info('Terminating ETL...')
        return 0
