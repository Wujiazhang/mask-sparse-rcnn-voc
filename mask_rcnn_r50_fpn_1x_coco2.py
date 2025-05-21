_base_ = [
    '_base_/models/mask-rcnn_r50_fpn.py',
    '_base_/datasets/coco_instance.py',
    '_base_/schedules/schedule_1x.py',
    '_base_/default_runtime.py'
]
log_config = dict(
    interval=1,
    hooks=[
        dict(type='TextLoggerHook'),
        dict(type='TensorboardLoggerHook', log_dir='/work/jpma/testproject3/VOCdetection/work_dirs/mask_rcnn_r50_fpn_1x_coco2')  # 自定义日志目录
    ])
train_cfg = dict(max_epochs=100, val_interval=7)
#CUDA_VISIBLE_DEVICES=7 nohup python tools/train.py  configs/mask_rcnn_r50_fpn_1x_coco2.py > MASK2.log 2>&1 &
#nohup python tools/test.py configs/mask_rcnn_r50_fpn_1x_coco.py work_dirs/mask_rcnn_r50_fpn_1x_voc/epoch_12.pth > MASKtest.log 2>&1 &