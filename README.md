# ezgiphy 0.0.3

#### A wrapper for the Giphy public API.
A package wrapper for the Giphy public API that allows you to work with all Giphy API endpoints.



Installing using pip
```
pip install ezgiphy
```

### Examples

```python
from ezgiphy import GiphyPublicAPI

giphy = GiphyPublicAPI('<giphy-api-key>')

```
#### Phrase search
Search all Giphy GIFs for a word or phrase. Supported parameters:
- q : Search query term or phrase (required).
- limit :  The maximum number of records to return.
- offset: An optional results offset.
- rating: Filters results by rating (g/pg/pg-13/r)
- lang: specify default country for regional content.

```python
giphy.search(q='something',limit=25,rating='g')
```

#### Translate search
Experimental search endpoint for gif dialects. Supported parameters:
- s : Search query term or phrase (required).

```python
giphy.translate(s='something')
```

#### Trending gifs
Get all trending gifs. Supported parameters:

- limit: The maximum number of records to return. 
- rating: Filters results by rating (g/pg/pg-13/r),

```python
giphy.trending(limit=25,rating='g')
```

#### Random gifs
Random gif(s) filtered by tag. Supported parameters:

- tag: The maximum number of records to return.
- rating: Filters results by rating (g/pg/pg-13/r).
```python
giphy.random(tag='something',rating='g')
```
#### Giphy Id search
Search Giphy gifs for a single Id. Supported parameters:

- id: Filter result by specific gif id (required).

```python
giphy.get_by_id(id='some id')
```

#### Search by ids 
Search all Giphy gifs for  an list of Id's. Supported parameters:

- ids: List of specific ids (required).
```python
giphy.get_by_ids(ids=['id one','id two','id three'])
```
<h3 style="color:red">Giphy Stickers functionalities will available in next version.</h3>.


