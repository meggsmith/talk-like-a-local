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
import webapp2 #lines 17-19 are imported libraries 
import jinja2
import os

my_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('anyone home')


class SlangHandler(webapp2.RequestHandler): #newly created handler to process slang_finder method and rendering our output.html page
    def get(self): #the get request
        slang_template=my_env.get_template("templates/location.html") #the route to the form template, using Jinja2 magic
        self.response.write(slang_template.render()) #the request to render the form template that uses the Jinga2 magic

    def post(self): #the post request
      def slang_finder(location): #the slang_finder method that will take the action on our user input to take in the location parameter's arguemnt and output the slang list for that location
          slang_dictionary = {'Boston':['wicked', 'pissah', 'bubbler', 'chowdah', 'lobstah'],
          'New York':['fuh-gedd-about-it', 'hipster', 'bodega', 'bridge and tunnel', 'schmear']}  #lines 39 - 40 are the hard coded dictionaries of relevant slang for possible location arguments
          if location == 'Boston':
            slang_list_for_location = slang_dictionary['Boston']
          elif location == 'New York':
            slang_list_for_location = slang_dictionary['New York']
          return(slang_list_for_location) #lines 41 -45 are the conditional statements that determine the location arguments (inputs) and decide which slang list dictionary to select to show the user

      requested_location=self.request.get('location') #newly created variable to extract the location parameter from the input form....aka the get request
      slang_list=slang_finder(requested_location) #newly created variable to use the method on the users chosen location

      my_slang_dict={'user_slang':slang_list, 'output_city':requested_location} #newly created dictionary assiging new variables - slang_list and requested_location - that will eventually be shown to the user
      slang_template=my_env.get_template('templates/output.html') #the newly created variable that contains the output template. This holds the output.html page - the holding cotainer ready to render the write response.
      self.response.write(slang_template.render(my_slang_dict)) #code to render the output template passing the dictionary of variables to display to the user
  
            

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/slang', SlangHandler) #root url to render/display the page using the localhost
], debug=True)
