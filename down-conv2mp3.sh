#!/bin/sh

# download from youtube and conver to mp3


# check youtube-dl, ffmpeg
type youtube-dl > /dev/null 2>&1 || { echo >&2  "please install youtube-dl."; exit 1;}
type ffmpeg > /dev/null 2>&1 || { echo >&2  "please install ffmpeg."; exit 1;}

# check argument
if [ $# -ne 1 ] ;then
  echo "usage: ./down.sh http://www.youtube.com/watch?v=xxxxxx"
  exit 1
fi

if [ -e $$ ] ;then
  echo "$$ is already exist."
  exit 1
fi

# make working dir
mkdir $$
cd $$

#download
youtube-dl $1 

if [ $? -ne 0 ]; then
  echo "download error..."
  exit 1
fi

#convert to mp3
FILE_NAME_ORIG=`ls`
FILE_NAME_MP3=`ls | sed -e s/mp4/mp3/`
#file type check
ffmpeg -i "$FILE_NAME_ORIG" -ab 128k "$FILE_NAME_MP3"

#copy to current dir
cp "$FILE_NAME_MP3" "../$FILE_NAME_MP3"

#remove working dir
rm -r -f ../$$

