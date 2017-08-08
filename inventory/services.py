import urllib.request, json 

def display_name(netid): 
	url = 'https://streamer.oit.duke.edu/ldap/people/netid/'+ netid +'?access_token=108332719d22af28cbf2a1c0cdd99371'
	with urllib.request.urlopen(url) as url:
	    data = json.loads(url.read().decode())
	    return (data[0]['display_name'])
