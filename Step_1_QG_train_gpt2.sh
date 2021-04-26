#!/usr/bin/env python3
import os
import logging

# Set up the logger
logging.basicConfig(format='%(asctime)s : %(message)s', datefmt="%H:%M:%S",
                    level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("1) QG_gpt2_train.py ")
print("*"*80)

os.system('CUDA_VISIBLE_DEVICES=0 python3 QG_gpt2_train.py \
    --eval_before_start \
    --n_epochs 4 \
    --model_name_or_path "./dataq/output/QG/gpt2_question_generation" \
    --output_dir "./dataq/output/QG/gpt2_question_generation" \
    --train_dataset_path "./dataq/original/SQuAD1.1-Zhou/train.txt" \
    --dev_dataset_path "./dataq/original/SQuAD1.1-Zhou/dev.txt" ')
	
