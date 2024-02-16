#!/usr/bin/env python3
import os
import subprocess
import platform
import mimetypes
from moviepy.editor import *
from PyQt5.QtWidgets import QApplication, QFileDialog
#TODO Keep original video rotation.

targetFileSize = 200000000
audioBitrate = 60000

filePaths = os.getenv("NAUTILUS_SCRIPT_SELECTED_FILE_PATHS")

if platform.system() == "Windows":
	trash = "NUL"
	
elif platform.system() == "Linux":
	trash = "/dev/null"

if filePaths == None:
	# File selection dialogue if not invoked through Nautilus file manager.
	app = QApplication([])
	file_dialog = QFileDialog()
	file_dialog.setFileMode(QFileDialog.ExistingFiles)
	file_dialog.setViewMode(QFileDialog.Detail)
	file_dialog.exec_()
	filePathList = file_dialog.selectedFiles()
	app.quit()
	
else:
	# If invoked through Nautilus file manager.
	filePathList = filePaths.split("\n")

for filePath in filePathList:
	mime = mimetypes.guess_type(filePath)
	fileType = mime[0].split("/")
	
	fileSize = os.path.getsize(filePath)
	
	if fileSize > 25000000 and fileType[0] == "video":
		dirName, file = os.path.split(filePath)
		fileName, fileExtension = os.path.splitext(file)
		dirName = dirName + '/'
		output_file = dirName + fileName + "Discord" + ".mp4"
		
		# Calculates bitrate based on target file size.
		videoLength = VideoFileClip(filePath).duration
		bitrate = (targetFileSize/videoLength)-audioBitrate
		bitrate = int(bitrate)
		
		# Will only set FPS to 30 if video is greater than 50MB.
		videoFPS = VideoFileClip(filePath).fps
		if videoFPS > 30 and fileSize > 50000000:
			videoFPS = 30
		
		# Will only set resolution to 960 and auto calculate width or height if video is greater than 100MB.
		clip = VideoFileClip(filePath)
		width = clip.size[0]
		height = clip.size[1]
		resized_clip = clip.resize(1)
		if (width > 960 or height > 960) and fileSize > 100000000:
			print("yes")
			if width > height:
				resized_clip = clip.resize(width=960)
				
			else:
				resized_clip = clip.resize(height=960)
		
		# Write to file using 2 pass encoding and other FFmpeg options.
		ffmpeg_params = ["-pass", "1", "-r", str(videoFPS), "-strict", "-2", "-c:v", "libx264", "-c:a", "libopus", "-b:v", str(bitrate), "-b:a", str(audioBitrate), "-preset", "veryslow", "-f", "mp4", trash]
		resized_clip.write_videofile(output_file, ffmpeg_params=ffmpeg_params, verbose=False)
		ffmpeg_params = ["-pass", "2", "-r", str(videoFPS), "-strict", "-2", "-c:v", "libx264", "-c:a", "libopus", "-b:v", str(bitrate), "-b:a", str(audioBitrate), "-preset", "veryslow", "-f", "mp4"]
		resized_clip.write_videofile(output_file, ffmpeg_params=ffmpeg_params, verbose=False)
		
		# Remove files created by FFmpeg in the first pass.
		os.remove("ffmpeg2pass-0.log")
		os.remove("ffmpeg2pass-0.log.mbtree")
