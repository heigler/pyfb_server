#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import with_statement
import re
import os
import json
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from pyfb_server import settings

class FBHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        data_path = os.path.join(settings.BASE_PATH, 'data')
        
        # user base info
        if re.match(settings.GH_USER_URL, self.path):
            user_data_file = os.path.join(data_path, 'users.json')
            with open(user_data_file, 'r') as userfile:
                user_data = json.loads(userfile.read())
            
            user_id = re.match(settings.GH_USER_URL, self.path).group()[1:]
            try:
                user = user_data['user%s' %user_id[-1]]
            except KeyError:
                self.send_error(404, 'user does not exist')
                return False
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(user))
        
        return True
        
        
class FBServer(object):
    
    def __init__(self):
        pass
    
    
    def start(self, server_port=settings.SERVER_PORT):
        try:
            server = HTTPServer(('', server_port), FBHandler)
            print 'starting FBServer...'
            server.serve_forever()
        except KeyboardInterrupt:
            print 'FBServer stoped.'
            server.socket.close()
            
            
if __name__ == '__main__':
    sv = FBServer()
    sv.start()