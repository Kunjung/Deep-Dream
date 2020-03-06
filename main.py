import subprocess

# Image files stored in img folder
image_filename_list = [
    # 'honeyandclover.jpg',
    # 'idinvaded.jpg',
    # 'night.png',
    'run.png',
    'shrimp.jpg',
    'telescope.jpg',
    'weather.jpg',
]


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
