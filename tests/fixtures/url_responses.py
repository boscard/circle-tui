import re, json, os
from urllib.parse import urlparse
from tests import FIXTURES_DIR

prefix = '/api/v1.1'

# '/endpoint': (status, headers, response_body_filename)
endpoints = {
    '/me': (200, {}, 'me.json'),
    '/projects': (200, {}, 'projects.json'),
    '/project/((\w+)*)/((\w+)*)/((\w+)*)/((\w+)*)/((\w+)*)/((\w+)*)': (200, {}, 'log_example'),
    '/project/((\w+)*)/((\w+)*)/((\w+)*)/((\w+)*)': (200, {}, 'build.json'),
}

def cached_response(request):
    parsed_uri = urlparse(request.url)
    request_endpoint = parsed_uri.path[len(prefix):]

    for endpoint, values in endpoints.items():
        if re.match(endpoint, request_endpoint):
            filename = os.path.join(FIXTURES_DIR, values[2])
            with open(filename) as body:
                return values[0], values[1], body.read()
