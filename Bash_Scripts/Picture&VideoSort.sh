# find . -type f \( -iname "*.jpg" \) -exec exiftool -d '%Y-%m-%d_%H-%M-%S.jpg' '-filename<CreateDate' {} -o ~/Pictures/"TimeStampedPictures&Videos"/TimeStampedPictures \;
# This command will rename the file by its creation date and with -o copy it to another directory.
#
# find . -type f \( -iname "*.jpg" \) -exec exiftool -d ~/Pictures/"TimeStampedPictures&Videos"/TimeStampedPictures/'%Y-%m-%d_%H-%M-%S.jpg' '-filename<CreateDate' {} \;
# This command will rename the file by its creation date and move it to another directory.
#
# TODO: Add deduplication to script's scope. 

picture_sort(){
	find . -type f \( -iname "*$1" \) $2 \; -exec exiftool -d /media/flip/"8TB HDD/Other/Pictures&Videos/Family Pictures/%Y/%Y-%m-%d_%H-%M-%S%%-c$3" '-filename<CreateDate' {} \; -exec mv {} /media/flip/"8TB HDD/Other/Pictures&Videos/Family Pictures/Unkown Date" \;
}

video_sort(){
	find . -type f \( -iname "*$1" \) -exec exiftool -d /media/flip/"8TB HDD/Other/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c$1" '-filename<CreateDate' {} \; -exec mv {} /media/flip/"8TB HDD/Other/Pictures&Videos/Family Videos/Unkown Date" \;
}

while true; do
	picture_sort .jpg "-exec jpegoptim -t {}" .jpg >> pictureVideoSort.log
	picture_sort .jpeg "-exec jpegoptim -t {}" .jpg >> pictureVideoSort.log
	picture_sort .png "-exec optipng -o7 {}" .png >> pictureVideoSort.log

	video_sort .mp4 >> pictureVideoSort.log
	video_sort .mkv >> pictureVideoSort.log
	video_sort .mov >> pictureVideoSort.log
	video_sort .webm >> pictureVideoSort.log

	sleep 1m
done
