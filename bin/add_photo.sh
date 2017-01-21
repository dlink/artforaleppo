#!/bin/bash

MEDIA_DIR='/data/artforaleppo-media/postcards'

if [[ "$1" == "" ]]; then
    echo 'no image filename given'
    exit 1
fi

src_filepath=$1
filename=${src_filepath##*/}
dst_filepath1=${MEDIA_DIR}/$filename
dst_filepath2=${MEDIA_DIR}/200px/$filename

cp -v $src_filepath $dst_filepath1
echo
echo 'original:'
gm identify $dst_filepath1

echo
echo 'new:'
gm mogrify -resize 900 $dst_filepath1
gm identify $dst_filepath1

cp -v $dst_filepath1 $dst_filepath2
echo
echo 'thumbnail:'
gm mogrify -resize 200 $dst_filepath2
gm identify $dst_filepath2



