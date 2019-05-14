class Response:
     # 2xx
    @staticmethod
    def success(data,statuscode):
         return {'status': 'success', 'data': data}, statuscode
    # 3xx
    @staticmethod
    def redirect(data,statuscode):
         return {'status': 'redirect', 'data': data}, statuscode
     #4xx
    @staticmethod
    def error(data,statuscode):
         return {'status': 'error', 'data': data}, statuscode
