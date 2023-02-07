# find . -type f \( -iname "*.jpg" \) -exec exiftool -d '%Y-%m-%d_%H-%M-%S.jpg' '-filename<CreateDate' {} -o ~/Pictures/"TimeStampedPictures&Videos"/TimeStampedPictures \;
# This command will rename the file by its creation date and with -o copy it to another directory.
#
# find . -type f \( -iname "*.jpg" \) -exec exiftool -d ~/Pictures/"TimeStampedPictures&Videos"/TimeStampedPictures/'%Y-%m-%d_%H-%M-%S.jpg' '-filename<CreateDate' {} \;
# This command will rename the file by its creation date and move it to another directory.

while true; do
find . -type f \( -iname "*.jpg" \) -exec jpegoptim -t {} \; -exec exiftool -d /media/flip/"8TB HDD/Other/Pictures&Videos/Family Pictures/%Y/%Y-%m-%d_%H-%M-%S%%-c.jpg" '-filename<CreateDate' {} \; -exec mv {} /media/flip/"8TB HDD/Other/Pictures&Videos/Family Pictures/Unkown Date" \; >> pictureVideoSort.log
find . -type f \( -iname "*.jpeg" \) -exec jpegoptim -t {} \; -exec exiftool -d /media/flip/"8TB HDD/Other/Pictures&Videos/Family Pictures/%Y/%Y-%m-%d_%H-%M-%S%%-c.jpg" '-filename<CreateDate' {} \; -exec mv {} /media/flip/"8TB HDD/Other/Pictures&Videos/Family Pictures/Unkown Date" \; >> pictureVideoSort.log
find . -type f \( -iname "*.png" \) -exec optipng -o7 {} \; -exec exiftool -d /media/flip/"8TB HDD/Other/Pictures&Videos/Family Pictures/%Y/%Y-%m-%d_%H-%M-%S%%-c.png" '-filename<CreateDate' {} \; -exec mv {} /media/flip/"8TB HDD/Other/Pictures&Videos/Family Pictures/Unkown Date" \; >> pictureVideoSort.log

find . -type f \( -iname "*.mp4" \) -exec exiftool -d /media/flip/"8TB HDD/Other/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.mp4" '-filename<CreateDate' {} \; -exec mv {} /media/flip/"8TB HDD/Other/Pictures&Videos/Family Videos/Unkown Date" \; >> pictureVideoSort.log
find . -type f \( -iname "*.mkv" \) -exec exiftool -d /media/flip/"8TB HDD/Other/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.mkv" '-filename<CreateDate' {} \; -exec mv {} /media/flip/"8TB HDD/Other/Pictures&Videos/Family Videos/Unkown Date" \; >> pictureVideoSort.log
find . -type f \( -iname "*.mov" \) -exec exiftool -d /media/flip/"8TB HDD/Other/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.mov" '-filename<CreateDate' {} \; -exec mv {} /media/flip/"8TB HDD/Other/Pictures&Videos/Family Videos/Unkown Date" \; >> pictureVideoSort.log
find . -type f \( -iname "*.webm" \) -exec exiftool -d /media/flip/"8TB HDD/Other/Pictures&Videos/Family Videos/%Y/%Y-%m-%d_%H-%M-%S%%-c.webm" '-filename<CreateDate' {} \; -exec mv {} /media/flip/"8TB HDD/Other/Pictures&Videos/Family Videos/Unkown Date" \; >> pictureVideoSort.log

sleep 1m
done
