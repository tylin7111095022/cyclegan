set -ex
python train.py --dataroot ./datasets/chromosome/train --name maps_image_cyclegan --model cycle_gan --pool_size 50 --dataset_mode unaligned
