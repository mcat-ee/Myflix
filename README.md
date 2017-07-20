# Myflix
*A Netflix clone!*

Myflix tries to be a somewhat simple and lightweight "DIY Netflix", similar to Plex or Emby, for your DIY NAS, especially aimed at the Raspberry Pi/Odroid/etc ecosystem. It's not meant or designed to be fancy, but the bare minimum to be pretty, fast and usable

**Shitty temporary tutorial:**

You will need jq, imagemagick, ffmpeg and a ton of coffee to understand whatthef#ck I did.
Download all the files, look around in buildDBs.cgi and config.cfg, set the path of your media files folders and run buildDBs... 
Pray to a deity of your choice!

Features :
* uses BASH for everything... at least so far!
* Movie and TV show databases are saved in an user friendly database
* Lightweight and highly customisable, just open a script and edit it! 
* Once you have built the database and the webpage, it's done. No streaming server or anything of the like...
* Since there is no real service, you could build the database and webpages on another machine, moving the webpage to the actual web server afterwards. ( keep in mind that the webserver must have access to the files etc...)
* Automatically converts srt's into vtt and makes them available in the video player
* Press f to fullscreen player, left to rewind 15 secs, right to skip forward 15 secs, space to play/pause

Issues :
* "Slow" file scanning, scanning 1200+ TV shows files while getting all kinds of metadata (so show id, posters for the show and the name of every episode...) took almost 20 minutes on an old odroid-c1... Skipping some metadata speeds up the process a lot ( episode name is the biggest culprit, as it adds a 2-3 seconds to every episode in the database). If I skip it, the time comes down to around 2-3 minutes. Note that this doesn't happen with movies as there is a lot less metadata to be fetched and my nas can perform this task in 30 seconds on so with 40+ movies.
* "Slow" html generation, the 1200+ files end up creating a html page with 25700 lines of code... Which generates in around 10 minutes...  
* html5 video player keeps buffering in the background if you play/pause a video. At the moment I have yet to implement a way to stop buffering
* not really an issue imho, but it's html5 reliant, so all video files HAVE to be h264 mp4's, no transcoding is going to happen. If you want transcoding, use something fancier like Emby

TO-DO:
* Separate metadata download and database creation... (MAYBE?)
* Splitting the TV database into "per show/season" files, would probably speed up things a lot (MAYBE? I kinda like it this way)
* A decent tutorial

More in the coming days...
