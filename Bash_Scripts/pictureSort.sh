#!/bin/bash
# This script will recursively search for images/videos losslessly compress, rename and organize them.
# TODO: Fix mv overwriting destination files.

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

mkdir -p $outpath/Pictures\&Videos/Family\ Pictures/Unknown\ Date
mkdir -p $outpath/Pictures\&Videos/Family\ Videos/Unknown\ Date
mkdir -p ../Trash/Duplicates/
mkdir -p ../Trash/Small/

while true; do
	# Recursively lists all files and puts them into "files" array.
	files=()
	mapfile -d $'\0' files < <(find . -print0)

	for ((i = 0; ${#files[@]} > i; i++)); do # Iterates through all files found.
		if file --mime-type -b "${files[i]}" | grep -q "image/" || file --mime-type -b "${files[i]}" | grep -q "video/" && [[ "${files[i]}" != *.syncthing.* ]]; then # Files that have "image/" or "video/" as a MIME type and not ".syncthing." in the name.
			if [ "$(stat -c %s "${files[i]}")" -le 20000 ]; then # Moves files less than 20KB to "../Trash/Small/".
				echo "Warning: File smaller than 20KB"
				mv "${files[i]}" ../Trash/Small/
			else
				checksum=`sha256sum "${files[i]}" | cut -d' ' -f1`
				if grep -q $checksum sha256sum.txt; then
					echo "Warning: File already exists"
					mv "${files[i]}" ../Trash/Duplicates/
				else
					echo $checksum >> sha256sum.txt
					case `file --mime-type -b "${files[i]}"` in
						"image/jpeg") 
							jpegoptim -t "${files[i]}"
							checksum=`sha256sum "${files[i]}" | cut -d' ' -f1`
							echo $checksum >> sha256sum.txt
							exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Pictures/%Y/%Y-%m-%d_%H-%M-%S%%-c.jpg" '-filename<CreateDate' "${files[i]}"
							mv "${files[i]}" "$outpath/Pictures&Videos/Family Pictures/Unknown Date"
							;;
						"image/png")
							optipng -o7 "${files[i]}"
							checksum=`sha256sum "${files[i]}" | cut -d' ' -f1`
							echo $checksum >> sha256sum.txt
							exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Pictures/%Y/%Y-%m-%d_%H-%M-%S%%-c.png" '-filename<CreateDate' "${files[i]}"
							mv "${files[i]}" "$outpath/Pictures&Videos/Family Pictures/Unknown Date"
							;;
						"image/heic")
							exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Pictures/%Y/%Y-%m-%d_%H-%M-%S%%-c.heic" '-filename<CreateDate' "${files[i]}"
							mv "${files[i]}" "$outpath/Pictures&Videos/Family Pictures/Unknown Date"
							;;
						"video/mp4")
							exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.mp4" '-filename<CreateDate' "${files[i]}"
							mv "${files[i]}" "$outpath/Pictures&Videos/Family Videos/Unknown Date"
							;;
						"video/x-ms-asf")
							exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.wmv" '-filename<CreateDate' "${files[i]}"
							mv "${files[i]}" "$outpath/Pictures&Videos/Family Videos/Unknown Date"
							;;
						"video/x-msvideo")
							exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.avi" '-filename<CreateDate' "${files[i]}"
							mv "${files[i]}" "$outpath/Pictures&Videos/Family Videos/Unknown Date"
							;;
						"video/quicktime")
							exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.mov" '-filename<CreateDate' "${files[i]}"
							mv "${files[i]}" "$outpath/Pictures&Videos/Family Videos/Unknown Date"
							;;
						"video/x-matroska")
							exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.mkv" '-filename<DateTimeOriginal' "${files[i]}"
							mv "${files[i]}" "$outpath/Pictures&Videos/Family Videos/Unknown Date"
							;;
						"video/3gpp") GP3=true
							exiftool -api largefilesupport=1 -d "$outpath/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.3gp" '-filename<CreateDate' "${files[i]}"
							mv "${files[i]}" "$outpath/Pictures&Videos/Family Videos/Unknown Date"
							;;
					esac
					
				fi
			fi
		fi
	done
	sleep 1m
done
} >> pictureVideoSort.log
