class StupyApi:
    def get():
        return 200

    def post(body):
        if "error" in body:
            return 400
        return 200
