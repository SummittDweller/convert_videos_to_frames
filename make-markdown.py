import argparse
import os
from datetime import datetime

front_matter = (
"---\n" + 
"title: TITLE\n" + 
"publishDate: DATE\n" +
"last_modified_at: 2023-01-01T00:00:01\n" + 
"draft: false\n" +
"description: DESCRIPTION\n" +
"tags:\n" + 
"  - TAG_1\n" +
"  - TAG_2\n" +
"azure:\n" + 
"  dir: DIR\n" +
"  subdir: SUB\n" +  
"---\n\n" )

## Function definitions

def frame_dir_to_markdown(dir, prefix, ext="png"):

    # open the markdown file to be written
    md_name = os.path.basename(dir) + ".md"
    md = open( md_name, "w")

    all_files = [os.path.join(path, name) for path, subdirs, files in os.walk(dir) for name in files]
    files = []
    sorted = []

    for file in all_files:
        if file.lower().endswith(ext):
            files.append(file)

    # print(files)
    # print("")

    files.sort()

    # print(files)
    # print("")

    # Break the `prefix` and `dir` into parent/child parts
    parent = os.path.dirname(prefix)
    child = os.path.basename(dir)    

    # Substitute known values into the front matter
    a = front_matter.replace("DATE", datetime.now().strftime("%Y-%m-%d"))
    b = a.replace("DIR", parent)
    c = b.replace("SUB", child)

    # Write the front matter to the new .md file
    md.write(c) 

    # Add each file's `figure` declaration to the .md file
    for path in files:
        add_file_to_markdown(path, md, prefix)

    md.close()    


def add_file_to_markdown(path, md, prefix):
    base = os.path.basename(path)
    md.write('{{% figure title="Image file is ' + base + '" src="' + prefix + '/' + base + '" %}}  \n\n') 

## Main

ap = argparse.ArgumentParser()

ap.add_argument("-d", "--dir", required=False,
    help="path of images directory to generate markdown from")

ap.add_argument("-e", "--ext", required=False, default="png",
    help="the extension of images to process: 'jpg', 'png' or 'tif'")
    
ap.add_argument("-u", "--url", required=False, 
    help="Azure prefix/address to be generated")

args = vars(ap.parse_args())

if args["url"] is None or args["dir"] is None:
    ap.print_help()
else:

    ext = args["ext"].strip(".")
    dir = args["dir"].strip("/")
    url = args["url"].strip("/")

    print("processing: ." + ext + " files in " + dir + " with prefix " + url)
    frame_dir_to_markdown(dir, url, ext)


# ---
# title: Creating Better Documentation
# publishDate: 2023-02-04T10:36:03-06:00
# last_modified_at: 2023-02-04T20:33:36
# draft: false
# description: A new approach to creating better documentation here.
# tags:
#   - documentation
#   - Azure
# azure: 
#   dir: https://sddocs.blob.core.windows.net/documentation/
#   subdir: Better-Documentation  
# ---