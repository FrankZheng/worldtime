#!/bin/python

import sys

class City:
	def __init__(self):
		self.valid = False

	def parse(self, line, country_code_name_map, state_name_map):
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
		

	def info(self):
		return '%s, %s, %s' % (self.asciiname, self.statename, self.contryname)


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


def parse_cities(city_filename, country_code_name_map, state_name_map):
	f = open(city_filename)
	lines = f.readlines()
	cities_name_map = {}
	cities = []

	for line in lines:
		city = City()
		city.parse(line, country_code_name_map, state_name_map)
		cities.append(city)
		if not cities_name_map.has_key(city.asciiname):
			cities_name_map[city.asciiname] = []
		cities_name_map[city.asciiname].append(city)

	return cities_name_map


	





if __name__ == '__main__':

	country_code_name_map = parse_contries('./countryInfo.txt')

	state_name_map = parse_states('./admin1CodesASCII.txt')

	cities_name_map = parse_cities('./cities15000.txt', country_code_name_map, state_name_map)

	selected_cityname = sys.argv[1]

	selected_cities = cities_name_map[selected_cityname.lower()]
	for selected_city in selected_cities: 
		print selected_city.info()
    
