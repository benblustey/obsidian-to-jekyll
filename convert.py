import sys
import os
import shutil
import re
from pathlib import Path

def update_content(string):
    # convert image paths for Jekyll structure
    pattern = r'!\[\[(.*?)\]\]'
    # Find all non-overlapping matches of the pattern
    matches = list(re.finditer(pattern, string))
    # Initialize the resulting string as the original string
    modified_string = string
    # Iterate over the matches in reverse order to avoid messing up the indices
    for match in reversed(matches):
        # Extract the match content
        value = match.group(1)
        # Construct the new format
        new_value = f"![Desktop View](/assets/images/posts/{value})"
        # Get the start and end indices of the match
        start, end = match.span()
        # Replace the matched substring in the original string
        modified_string = modified_string[:start] + new_value + modified_string[end:]
    return modified_string

def process_directory(input_dir, output_dir):

    for file in os.listdir(input_dir):
        
        curr_file_path = os.path.join(input_dir, file)
        # only process file if the extension is .MD
        if file.endswith(".md"):
            with open(curr_file_path, "r") as f:
                content = f.read().lstrip().replace("&nbsp;", " ")
                title_clean = file[:-3].replace("&", "and")

                if content.startswith("---\n") and len(content.split("---\n")) >= 3:  # yaml already therex``
                    post_date = content.split("date: ")[1]
                    post_date = post_date.split("\n", 1)[0]

                file_name_clean = title_clean.replace("&nbsp;", " ").replace(" ", "_").lower()
                file_name_clean = post_date + '_' + file_name_clean + '.md'

                output = update_content(content)

            # get the date variable from the MD file
            with open(os.path.join(output_dir, file_name_clean), "w") as f:
                f.write(output)

if __name__ == '__main__':

    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print("Invalid number of commandline parameters")
        exit(1)

    input_dir = os.path.join(os.getcwd(), os.path.normpath(sys.argv[1]))
    output_dir = os.path.join(os.getcwd(), os.path.normpath(sys.argv[2]))

    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
    # else:
    #     for f in os.listdir(output_dir):
    #         os.remove(os.path.join(output_dir, f))
    
    ## IMAGE PROCESSING
    input_img_dir = input_dir + '/images'
    output_img_dir = output_dir + '/images'

    # create a image directory if not found
    if not os.path.isdir(output_img_dir):
        os.mkdir(output_img_dir)
    else:
        # delete all images
        # not sure if I need to do this
        for f in os.listdir(output_img_dir):
            os.remove(os.path.join(output_img_dir, f))

    # copy image directory to output_dir
    files=os.listdir(input_img_dir)
    for fname in files:
        # should add some file renames to replace any possible spaces
        shutil.copy2(os.path.join(input_img_dir,fname), output_img_dir)

    ## Process the MD files
    process_directory(input_dir, output_dir)
