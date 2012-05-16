picasa-downloader
============================

A script that automatically downloads all images from a picasa web album.

###Installation
For a stable install run
```
pip install picasa-downloader
```
If you wish to run the latest copy out of git
```
python setup.py install
```
###Operation
Run it by using:
```
picasa user_id [--resume=album_name] [--force] [--username=google_username] [--password=google_password]
```

 - user_id can either be the user's numeric Google ID or their Gmail address (with '@gmail.com' at the end)

 - The optional resume flag allows you to skip all albums until you reach the album specified.

 - Force will overwrite existing image files with re-downloaded copies.

 - Username and password allows the user to login and download private albums--if both are not provided, the script will simply ignore logging in
