import argparse
import os

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

    for path in files:
        add_file_to_markdown(path, md, prefix)

    md.close()    


def add_file_to_markdown(path, md, prefix):
    base = os.path.basename(path)
    md.write("{{% figure title='Image file is " + base + "' src='" + prefix + "/" + base + " %}}  \n\n") 


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

    ext = args["extension"].strip(".")
    dir = args["dir"].strip("/")
    url = args["url"].strip("/")

    print("processing: ." + ext + " files in " + dir + " with prefix " + url)
    frame_dir_to_markdown(dir, url, ext)


