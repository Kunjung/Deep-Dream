import subprocess
import os

# Image files stored in img folder
direct_image_filename_list = [
    # 'honeyandclover.jpg',
    # 'idinvaded.jpg',
    # 'night.png',
    'run.png',
    'shrimp.jpg',
    'telescope.jpg',
    'weather.jpg',
]

image_filename_list = os.listdir('img')  # lists all filenames present in img
# filter only .png and .jpg image files
image_filename_list = [filename for filename in image_filename_list if (filename.endswith('.jpg') or filename.endswith('.png'))]

if len(image_filename_list) > 15:
    ## likely got some unnecessary files, remove and reset to direct_image_filename_list
    image_filename_list = direct_image_filename_list


for image_filename in image_filename_list:
    output_name = image_filename.split('.')[0] + '.png'
    script_name = 'deep_dream.py'
    print('image_filename', image_filename)
    print('output_name', output_name)
    command = 'python {0} img/{1} result/{2}'.format(script_name, image_filename, output_name)
    print('command', command)
    try:
        subprocess.Popen(command, shell=True)
    except Exception as e:
        print("Got Error", e)
