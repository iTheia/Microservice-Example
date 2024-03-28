DEFAULT_LIMIT = 10
DEFAULT_PAGE = 0

class Pager:

  def __init__(self, **kwargs) -> None:
    self.req_params = kwargs

  def paginate(self):
    return {
      **self._get_pagionation_options(),
      'filters': self._get_filters()
    }

  def _get_pagionation_options(self):
    page_number = int(self.req_params.get('page', DEFAULT_PAGE))
    limit = int(self.req_params.get('limit', DEFAULT_LIMIT))

    return {
      'limit': limit,
      'offset': limit * page_number,
    }

  def _get_filters(self):
    filters = []
    for key, value in self.req_params.items():
        if key.startswith('filter_'):
            field_name = key[len('filter_'):]
            filters.append({'field': field_name, 'filter': value})
    return filters

