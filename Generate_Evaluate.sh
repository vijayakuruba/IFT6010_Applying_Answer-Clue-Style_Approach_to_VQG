#!/bin/bash

CUDA_VISIBLE_DEVICES=0 PYTHONIOENCODING=utf-8 python3 QG_gpt2_generate.py \
  --model_type gpt2 \
  --model_name_or_path "./dataq/output/QG/gpt2_question_generation" \
  --calc_tg_metrics \
  --filename "./dataq/processed/VQA/vqa_test.json" \
  --filecache "" \
  --data_type vqa \
  --output_file "./dataq/processed/VQA/test.VQA.qg.generated.gpt2_Run2.json"
#  --debug

#Test on Squad1.1
#    PYTHONIOENCODING=utf-8 python3 QG_gpt2_generate.py \
#    --model_type gpt2 \
#    --model_name_or_path "./dataq/output/QG/gpt2_question_generation"\
#	--calc_tg_metrics \
#    --filename "./dataq/original/SQuAD1.1-Zhou/test.txt" \
#    --filecache "" \
#    --data_type squad  \
#    --output_file "./dataq/processed/SQuAD1.1-Zhou/test.squad1.1.qg.generated.gpt2.json"

# test on SQuAD
#input_path="./dataq/original/SQuAD2.0/"
#output_path="./dataq/processed/SQuAD2.0/"
#data_type="squad"
#data_file_prefix="train"
#st_idx=0
#ed_idx=5000

#CUDA_VISIBLE_DEVICES=0 PYTHONIOENCODING=utf-8 python3 QG_gpt2_generate.py \
#    --model_type gpt2 \
#    --model_name_or_path "./dataq/output/QG/gpt2_question_generation" \
#	--calc_tg_metrics \
#    --filename ""  \
#    --filecache "$output_path${data_file_prefix}.sentences.augmented.${st_idx}_${ed_idx}.pkl" \
#    --data_type augmented_sents \
#    --output_file "$output_path${data_file_prefix}.qa.${st_idx}_${ed_idx}.qg.generated.gpt2.debug.check.json" \
#	--debug
