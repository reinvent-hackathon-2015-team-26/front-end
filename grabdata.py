# A simple retrieval program to retrive data from rapidpro to AWS S3

# https://fr9ph8ccpi.execute-api.us-west-2.amazonaws.com/prod/getTeamList?team=1
# https://fr9ph8ccpi.execute-api.us-west-2.amazonaws.com/prod/addUser?team=1
# https://fr9ph8ccpi.execute-api.us-west-2.amazonaws.com/prod/addUser?phone=12345&latitude=12345&longitude=54321&name=testkl&team=1&vaccine=flue&visit=12345678
# https://github.com/rapidpro/rapidpro-python

import datetime
from temba_client.client import TembaClient
from geopy.geocoders import Nominatim
from urlparse import urlunparse, urlparse
import urllib2

# url = "https://fr9ph8ccpi.execute-api.us-west-2.amazonaws.com/prod/addUser?team=1"
client = TembaClient('rapidpro.io', '<insert key>')

fifteen = datetime.datetime.now() - datetime.timedelta(hours=-5, minutes=10)
print fifteen.isoformat()
timestamp = fifteen.isoformat()
# quit()

# post type I only.
# 'archived', 'broadcast', 'contact', 'create', 'created_on', 'delivered_on', 
# 'deserialize', 'deserialize_list', 'direction', 'id', 'labels', 'sent_on', 
# 'status', 'text', 'type', 'urn'

# https://fr9ph8ccpi.execute-api.us-west-2.amazonaws.com/prod/addUser?
# phone=12345
# &latitude=12345
# &longitude=54321
# x&name=testkl
# &team=1
# x&vaccine=flue
# &visit=0

for message in client.get_messages(after=timestamp, labels='address'):
	# print dir(message)0
	print(message.id)
	print(message.text)
	print "contact"
	print message.contact
	# print(dir(client.get_contact(uuid=message.contact)))
	
	geolocator = Nominatim()
	myAddress = str(message.text)

	location = geolocator.geocode(myAddress)
	print(location.address)
	print((location.latitude, location.longitude))


	
	latitude = location.latitude
	longitude = location.longitude
	name = client.get_contact(uuid=message.contact).name
	team = 1
	vaccine = "flu"
	visit = 0

	# can't get phone number, don't know where to get. 
	phone = name

	# phone = message.contact
	# print(message.type)
	# print(message.created_on)
	# 'count', 'create', 'deserialize', 'deserialize_list', 'name', 'uuid'
	# for label in client.get_labels():
	# 	# print dir(label)
	# 	print label.name
	# print timestamp

	url = "https://fr9ph8ccpi.execute-api.us-west-2.amazonaws.com/prod/addUser?phone="+str(phone)+"&latitude="+str(latitude)+"&longitude="+str(longitude)+"&name="+str(name)+"&team="+str(team)+"&vaccine="+str(vaccine)+"&visit="+str(visit)+""
	print urllib2.urlopen(url)
	# print url
	# print(urlparse(url))

	# response = s.urlopen(url)
# 
# print urlunparse("test.com")

