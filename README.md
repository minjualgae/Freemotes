# Leek's Freemotes V.1.5
 "Free" Discord Nitro with extra steps
 ~~Basically a gif sender~~
#### All gif emotes are edited to 49px x 49px to mimic real emotes at standard Discord size


How it works...

1. Reads and saves all csv data into a dictionary
**Make sure there are no spaces in csv and follow formatting (using commas) or else it won't work properly**

2. Detects keypresses and if in a specific pattern, types out a gif link.
	Ex:
	> input: ":pepelaugh:" + any key press after
	> output: a link associated with the key :pepelaugh:

## Available Functions

On Tab Press:
- Autocompletes emote based on closest search
 	Ex:
 	> input: ":pepel" + tab key press
 	> output: ":pepelaugh:"

## Download Link

I used pyinstaller to convert the script into a .exe if anyone wants to try it directly

Make sure both freemotes.exe and freemotes.csv are in the same directory or file for it to run properly
You can make your own freemotes.csv, just follow the format in the premade freemotes.csv

### Freemotes.exe
[Download freemotes.exe](https://github.com/minjualgae/Freemotes/raw/main/Freemotes/freemote.exe)

### Freemotes.csv
[Download premade freemotes.csv](https://drive.google.com/file/d/1VkETFiftPUtEsFZ20wx3ke3KJXkUc00H/view) <-- Made For Duan