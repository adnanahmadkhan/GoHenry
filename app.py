import requests
import flask


app = flask.Flask(__name__)


class PaginateResponse:

    def __init__(self, request, last_page):
        self.request = request
        self.last_page = last_page

    def get_next_page(self):
        """
        Returns the next page.
        If current page is equal or greater than the last page returns None
        else increments the page number and return full url for next page.
        """
        args = dict(self.request.args)

        if args.get('page'):
            if int(args.get('page')) >= self.last_page:
                return None

            args['page'] = int(args['page']) + 1
            next_page_request = requests.Request(
                'GET',
                self.request.base_url,
                params=args
            ).prepare()

            return next_page_request.url
        else:
            args['page'] = 2
            next_page_request = requests.Request(
                'GET',
                self.request.base_url,
                params=args
            ).prepare()
            return next_page_request.url

    def get_previous_page(self):
        """
        Returns the previous page.
        If current page is greater than last page returns None
        else decrements the page number and return full url for previous page.
        """
        args = dict(self.request.args)
        if args.get('page'):
            if int(args.get('page')) == 1 \
                    or int(args['page']) > self.last_page:
                return None

            args['page'] = int(args['page']) - 1
            prev_page_request = requests.Request(
                'GET',
                self.request.base_url,
                params=args
            ).prepare()

            return prev_page_request.url
        else:
            return None

    def get_first_page(self):
        args = dict(self.request.args)
        args['page'] = 1

        first_page_request = requests.Request(
            'GET',
            self.request.base_url,
            params=args
        ).prepare()

        return first_page_request.url

    def get_last_page(self):
        args = dict(self.request.args)
        args['page'] = self.last_page

        last_page_request = requests.Request(
            'GET',
            self.request.base_url,
            params=args
        ).prepare()

        return last_page_request.url


@app.route('/')
def index():
    return "Welcome to ad campaign api!"


@app.route('/campaign_statistics')
def campaign_statistics():
    if flask.request.headers.get('api_key') == 'uHL6FHwsIXgk8ke3uAdNNg':
        if flask.request.args.get('page'):
            if int(flask.request.args.get('page')) > 10:
                return "Not found", 404

        paginate_response = PaginateResponse(flask.request, 10)
        with open('campaign_statistics.json') as fp:
            response = {
                "records": fp.read(),
                "links": [
                    {"self": flask.request.url},
                    {"next": paginate_response.get_next_page()},
                    {"prev": paginate_response.get_previous_page()},
                    {"first": paginate_response.get_first_page()},
                    {"last": paginate_response.get_last_page()}
                ]
            }
            return flask.jsonify(response)
    else:
        return "Unauthorized", 401


@app.route('/campaigns')
def campaigns():
    if flask.request.headers.get('api_key') == 'uHL6FHwsIXgk8ke3uAdNNg':
        if flask.request.args.get('page'):
            if int(flask.request.args.get('page')) > 10:
                return "Not found", 404

        paginate_response = PaginateResponse(flask.request, 10)
        with open('campaigns.json') as fp:
            response = {
                "records": fp.read(),
                "links": [
                    {"self": flask.request.url},
                    {"next": paginate_response.get_next_page()},
                    {"prev": paginate_response.get_previous_page()},
                    {"first": paginate_response.get_first_page()},
                    {"last": paginate_response.get_last_page()}
                ]
            }
            return flask.jsonify(response)
    else:
        return "Unauthorized", 401


@app.route('/creatives')
def creatives():
    if flask.request.headers.get('api_key') == 'uHL6FHwsIXgk8ke3uAdNNg':
        if flask.request.args.get('page'):
            if int(flask.request.args.get('page')) > 10:
                return "Not found", 404

        paginate_response = PaginateResponse(flask.request, 10)
        with open('creatives.json') as fp:
            response = {
                "records": fp.read(),
                "links": [
                    {"self": flask.request.url},
                    {"next": paginate_response.get_next_page()},
                    {"prev": paginate_response.get_previous_page()},
                    {"first": paginate_response.get_first_page()},
                    {"last": paginate_response.get_last_page()}
                ]
            }
            return flask.jsonify(response)
    else:
        return "Unauthorized", 401
