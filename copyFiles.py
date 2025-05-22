import os
import shutil

# List of files to copy (relative to current working directory)
files_to_copy = [
    "Resources/templates/Speaker setups/CUBE/Cube_default_speaker_setup.xml",
    "Resources/templates/Speaker setups/DOME/Dome_default_speaker_setup.xml",
    "Resources/templates/Speaker setups/CUBE/Cube0(0)Subs0.xml",
    "Resources/templates/Speaker setups/DOME/Dome0(0)Subs0.xml",
    "Resources/templates/Speaker setups/CUBE/Cube12(3X4)Subs2 Centres.xml",
    "Resources/templates/Speaker setups/DOME/Dome13(9-4)Subs2 Bremen.xml",
    "Resources/templates/Speaker setups/DOME/Dome8(4-4)Subs1 ZiMMT Small Studio.xml",
    "Resources/templates/Speaker setups/CUBE/Cube93(32-32-16-8-4-1)Subs5 Satosphere.xml",
    "Resources/templates/Speaker setups/DOME/Dome93(32-32-16-8-4-1)Subs5 Satosphere.xml",
    "Resources/templates/Speaker setups/CUBE/Cube26(8-8-6-2-2)Subs3 Lisbonne.xml",
    "Resources/templates/Speaker setups/DOME/Dome61(29-11-14-7)Subs0 Brahms.xml",
    "Resources/templates/Speaker setups/CUBE/Cube24(8-8-8)Subs2 Studio PANaroma.xml",
    "Resources/templates/Speaker setups/DOME/Dome20(8-6-4-2)Sub4 Lakefield Icosa.xml",
    "Resources/templates/Speaker setups/DOME/Dome32(4X8)Subs4 SubMix.xml",
]

# Destination directory (update this as needed)
destination_dir = "C:/Users/barth/Documents/git/perso/pythonScripts/temp/"

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Copy files
for file_path in files_to_copy:
    full_source_path = os.path.abspath(file_path)
    if os.path.exists(full_source_path):
        shutil.copy(full_source_path, destination_dir)
        print(f"Copied: {file_path}")
    else:
        print(f"File not found: {file_path}")
