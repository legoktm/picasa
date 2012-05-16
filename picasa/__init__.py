#!/usr/bin/python

import sys
import re
import os
import urllib
import urllib2
import gdata.photos
import gdata.photos.service






def main():
  pws = gdata.photos.service.PhotosService()
  
  username = sys.argv[1]
  resume = ''
  username = False
  password = False
  force = False
  for arg in sys.argv:
    if arg.startswith('--resume='):
      resume = arg.split('--resume=')[1]
    if arg.startswith('--username='):
      username = arg.split('--username=')[1]
    if arg.startswith('--password='):
      password = arg.split('--password=')[1]
    if arg == '--force':
      force = True
    
  if username and password:
    pws.ClientLogin(username, password)
    print 'Logged in as %s.' %(username)
  else:
    print 'Logged in as anonymous.'
  print 'Grabbing %s\'s photos' %username
  albums = pws.GetUserFeed(user=username).entry
  flag = not bool(resume)
  for album in albums:
    if album.name.text.lower() == resume.lower():
      flag = True
    if flag:
      process_album(album, force)
    else:
      print 'Skipping %s' %(album.name.text)
    
def process_album(album, force):
  album_name = album.name.text
  create_dir(album_name)
  print 'Starting %s' %(album_name)
  photos = pws.GetFeed(album.GetPhotosUri()).entry
  try:
    photo = photos[0]
  except IndexError:
    print 'No photos in %s' %(album_name)
    return
  gallery_link = str(photo.GetHtmlLink().href)
  text = grab_url(gallery_link)
  found = re.findall('"width":"(.*?)","height":"(.*?)","size":"(.*?)","commentingEnabled":"(.*?)","allowNameTags":"(.*?)","media":\{"content":\[\{"url":"https:\/\/(.*?)",', text)
  #print found
  #url_list = []
  for object in found:
    split = object[5].split('/')
    split.append(split[5]) #extra item
    split[5] = 's'+object[0]
    url = 'https://' + '/'.join(split)
    filename = split[6]
    if os.path.isfile(filename) and (not force):
      continue
    #print url
    try:
      download_image(url, album_name.lower(), filename)
    except:
      print 'Skipping: Error on %s' %(url)
    print 'Successfully grabbed %s' %(split[6])
    #url_list.append(url)
  print 'Finished %s' %(album_name)

def download_image(url, album, filename):
  img = grab_url(url)
  file = open(album+'/'+filename, 'w')
  file.write(img)
  file.close()

def grab_url(link):
  obj = urllib.urlopen(link)
  text = obj.read()
  obj.close()
  return text

def create_dir(name):
  try:
    os.mkdir(name.lower())
  except OSError:
    pass  


if __name__ == "__main__":
  main()
