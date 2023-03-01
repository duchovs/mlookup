import sys
import requests
import json


if len(sys.argv) == 1:
    title = "the rundown"
#    raise Exception('No arguments provided')
elif len(sys.argv) == 2:
    title = sys.argv[1]
elif len(sys.argv) > 2:
    raise Exception('Too many arguments provided')

IP = "raspi:7878"
API = "1de96c534b2342d6976cebde16211e7c"
URL = "http://"+IP+"/api/v3/movie"
D = {"X-Api-Key":API}
headers = {"Accept":"*/*","X-Api-Key":API,"Content-Type":"application/json"}
options = {"id":0,"addOptions":{"monitor":"movieOnly","searchForMovie":True},"rootFolderPath":'/media/external/Videos/Movies'}

def search_movie(title):
    lookup = title.replace(' ', '%20')
    req1 = requests.get(URL+"/lookup?term="+lookup,headers=D)
    data = json.loads(req1.text)[0]
    return data

def get_dict(data):
    movie = {}
    movie['title'] = data['title']
    movie['qualityProfileId'] = 1
    movie['tmdbId'] = data['tmdbId']
    movie['titleSlug'] = data['titleSlug']
    movie['images'] = data['images']
    movie.update(options)
    return movie

def get_poster(movie):
    poster = movie['images'][0]['remoteUrl']
    return poster

def get_error(req):
    info = []
    try:
        info.append(json.loads(req.text)[0]['title']+" was just queued for download")
    except KeyError:
        info.append(json.loads(req.text)[0]['errorMessage'])
    return info
        
def queue_movie(title):
    movie = get_dict(search_movie(title))
    req2=requests.post(URL,headers=headers,json=movie)

    info = get_error(req2)
    info.append(get_poster(movie))
    
    return info

queue_movie(title)