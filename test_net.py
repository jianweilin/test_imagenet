import mxnet as mx
from mxnet.gluon.data import DataLoader
from mxnet.gluon.model_zoo import vision as models
from mxnet.gluon.data.vision import ImageRecordDataset

def test(val_data):
    metrics = [mx.metric.Accuracy(), mx.metric.TopKAccuracy(5)]
    mod = mx.module.Module.load('resnet50', 0, context=ctx)
    mod.bind(for_training=False,
         data_shapes=val_data.provide_data,
         label_shapes=val_data.provide_label)
    score = mod.score(val_data, metrics)
    return score

if __name__ == '__main__':
    val_dir = '/home/zhbli/Project/test_imagenet/Dataset/imagenet_val.rec'
    batch_size = 64
    ctx = mx.gpu(1)
    val_dataiter = mx.io.ImageRecordIter(
        path_imgrec="./Dataset/imagenet_val.rec",
        data_shape=(3, 224, 224),
        batch_size=batch_size,
        prefetch_buffer=4,
        min_img_size=224,
        preprocess_threads=20,
        resize=256, # if do not resize, acc will decline by five points
        round_batch=False)
    score = test(val_dataiter)
    print(score) # [('accuracy', 0.75081921355498726), ('top_k_accuracy_5', 0.92599104859335035)]
