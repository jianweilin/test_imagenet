import os
im2rec_path = '~/anaconda3/lib/python3.6/site-packages/mxnet/tools/im2rec.py'
root = '/home1/qwang/imagenet/val'
os.system('python {} --quality 100 --num-thread 20 imagenet {}'.format(im2rec_path, root))