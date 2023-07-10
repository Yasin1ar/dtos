# Bash Script for Renaming Files with spaces to dots

This *simple* bash script exactly does the opposite of  [dtos](https://github.com/Yasin1ar/dtos)

## How to Use

1. Download the script to your local machine.
2. Make the script executable using the command `chmod +x stod`.
3. Navigate to the directory containing the files you want to rename.
4. Run the script using the command `./stod`.

The script gets files in the current directory as command-line arguments, and rename each file according to the following rules:

1. If the file does not have an extension, it will be skipped.
2. The spaces in the filename will be replaced with dots.
3. The file extension will be preserved.

For example, a file named `my video file.mkv` will be renamed to `my.video.file.mkv` *with this command :*

**./stod  'my video file.mkv'**
