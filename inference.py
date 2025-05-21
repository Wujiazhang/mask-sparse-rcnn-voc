import mmdet
from mmdet.apis import DetInferencer
inferencer = DetInferencer(
    weights='work_dirs/mask_rcnn_r50_fpn_1x_coco2/epoch_66.pth',
    device='cuda:0'
)
inferencer('demo/out', out_dir='outputs/outmask', no_save_pred=False)
inferencer('demo/in', out_dir='outputs/inmask', no_save_pred=False)
#nohup python inference.py > sparsein.log 2>&1 &
#tensorboard --logdir=1cye/vis_data