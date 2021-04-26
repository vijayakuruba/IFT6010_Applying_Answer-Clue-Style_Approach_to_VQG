import json
import numpy as np


def get_image_ids():
    IN_PATH_50 = "./dataq/processed/VQA/Human_Evaluation/new_samples.0-50.json"
    IN_PATH_100 = "./dataq/processed/VQA/Human_Evaluation/new_samples.50-100.json"

    f_50 = open(IN_PATH_50, 'r')
    f_100 = open(IN_PATH_100, 'r')

    d_50 = json.load(f_50)
    d_100 = json.load(f_100)

    f_50.close()
    f_100.close()

    image_ids = []

    for data in d_50["data"]:
        aid = data["image_id"]
        q = data["question"]
        image_ids.append(aid)

    for data in d_100["data"]:
        aid = data["image_id"]
        q = data["question"]
        image_ids.append(aid)

    print(len(image_ids))
    return image_ids


def run():
    OUT_PATH_EVAL = "./dataq/processed/VQA/Human_Evaluation/new_samples.eval.json"
    OUT_PATH_GOLD = "./dataq/processed/VQA/Human_Evaluation/new_samples.gold.json"
    QUESTIONS_PATH = "./dataq/processed/VQA/test.VQA.qg.generated.gpt2_Run2.json"
    IN_PATH = "./dataq/processed/VQA/vqa_test.json"

    q_file = open(QUESTIONS_PATH, 'r')
    in_file = open(IN_PATH, 'r')

    q_data = json.load(q_file)
    in_data = json.load(in_file)

    q_file.close()
    in_file.close()

    og_questions = []

    for data in in_data["data"]:
        im_id = int(data["image_id"])
        q = data["question"]["question_text"]
        a = data["answer_text"]
        og_questions.append([q, im_id, a])

    questions = []

    for data in q_data["data"][0]["paragraphs"]:
        og_q = data["qas"][0]["original_question"]
        q = data["qas"][0]["question"]
        a = data["qas"][0]["answers"][0]["text"]
        questions.append([og_q, q, a])

    output1 = {"data": []}
    output2 = {"data": []}

    n = len(og_questions)
    m = len(questions)
    i = j = 0
    while i < n and j < m:
        if og_questions[i][0] == questions[j][0]:
            q = questions[j][1]
            a = questions[j][2]
            im_id = og_questions[i][1]
            output1["data"].append({
                "image_id": im_id,
                "question": q,
                "answer": a,
                "question_is_relevant": 0,
                "question_is_meaningful": 0,
                "answer_is_correct": 0
            })
            output2["data"].append({
                "image_id": im_id,
                "original_question": og_questions[i][0],
                "original_answer": og_questions[i][2],
                "question_is_relevant": 0,
                "question_is_meaningful": 0,
                "answer_is_correct": 0
            })
            i += 1
            j += 1
        else:
            i += 1

    np.random.seed(0)
    idx = np.random.randint(0, len(output1["data"]), (100,))
    data1 = np.array(output1["data"])[idx]
    data1 = sorted(data1, key=lambda d: d["image_id"])
    data2 = np.array(output2["data"])[idx]
    data2 = sorted(data2, key=lambda d: d["image_id"])

    with open(OUT_PATH_EVAL, 'w') as fh:

        json.dump({"data": data1}, fh)

    with open(OUT_PATH_GOLD, 'w') as fh:
        json.dump({"data": data2}, fh)


if __name__ == '__main__':
    run()
