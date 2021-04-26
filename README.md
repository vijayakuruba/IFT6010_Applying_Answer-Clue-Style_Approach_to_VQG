# IFT6010_Applying_Answer-Clue-Style_Approach_to_VQG
This repo is cretaed as a part of project course work for IFT6010 - 2021.
In this project,  we  adapt  Liu  Bang’s  Answer-Clue-Style-aware approach to the VQG task. Ourgoal is to develop a scalable system that can automatically generate diverse and high-quality visual question-answers pairs from a set of un-labelled  images. The  proposed  pipeline  is  a combination  of  an  image  captioning  module that extracts detailed and meaningful information from an image and an ACS-aware question generation module that produces question-answers pairs from the extracted visual infor-mation. 

This project works on on paper https://arxiv.org/abs/2002.00748 and the code is adapted from https://github.com/BangLiu/ACS-QG

1. Down load the datasets to train -  use setup.sh file to download all required files and use Create_Glove_bin.py file to create Glove bin files
2. Download VQA datasets from https://visualqa.org/download.html
3. Install requirements.txt
4. Run_mergevqa.sh. This will merge Caption generated from Image model,Questions from VQA datset,image id from Annotations to give vqa_test.json file.
5. Train the GPT2-ACS model with Squad1.1 dataset using Step_1_QG_train_gpt2.sh 
6. Evaluate model with Step_2_Generate_Evaluate.sh
