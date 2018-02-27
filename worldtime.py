#!/bin/python

import sys
from flask import Flask
import json



class City:
	def __init__(self):
		self.valid = False

	def parse(self, line, country_code_name_map, state_name_map, timezones_offset_map):
		fields = line.split('\t')
		self.geonameid = fields[0]
		self.name = fields[1].lower()
		self.asciiname = fields[2].lower()
		self.alternatenames = fields[3].split('\t')
		self.lat = fields[4]
		self.lng = fields[5]
		self.contrycode = fields[8]
		self.admin1code = fields[10]
		self.timezone = fields[17]
		self.valid = True

		if country_code_name_map.has_key(self.contrycode):
			self.contryname = country_code_name_map[self.contrycode]

		code = '%s.%s' % (self.contrycode, self.admin1code)
		if state_name_map.has_key(code):
			self.statename = state_name_map[code]

		if timezones_offset_map.has_key(self.timezone):
			self.timezone_offset = timezones_offset_map[self.timezone]


	def info(self):
		return '%s, %s, %s, %s(%f)' % (self.asciiname, self.statename, self.contryname, self.timezone, self.timezone_offset)


def parse_contries(country_filename):
	f = open(country_filename)
	lines = f.readlines()
	country_code_name_map = {}
	for line in lines:
		if not line.startswith('#'):
			fields = line.split('\t')
			country_code, country_ascii_name = fields[0], fields[4]
			country_code_name_map[country_code] = country_ascii_name
	return  country_code_name_map



def parse_states(state_filename):
	f = open(state_filename)
	lines = f.readlines()
	state_name_map = {}

	for line in lines:
		fields = line.split('\t')
		code, asciiname = fields[0], fields[2]
		state_name_map[code] = asciiname

	return state_name_map


def parse_cities(city_filename, country_code_name_map, state_name_map, timezones_offset_map):
	f = open(city_filename)
	lines = f.readlines()
	cities_name_map = {}
	cities = []

	for line in lines:
		city = City()
		city.parse(line, country_code_name_map, state_name_map, timezones_offset_map)
		cities.append(city)
		if not cities_name_map.has_key(city.asciiname):
			cities_name_map[city.asciiname] = []
		cities_name_map[city.asciiname].append(city)

	return cities_name_map

def parse_timezones(timezones_filename):
	f = open(timezones_filename)
	lines = f.readlines()
	timezones_offset_map = {}
	for line in lines:
		if not line.startswith('#'):
			fields = line.split('\t')
			timezoneId = fields[1]
			offset = float(fields[2])
			timezones_offset_map[timezoneId] = offset
	return timezones_offset_map



def test():
	country_code_name_map = parse_contries('./countryInfo.txt')
	state_name_map = parse_states('./admin1CodesASCII.txt')
	timezones_offset_map = parse_timezones('./timeZones.txt')
	cities_name_map = parse_cities('./cities15000.txt', country_code_name_map, state_name_map, timezones_offset_map)

	selected_cityname = sys.argv[1].lower()

	if cities_name_map.has_key(selected_cityname):
		selected_cities = cities_name_map[selected_cityname.lower()]
	else:
		print 'no such city'
		return

	for selected_city in selected_cities:
		print selected_city.info()



if __name__ == '__main__':
	test()


#initialization
country_code_name_map = parse_contries('./countryInfo.txt')
state_name_map = parse_states('./admin1CodesASCII.txt')
timezones_offset_map = parse_timezones('./timeZones.txt')
cities_name_map = parse_cities('./cities15000.txt', country_code_name_map, state_name_map, timezones_offset_map)



app = Flask(__name__)


@app.route("/")
def index():
	default_city_names = (
		'SAN FRANCISCO',
		'LONDON',
		'BERLIN',
		'BEIJING',
		'SEOUL',
		'TOKYO',
		'SINGAPORE',
		'NEW YORK'
		)
	response = []

	for default_city_name in default_city_names:
		city_name = default_city_name.lower()
		if cities_name_map.has_key(city_name):
			cities = cities_name_map[city_name]
			for city in cities:
				d = {
				'name' : city.asciiname.lower(),
				'state' : city.statename,
				'country_name' : city.contryname,
				'timezone' : city.timezone,
				'timezone_offset' : city.timezone_offset
				}
			response.append(d)

	return json.dumps(response)






