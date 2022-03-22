class Request:
	def __init__(self, environ, start_response):
  	self.environ = environ
    self.http_host = environ['HTTP_HOST']
    self.http_user_agent = environ['HTTP_USER_AGENT']
    self.lang = environ.get('LANG')
    self.method = environ.get('REQUEST_METHOD')
    self.path = environ.get('PATH_INFO')
		self.host_address = environ.get('HTTP_HOST')
    self.gateway_interface = environ.get('GATEWAY_INTERFACE')
    self.server_port = environ.get('SERVER_PORT')
    self.remote_host = environ.get('REMOTE_HOST')
    self.content_type = environ.get('CONTENT_TYPE')
    self.content_length = environ.get('CONTENT_LENGTH')
    self.body = environ.get('BODY')
    self.query_string = environ.get('QUERY_STRING')
    self.server_protocol = environ.get('SEVER_PROTOCOL')
    self.server_software = environ.get('SERVER_SOFTWARE')
		self.start_response = start_response
    self.parse_qs()

	def parse_qs(self):
		