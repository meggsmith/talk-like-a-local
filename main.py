#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import jinja2
import os

my_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('anyone home')


class SlangHandler(webapp2.RequestHandler):
    def get(self):
        slang_template=my_env.get_template("templates/location.html")
        self.response.write(slang_template.render())

    def post(self):
      def slang_finder(location):
          slang_dictionary = {'Boston':['wicked', 'pissah', 'bubbler', 'chowdah', 'lobstah'],
          'New York':['fuh-gedd-about-it', 'hipster', 'bodega', 'bridge and tunnel', 'schmear']}  
          if location == 'Boston':
            slang_list_for_location = slang_dictionary['Boston']
          elif location == 'New York':
            slang_list_for_location = slang_dictionary['New York']
          return(slang_list_for_location)

      requested_location=self.request.get('location')
      slang_list=slang_finder(requested_location)

      my_slang_dict={'user_slang':slang_list, 'output_city':requested_location}
      slang_template=my_env.get_template('templates/output.html')
      self.response.write(slang_template.render(my_slang_dict))
  
            

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/slang', SlangHandler)
], debug=True)
