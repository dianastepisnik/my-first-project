#!/usr/bin/env python

import webapp2


class MainHandler(webapp2.RequestHandler):
    def get(self):
        return self.response.write('Blabla')

app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
], debug=True)
