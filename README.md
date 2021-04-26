# IFT6010_Applying_Answer-Clue-Style_Approach_to_VQG
Project Course work for IFT6010

This project works on on paper https://arxiv.org/abs/2002.00748 and the code is adapted from https://github.com/BangLiu/ACS-QG

1. Down load the datasets to train -  use setup.sh file to download all required files and use Create_Glove_bin.py file to create Glove bin files
2. Dowmload VQA datasets from https://visualqa.org/download.html 
3. Train the GPT2-ACS model with Squad1.1 dataset using Step_1_QG_train_gpt2.sh 
4. Evaluate model with Step_2_Generate_Evaluate.sh
