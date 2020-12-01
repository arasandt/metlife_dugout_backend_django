class JSONTranslationMiddleware:
    def __init__(self, get_response):
        # called when app first starts.
        self.get_response = get_response

    def __call__(self, request):
        # called for each request.
        print("inside middleware call")
        response = self.get_response(request)
        return response