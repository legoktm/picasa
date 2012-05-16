#!/usr/bin/python

import sys
import re
import os
import urllib
import urllib2
import gdata.photos
import gdata.photos.service


pws = gdata.photos.service.PhotosService()



def main():
  username = sys.argv[1]
  resume = ''
  if len(sys.argv) == 3:
    if sys.argv[2].startswith('--resume='):
      resume = sys.argv[2].split('--resume=')[1]

  print 'Grabbing %s\'s photos' %username
  albums = pws.GetUserFeed(user=username).entry
  flag = not bool(resume)
  for album in albums:
    if album.name.text.lower() == resume.lower():
      flag = True
    if flag:
      process_album(album)
    else:
      print 'Skipping %s' %(album.name.text)
    
def process_album(album):
  create_dir(album.name.text)
  print 'Starting %s' %(album.name.text)
  photos = pws.GetFeed(album.GetPhotosUri()).entry
  try:
    photo = photos[0]
  except IndexError:
    print 'No photos in %s' %(album.name.text)
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
    #print url
    try:
      download_image(url, album.name.text.lower(), split[6])
    except:
      print 'Skipping: Error on %s' %(url)
    print 'Successfully grabbed %s' %(split[6])
    #url_list.append(url)
  print 'Finished %s' %(album.name.text)

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
