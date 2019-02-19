def extract_areas(data):
  is_list = isinstance(data, list)
  is_area = 'children' in data

  if is_list:
    areas = []
    for item in data:
      areas += extract_areas(item)
    return areas

  elif is_area:
    return [data]

  return []


def extract_routes(data):
  is_list = isinstance(data, list)
  is_area = 'children' in data

  if is_list:
    areas = []
    for item in data:
      areas += extract_areas(item)
    return areas

  elif is_area:
    return extract_routes(data['children'])

  return [data]