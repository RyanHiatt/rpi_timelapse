import glob
import os

list_of_images = glob.glob(f"/media/ryanhiatt/D1D3-3025/*.jpg")
latest_file = max(list_of_images, key=os.path.getctime)
print(latest_file)
print(latest_file.split('.')[0].split('image')[0])
file_index = int(latest_file.split('.')[0].split('image')[1])
print(file_index)