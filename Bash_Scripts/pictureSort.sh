#!/bin/bash
# This script will recursively search for images/videos losslessly compress, rename and organize them.

{
while getopts "i:o:" arg; do
  case $arg in
    i) inpath=$OPTARG
    ;;
    o) outpath=$OPTARG
    ;;
  esac
done

inpath="${inpath:-.}"
outpath="${outpath:-.}"

cd "$inpath"



while true; do
	# Recursively lists all files and puts them into "files" array.
	files=()
	mapfile -d $'\0' files < <(find . -print0)

	mkdir -p $outpath/Pictures\&Videos/Family\ Pictures/Unknown\ Date
	mkdir -p $outpath/Pictures\&Videos/Family\ Videos/Unknown\ Date
	mkdir -p ../Trash/Duplicates/
	mkdir -p ../Trash/Small/

	for ((i = 0; ${#files[@]} > i; i++)); do
		
		jpeg=false
		png=false
		heic=false
		mp4=false
		xmsasf=false
		xmsvideo=false
		quicktime=false
		xmatroska=false
		GP3=false
		
		# Checks for file type.
		if file -i "${files[i]}" | grep "image/jpeg" && [[ "${files[i]}" != *.syncthing.* ]]; then
			jpeg=true
		fi
		if file -i "${files[i]}" | grep "image/png"; then
			png=true
		fi
		if file -i "${files[i]}" | grep "image/heic"; then
			heic=true
		fi
		if file -i "${files[i]}" | grep "video/mp4"; then
			mp4=true
		fi
		if file -i "${files[i]}" | grep "video/x-ms-asf"; then
			xmsasf=true
		fi
		if file -i "${files[i]}" | grep "video/x-msvideo"; then
			xmsvideo=true
		fi
		if file -i "${files[i]}" | grep "video/quicktime"; then
			quicktime=true
		fi
		if file -i "${files[i]}" | grep "video/x-matroska"; then
			xmatroska=true
		fi
		if file -i "${files[i]}" | grep "video/3gpp"; then
			GP3=true
		fi
		
		# Pictures
		if [ "$jpeg" = true ]; then
			if [ "$(stat -c %s "${files[i]}")" -le 20000 ]; then
				mv "${files[i]}" ../Trash/Small/
			else
				jpegoptim -t "${files[i]}"
				checksum=`sha256sum "${files[i]}" | cut -d' ' -f1`
				if grep $checksum sha256sum.txt; then
					echo "Warning: File already exists"
					exiftool -api largefilesupport=1 -d "../Trash/Duplicates/%Y-%m-%d_%H-%M-%S%%-c.jpg" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" ../Trash/Duplicates/
				else
					echo $checksum >> sha256sum.txt
					exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Pictures/%Y/%Y-%m-%d_%H-%M-%S%%-c.jpg" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" "$outpath/Pictures&Videos/Family Pictures/Unknown Date"
				fi
			fi
		fi
		
		if [ "$png" = true ]; then
			if [ "$(stat -c %s "${files[i]}")" -le 20000 ]; then
				mv "${files[i]}" ../Trash/Small/
			else
				optipng -o7 "${files[i]}"
				checksum=`sha256sum "${files[i]}" | cut -d' ' -f1`
				if grep $checksum sha256sum.txt; then
					echo "Warning: File already exists"
					exiftool -api largefilesupport=1 -d "../Trash/Duplicates/%Y-%m-%d_%H-%M-%S%%-c.png" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" ../Trash/Duplicates/
				else
					echo $checksum >> sha256sum.txt
					exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Pictures/%Y/%Y-%m-%d_%H-%M-%S%%-c.png" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" "$outpath/Pictures&Videos/Family Pictures/Unknown Date"
				fi
			fi
		fi
		
		if [ "$heic" = true ]; then
			if [ "$(stat -c %s "${files[i]}")" -le 20000 ]; then
				mv "${files[i]}" ../Trash/Small/
			else
				checksum=`sha256sum "${files[i]}" | cut -d' ' -f1`
				if grep $checksum sha256sum.txt; then
					echo "Warning: File already exists"
					exiftool -api largefilesupport=1 -d "../Trash/Duplicates/%Y-%m-%d_%H-%M-%S%%-c.heic" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" ../Trash/Duplicates/
				else
					echo $checksum >> sha256sum.txt
					exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Pictures/%Y/%Y-%m-%d_%H-%M-%S%%-c.heic" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" "$outpath/Pictures&Videos/Family Pictures/Unknown Date"
				fi
			fi
		fi
		
		# Videos
		if [ "$mp4" = true ]; then
			if [ "$(stat -c %s "${files[i]}")" -le 20000 ]; then
				mv "${files[i]}" ../Trash/Small/
			else
				checksum=`sha256sum "${files[i]}" | cut -d' ' -f1`
				if grep $checksum sha256sum.txt; then
					echo "Warning: File already exists"
					exiftool -api largefilesupport=1 -d "../Trash/Duplicates/%Y-%m-%d_%H-%M-%S%%-c.mp4" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" ../Trash/Duplicates/
				else
					echo $checksum >> sha256sum.txt
					exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.mp4" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" "$outpath/Pictures&Videos/Family Videos/Unknown Date"
				fi
			fi
		fi
		
		if [ "$xmsasf" = true ]; then
			if [ "$(stat -c %s "${files[i]}")" -le 20000 ]; then
				mv "${files[i]}" ../Trash/Small/
			else
				checksum=`sha256sum "${files[i]}" | cut -d' ' -f1`
				if grep $checksum sha256sum.txt; then
					echo "Warning: File already exists"
					exiftool -api largefilesupport=1 -d "../Trash/Duplicates/%Y-%m-%d_%H-%M-%S%%-c.wmv" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" ../Trash/Duplicates/
				else
					echo $checksum >> sha256sum.txt
					exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.wmv" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" "$outpath/Pictures&Videos/Family Videos/Unknown Date"
				fi
			fi
		fi
		
		if [ "$xmsvideo" = true ]; then
			if [ "$(stat -c %s "${files[i]}")" -le 20000 ]; then
				mv "${files[i]}" ../Trash/Small/
			else
				checksum=`sha256sum "${files[i]}" | cut -d' ' -f1`
				if grep $checksum sha256sum.txt; then
					echo "Warning: File already exists"
					exiftool -api largefilesupport=1 -d "../Trash/Duplicates/%Y-%m-%d_%H-%M-%S%%-c.avi" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" ../Trash/Duplicates/
				else
					echo $checksum >> sha256sum.txt
					exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.avi" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" "$outpath/Pictures&Videos/Family Videos/Unknown Date"
				fi
			fi
		fi
		
		if [ "$quicktime" = true ]; then
			if [ "$(stat -c %s "${files[i]}")" -le 20000 ]; then
				mv "${files[i]}" ../Trash/Small/
			else
				checksum=`sha256sum "${files[i]}" | cut -d' ' -f1`
				if grep $checksum sha256sum.txt; then
					echo "Warning: File already exists"
					exiftool -api largefilesupport=1 -d "../Trash/Duplicates/%Y-%m-%d_%H-%M-%S%%-c.mov" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" ../Trash/Duplicates/
				else
					echo $checksum >> sha256sum.txt
					exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.mov" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" "$outpath/Pictures&Videos/Family Videos/Unknown Date"
				fi
			fi
		fi
		
		if [ "$xmatroska" = true ]; then
			if [ "$(stat -c %s "${files[i]}")" -le 20000 ]; then
				mv "${files[i]}" ../Trash/Small/
			else
				checksum=`sha256sum "${files[i]}" | cut -d' ' -f1`
				if grep $checksum sha256sum.txt; then
					echo "Warning: File already exists"
					exiftool -api largefilesupport=1 -d "../Trash/Duplicates/%Y-%m-%d_%H-%M-%S%%-c.mkv" '-filename<DateTimeOriginal' "${files[i]}"
					mv "${files[i]}" ../Trash/Duplicates/
				else
					echo $checksum >> sha256sum.txt
					exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.mkv" '-filename<DateTimeOriginal' "${files[i]}"
					mv "${files[i]}" "$outpath/Pictures&Videos/Family Videos/Unknown Date"
				fi
			fi
		fi
		
		if [ "$GP3" = true ]; then
			if [ "$(stat -c %s "${files[i]}")" -le 20000 ]; then
				mv "${files[i]}" ../Trash/Small/
			else
				checksum=`sha256sum "${files[i]}" | cut -d' ' -f1`
				if grep $checksum sha256sum.txt; then
					echo "Warning: File already exists"
					exiftool -api largefilesupport=1 -d "../Trash/Duplicates/%Y-%m-%d_%H-%M-%S%%-c.3gp" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" ../Trash/Duplicates/
				else
					echo $checksum >> sha256sum.txt
					exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.3gp" '-filename<CreateDate' "${files[i]}"
					mv "${files[i]}" "$outpath/Pictures&Videos/Family Videos/Unknown Date"
				fi
			fi
		fi
	done
	sleep 10m
done
} >> pictureVideoSort.log
