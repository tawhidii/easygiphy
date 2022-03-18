import json
from urllib import parse, request
from errors import APIKeyError, RequiredError
from constants import PUBLIC_API_URL, STICKER_API_URL


class APIBase:
    """
    Base class for API initializer.
    """

    def __init__(self, api_key=None):
        self.api_key = api_key
        if api_key is None:
            raise APIKeyError
        self.params = {
            'api_key': self.api_key
        }


class GiphyPublicAPI(APIBase):
    """
    Wrapper class for Giphy public api.
    You can find api key from https://developers.giphy.com/dashboard/
    """

    def __get_json(self, url, sort_key=False, indent=4):
        """

        :param url: Giphy api endpoint with query parameters.
        :param sort_key:Sorting the keys when dumping saves the key-value pairs in
        alphabetical order by keys.
        :param indent:The indent parameter specifies the spaces that
         are used at the beginning of a line. By default, it's value is 4.

        """
        with request.urlopen(url) as response:
            data = json.loads(response.read())
        return json.dumps(obj=data, sort_keys=sort_key, indent=indent)

    def search(self, **kwargs):
        """

        :param q: Search query term or phrase (required).
        :param limit: The maximum number of records to return.
        :param offset: An optional results offset.
        :param rating: Filters results by rating (g/pg/pg-13/r)
        :param lang: specify default country for regional content.
        """
        if kwargs:
            self.params.update(**kwargs)
        params = parse.urlencode(self.params)
        url = "".join((PUBLIC_API_URL, '/search', '?', params))
        return self.__get_json(url)

    def translate(self, **kwargs):
        """
        :param s:  Search query term or phrase (required).

        """
        if kwargs:
            self.params.update(kwargs)
        params = parse.urlencode(self.params)
        url = "".join((PUBLIC_API_URL, '/translate', '?', params))
        return self.__get_json(url)

    def trending(self, **kwargs):
        """
        :param limit: The maximum number of records to return.
        :param rating: Filters results by rating (g/pg/pg-13/r)
        """
        if kwargs:
            self.params.update(kwargs)
        params = parse.urlencode(self.params)
        url = "".join((PUBLIC_API_URL, '/trending', '?', params))
        return self.__get_json(url)

    def random(self, **kwargs):
        """
        :param tag: The maximum number of records to return.
        :param rating: Filters results by rating (g/pg/pg-13/r)
        """
        if kwargs:
            self.params.update(kwargs)
        params = parse.urlencode(self.params)
        url = "".join((PUBLIC_API_URL, '/random', '?', params))
        return self.__get_json(url)

    def get_by_id(self, id=None):
        """
        :param id: Filter result by specific gif id (required).
        """
        if id is None:
            raise RequiredError('id')
        params = parse.urlencode(self.params)
        url = "".join((PUBLIC_API_URL, f'/{id}', '?', params))
        return self.__get_json(url)

    def get_by_ids(self, ids=[]):
        """
        :param ids: List of specific ids (required).
        """
        if len(ids) < 0:
            raise RequiredError('list of ids')
        params = parse.urlencode(self.params)
        url = "".join((PUBLIC_API_URL, '?', params, f"{'&ids='}", "%2C".join(ids)))
        return self.__get_json(url)


class GiphyStickerAPI(APIBase):
    """
      Wrapper class for Giphy sticker api.
      You can find api key from https://developers.giphy.com/dashboard/
      """

    def __get_json(self, url, sort_key=False, indent=4):
        """

        :param url: Giphy api endpoint with query parameters.
        :param sort_key:Sorting the keys when dumping saves the key-value pairs in
        alphabetical order by keys.
        :param indent:The indent parameter specifies the spaces that
         are used at the beginning of a line. By default, it's value is 4.

        """
        with request.urlopen(url) as response:
            data = json.loads(response.read())
        return json.dumps(obj=data, sort_keys=sort_key, indent=indent)

    def search(self, **kwargs):
        """

        :param q: Search query term or phrase (required).
        :param limit: The maximum number of records to return.
        :param offset: An optional results offset.
        :param rating: Filters results by rating (g/pg/pg-13/r)
        :param lang: specify default country for regional content.
        """
        if kwargs:
            self.params.update(**kwargs)
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, '/search', '?', params))
        return self.__get_json(url)

    def translate(self, **kwargs):
        """
        :param s:  Search query term or phrase (required).

        """
        if kwargs:
            self.params.update(kwargs)
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, '/translate', '?', params))
        return self.__get_json(url)

    def trending(self, **kwargs):
        """
        :param limit: The maximum number of records to return.
        :param rating: Filters results by rating (g/pg/pg-13/r)
        """
        if kwargs:
            self.params.update(kwargs)
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, '/trending', '?', params))
        return self.__get_json(url)

    def random(self, **kwargs):
        """
        :param tag: The maximum number of records to return.
        :param rating: Filters results by rating (g/pg/pg-13/r)
        """
        if kwargs:
            self.params.update(kwargs)
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, '/random', '?', params))
        return self.__get_json(url)

    def get_by_id(self, id=None):
        """
        :param id: Filter result by specific gif id (required).
        """
        if id is None:
            raise RequiredError('id')
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, f'/{id}', '?', params))
        return self.__get_json(url)

    def get_by_ids(self, ids=[]):
        """
        :param ids: List of specific ids (required).
        """
        if len(ids) < 0:
            raise RequiredError('list of ids')
        params = parse.urlencode(self.params)
        url = "".join((STICKER_API_URL, '?', params, f"{'&ids='}", "%2C".join(ids)))
        return self.__get_json(url)


test = GiphyStickerAPI(api_key='uSuEHJwr1wWxxNo46TjdTh9ROTl5Fcjt')
res = test.random(tag='ukraine')
print(res)
