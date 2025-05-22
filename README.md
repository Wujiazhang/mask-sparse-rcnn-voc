# mask-sparse-rcnn-voc
在VOC数据集上训练mask/sparse-rcnn

环境配置：torch 1.12.0+cu116

mmdetection安装：
pip3 install -U openmim
mim install mmengine
mim install "mmcv==2.1.0"
mim install mmdet

数据集：VOC数据集通过官网下载。VOC数据转COCO格式运行代码：
python voc_to_coco.py
python split.py

注：需要需改路径。
训练命令：
python train.py  configs/mask_rcnn_r50_fpn_1x_coco2.py
python train.py  configs/sparse_rcnn_r50_fpn_1x_coco2.py

模型推理：
python inference.py

生成Mask-rcnn一阶段proposalbox: 
python proposalbox.py

Tensorboard可视化：
python showtensorboard.py
tensorboard --logdir=your logfile path

