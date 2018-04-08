'''
Convert val.txt (no index) to  <prefix>_val.txt (with index).
Format of <prefix>_val.txt:
integer_image_index \t label_index \t path_to_image
This is an example file:
95099  464     n04467665_17283.JPEG
10025081        412     ILSVRC2010_val_00025082.JPEG
74181   789     n01915811_2739.JPEG
10035553        859     ILSVRC2010_val_00035554.JPEG
10048727        929     ILSVRC2010_val_00048728.JPEG
94028   924     n01980166_4956.JPEG
1080682 650     n11807979_571.JPEG
972457  633     n07723039_1627.JPEG
7534    11      n01630670_4486.JPEG
1191261 249     n12407079_5106.JPEG
'''

def make_list(file_in):
    index = 0
    fout = open(file_out, 'w')
    with open(file_in) as fin:
        while True:
            index = index + 1
            line = fin.readline()
            if not line:
                break
            path_to_image, label_index = line.split()
            new_line = str(index) + '\t' + label_index + '\t' + path_to_image + '\n'
            fout.write(new_line)
    fout.close()

file_in = 'val.txt'
file_out = 'imagenet_val.lst'
make_list(file_in)