import argparse
import os
import cv2
import pafy
from os import system, name
from time import sleep

def parseArgs():
    parser = argparse.ArgumentParser(description="Splits a given video into its individual frames")
    parser.add_argument("-v", "--video", help="Path to a video file", required=True)
    parser.add_argument("-d", "--directory", help="Name of the directory to store the files in.", required=True)
    return parser.parse_args()

def createDirectory(directory):
    try:
        os.mkdir(directory)
    except FileExistsError:
        print("[INFO] Directory already exists!")

def saveFrame(frame, directory, index):
    try:
        cv2.imwrite(directory+"/"+directory+str(index)+".jpg", frame)
        return True
    except cv2.error:
        return False

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _ = system("clear")

def splitVideo(video, directory):
    try:
        cap = cv2.VideoCapture(video)
    except FileExistsError:
        print("[INFO] File does not exist!")
        exit(0)
    
    index = 0
    while cap.isOpened():
        ret, frame = cap.read()
        val = saveFrame(frame, directory, index)
        if val == False:
            break
        print("[INFO] Image "+str(index)+" has been processed!")
        clear()
        index += 1

        if cv2.waitKey(1) &0xFF== ord("q"):
            break
        
        cv2.imshow(directory, frame)
    
    print("[INFO] Video successfully converted!")
    print("[INFO] "+str(index)+" Total Frames Made.")
    cap.release()


if __name__ == "__main__":
    args = parseArgs()
    createDirectory(args.directory)
    splitVideo(args.video, args.directory)
