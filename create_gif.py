import imageio.v3 as iio

# List your image filenames
filenames = [
    'image1.jpg',
    'image2.jpg',
    'image3.jpg',
]

# Read all images into a list
images = []
for filename in filenames:
    images.append(iio.imread(filename))

# Create the GIF
iio.imwrite('my_animation.gif', images, duration=200, loop=0)

print("GIF created successfully!")