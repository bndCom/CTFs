# NotFS - Forensics

## Description

Is this a FileSystem? Identify the file and make the necessary adjustments to solve the challenge. Note: The challenge file size is 16GB after extraction.

## Quick Overview

The disk image is corrupted, so we can't mount it or explore it with disk analysis tools like Autopsy or FTK Imager.

## Solution

- There are various tools for repairing corrupted filesystems; one well-known tool is `TestDisk`.
- Open the image with TestDisk, list the files within the first listed partition, and you will find 7 images. One of them is a corrupted PNG file with missing magic bytes.
- Fix the corrupted PNG file, and you will get the flag.

![flag](flag.png)
