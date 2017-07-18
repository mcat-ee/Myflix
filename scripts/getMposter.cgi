#! /bin/bash

cd "$(dirname "$0")"
if [ "$#" -ne 1 ]; then
	echo "$0": usage: getMposter.cgi ID
	exit 1
fi

dMoImg=false
dMoFolder=../MoImg/
imgResizeMo="500x"
tinyPNGapi=""
TMDBapi=""
compressImgMo=false

. config.cfg

id=${1};
if [[ ! -z "$TMDBapi" ]]; then
	myUrl="https://api.themoviedb.org/3/movie/tt"${id}"/images?include_image_language=en&api_key="$TMDBapi
	output=$(curl -s --request GET --url $myUrl --data '{}' | jq -r '.posters | map(select((.width | contains(1000)) and (.height | contains(1500))) | .file_path) | .[]' | head -n1)

	if [[ $output == *".jpg"* ]]; then
		output="https://image.tmdb.org/t/p/original"$output;
	else
		output=$(curl -s --request GET --url $myUrl --data '{}' | jq -r '.posters[0].file_path' )
		if [[ $output == *".jpg"* ]]; then
			output="https://image.tmdb.org/t/p/original"$output;
		else
			echo "null";
			exit;
		fi
	fi

	if $dMoImg; then
		if [ ! -d "$dMoFolder" ]; then
			mkdir $dMoFolder
		fi
		wget -q -P $dMoFolder $output;
		output=$(basename $output)
		if [ ! -z "$imgResizeMo" ]; then
			convert -resize $imgResizeMo $dMoFolder$output $dMoFolder$output
		fi
		if $compressImgMo; then
			convert -strip -interlace Plane -gaussian-blur 0.05 -quality 90% $dMoFolder$output $dMoFolder$output
		fi
		if [[ ! -z "$tinyPNGapi" ]]; then
			imgUrl=$(curl -s --user api:$tinyPNGapi  --data-binary @$dMoFolder$output https://api.tinify.com/shrink | jq -r '.output.url')
			curl -s --user api:$tinyPNGapi --output $dMoFolder$output $imgUrl
		fi
		chmod 755 -R $dMoFolder
		tempFolder=$(basename $dMoFolder)
		echo $tempFolder"/"$output;
	else
		echo $output
	fi
else
	echo "null"
fi

