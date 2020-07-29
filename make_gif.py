import glob, os
import imageio

d ="."
for directory in [os.path.join(d, o) for o in os.listdir(d) 
                    if os.path.isdir(os.path.join(d,o))]:
    images = []
    print(directory)
    s = ""
    for filename in sorted(glob.glob(directory+"/*.png")):
        s += f"<img src = '{filename}'></img><br><br><br>"
    l = directory+'/changes.txt'
    s += f"<iframe src ='{l}' height = '1000px' width = '1000px'></iframe>"
    if len(s)!=0:
        with open(f'{directory}.html','w') as f:
            f.write(s)

        # print(filename)
#         images.append(imageio.imread(filename,as_gray = True))
#     if images:
#         imageio.mimsave(f'{directory[2:]}.gif', images,duration = 0.3)

# # os.chdir("/mydir")

# # for file in glob.glob("*.txt"):
