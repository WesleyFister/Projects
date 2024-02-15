#!/usr/bin/env python3
import os
import subprocess
import platform
from moviepy.editor import *
from PyQt5.QtWidgets import QApplication, QFileDialog

targetFileSize = 200000000
audioBitrate = 60000

filePaths = ""
filePaths = os.getenv("NAUTILUS_SCRIPT_SELECTED_FILE_PATHS")


if platform.system() == "Windows":
	app = QApplication([])

	file_dialog = QFileDialog()
	file_dialog.setFileMode(QFileDialog.ExistingFiles)
	file_dialog.setViewMode(QFileDialog.Detail)
	file_dialog.exec_()
	filePathList = file_dialog.selectedFiles()
	app.quit()
	
	for filePath in filePathList:
		if filePath:
			dirName, file = os.path.split(filePath)
			fileName, fileExtension = os.path.splitext(file)
			dirName = dirName + '/'
			output_file = dirName + fileName + "Discord" + ".mp4"
			
			videoLength = VideoFileClip(filePath).duration
			bitrate = (targetFileSize/videoLength)-audioBitrate
			bitrate = int(bitrate)
			
			clip = VideoFileClip(filePath)
			resized_clip = clip.resize(width=960, height=540)
			
			ffmpeg_params = ["-pass", "1", "-r", "30", "-c:v", "libx264", "-c:a", "aac", "-b:v", str(bitrate), "-b:a", str(audioBitrate), "-preset", "veryslow", "-f", "mp4", "NUL"]
			resized_clip.write_videofile(output_file, ffmpeg_params=ffmpeg_params, verbose=False)
			
			ffmpeg_params = ["-pass", "2", "-r", "30", "-c:v", "libx264", "-c:a", "aac", "-b:v", str(bitrate), "-b:a", str(audioBitrate), "-preset", "veryslow", "-f", "mp4"]
			resized_clip.write_videofile(output_file, ffmpeg_params=ffmpeg_params, verbose=False)
			
			os.remove("ffmpeg2pass-0.log")
			os.remove("ffmpeg2pass-0.log.mbtree")
	
elif platform.system() == "Linux" and filePaths == "" or filePaths == None:
	app = QApplication([])

	file_dialog = QFileDialog()
	file_dialog.setFileMode(QFileDialog.ExistingFiles)
	file_dialog.setViewMode(QFileDialog.Detail)
	file_dialog.exec_()
	filePathList = file_dialog.selectedFiles()
	app.quit()
	
	for filePath in filePathList:
		if filePath:
			dirName, file = os.path.split(filePath)
			fileName, fileExtension = os.path.splitext(file)
			dirName = dirName + '/'
			output_file = dirName + fileName + "Discord" + ".mp4"
			
			videoLength = VideoFileClip(filePath).duration
			bitrate = (targetFileSize/videoLength)-audioBitrate
			bitrate = int(bitrate)
			
			clip = VideoFileClip(filePath)
			resized_clip = clip.resize(width=960, height=540)
			
			ffmpeg_params = ["-pass", "1", "-r", "30", "-c:v", "libx264", "-c:a", "aac", "-b:v", str(bitrate), "-b:a", str(audioBitrate), "-preset", "veryslow", "-f", "mp4", "/dev/null"]
			resized_clip.write_videofile(output_file, ffmpeg_params=ffmpeg_params, verbose=False)
			
			ffmpeg_params = ["-pass", "2", "-r", "30", "-c:v", "libx264", "-c:a", "aac", "-b:v", str(bitrate), "-b:a", str(audioBitrate), "-preset", "veryslow", "-f", "mp4"]
			resized_clip.write_videofile(output_file, ffmpeg_params=ffmpeg_params, verbose=False)
			
			os.remove("ffmpeg2pass-0.log")
			os.remove("ffmpeg2pass-0.log.mbtree")
	
else:
	filePathList = filePaths.split("\n")
	for filePath in filePathList:
		if filePath:
			dirName, file = os.path.split(filePath)
			fileName, fileExtension = os.path.splitext(file)
			dirName = dirName + '/'
			output_file = dirName + fileName + "Discord" + ".mp4"
			
			videoLength = VideoFileClip(filePath).duration
			bitrate = (targetFileSize/videoLength)-audioBitrate
			bitrate = int(bitrate)
			
			clip = VideoFileClip(filePath)
			resized_clip = clip.resize(width=960, height=540)
			
			ffmpeg_params = ["-pass", "1", "-r", "30", "-c:v", "libx264", "-c:a", "aac", "-b:v", str(bitrate), "-b:a", str(audioBitrate), "-preset", "veryslow", "-f", "mp4", "/dev/null"]
			resized_clip.write_videofile(output_file, ffmpeg_params=ffmpeg_params, verbose=False)
			
			ffmpeg_params = ["-pass", "2", "-r", "30", "-c:v", "libx264", "-c:a", "aac", "-b:v", str(bitrate), "-b:a", str(audioBitrate), "-preset", "veryslow", "-f", "mp4"]
			resized_clip.write_videofile(output_file, ffmpeg_params=ffmpeg_params, verbose=False)
			
			os.remove("ffmpeg2pass-0.log")
			os.remove("ffmpeg2pass-0.log.mbtree")
