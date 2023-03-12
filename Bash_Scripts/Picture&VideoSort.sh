# This script will recursively search for images/videos compress, rename and organize them.

picture_sort(){
	all_files=$(find . -type f -iname "*$1")
	lines=`find . -type f -iname "*$1" | wc -l`
	
	if [ $lines != 0 ]; then # Checks if $all_files is empty.
		for ((i = 1; $lines >= i; i++)); do
			file=`echo $all_files | cut -d' ' -f$i`
			checksum=`sha256sum "$file" | cut -d' ' -f1` # Compares checksum to a list and adds it to the list if a checksum is not found.
			if grep $checksum /media/flip/8TB\ HDD/Other/Pictures\&Videos/sha256sum.txt; then
				echo "File already exists."
				exiftool -d ../Trash/%Y-%m-%d_%H-%M-%S%%-c$1 '-filename<CreateDate' "$file"
				mv --backup $file ../Trash/
			else
				if [ $2 == ".png" ]; then
					optipng -o7 "$file"
					checksum=`sha256sum "$file" | cut -d' ' -f1`
				fi
				if [ $2 == ".jpg" ]; then
					jpegoptim -t "$file"
					checksum=`sha256sum "$file" | cut -d' ' -f1`
				fi
				echo $checksum >> /media/flip/8TB\ HDD/Other/Pictures\&Videos/sha256sum.txt
				exiftool -d /media/flip/"8TB HDD/Other/Pictures&Videos/Family Pictures/%Y/%Y-%m-%d_%H-%M-%S%%-c$2" '-filename<CreateDate' "$file"
				mv --backup "$file" /media/flip/"8TB HDD/Other/Pictures&Videos/Family Pictures/Unkown Date/"
			fi
		done
	fi
}

video_sort(){
	all_files=$(find . -type f -iname "*$1")
	lines=`find . -type f -iname "*$1" | wc -l`
	
	if [ $lines != 0 ]; then # Checks if $all_files is empty.
		for ((i = 1; $lines >= i; i++)); do
			file=`echo $all_files | cut -d' ' -f$i`
			checksum=`sha256sum "$file" | cut -d' ' -f1` # Compares checksum to a list and adds it to the list if a checksum is not found.
			if grep $checksum /media/flip/8TB\ HDD/Other/Pictures\&Videos/sha256sum.txt; then
				echo "File already exists."
				exiftool -d ../Trash/%Y-%m-%d_%H-%M-%S%%-c$1 '-filename<CreateDate' "$file"
				mv --backup $file ../Trash/
			else
				echo $checksum >> /media/flip/8TB\ HDD/Other/Pictures\&Videos/sha256sum.txt
				exiftool -d /media/flip/"8TB HDD/Other/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c$1" '-filename<CreateDate' "$file"
				mv --backup "$file" /media/flip/"8TB HDD/Other/Pictures&Videos/Family Videos/Unkown Date/"
			fi
		done
	fi
}

while true; do
	picture_sort .jpg .jpg >> pictureVideoSort.log
	picture_sort .png .png >> pictureVideoSort.log
	picture_sort .jpeg .jpg >> pictureVideoSort.log
	
	video_sort .mp4 >> pictureVideoSort.log
	video_sort .mkv >> pictureVideoSort.log
	video_sort .mov >> pictureVideoSort.log
	video_sort .webm >> pictureVideoSort.log
	video_sort .wmv >> pictureVideoSort.log
	sleep 1m
done
