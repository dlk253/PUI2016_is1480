import sys
import json
import urllib2 

# mtaKey = "6a40826c-4f43-4d81-834d-c20d8dc72a1d"
mtaKey = sys.argv[1]
busLine = sys.argv[2]

# format response url with api key and bus line variables from command line input
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(mtaKey, busLine)

# load api response data into python dict
response = urllib2.urlopen(url)
data = response.read().decode("utf-8")
busDict = json.loads(data)

# set variable to access individual bus data in nested dict structure
activeBusData = busDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

busName = activeBusData[0]['MonitoredVehicleJourney']['PublishedLineName']
busCount = 0
locations = ""

# get lat/lon for each active bus, and total count
for i in activeBusData:
	lat = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
	lon = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
	locations = locations + "Bus " + str(busCount) + " is at latitude " + str(lat) + " and longitude " + str(lon) + "\n"
	busCount+=1

# format output
print "Bus Line : " + busName
print "Number of Active Buses : " + str(busCount)
print locations