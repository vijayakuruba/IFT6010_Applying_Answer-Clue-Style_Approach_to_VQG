import json


def load_image_captions(path, captions_dict=None):
    with open(path, 'r') as fh:
        if captions_dict is None:
            captions_dict = dict()
        data = json.load(fh)
        for caption in data:
            captions_dict[caption["image_id"]] = '. '.join(
                list(map(lambda x: x.strip().capitalize(), caption["caption"].split('.'))))

    return captions_dict


def main():
    OUT_PATH = "./dataq/processed/VQA/vqa_test.json"
    ANSWERS_PATH = "./dataq/original/VQA/v2_mscoco_val2014_annotations.json"
    QUESTIONS_PATH = "./dataq/original/VQA/v2_OpenEnded_mscoco_val2014_questions.json"
    CAPTIONS_PATH = "./dataq/original/VQA/predictions_test_val_split_bs2.json"

    q_file = open(QUESTIONS_PATH, 'r')
    a_file = open(ANSWERS_PATH, 'r')
    q_data = json.load(q_file)
    a_data = json.load(a_file)

    captions = load_image_captions(CAPTIONS_PATH)

    output = {"data": []}
    n_items = 0
    pos = 0
    # q_types = set()
    for d in q_data["questions"]:
        aid = d["image_id"]
        if aid in captions:
            n_items += 1
            ann = a_data["annotations"][pos]
            output["data"].append({
                "image_id": aid,
                "context": captions[aid],
                "answer_text": ann["multiple_choice_answer"],
                "question": {
                    "question_type": ann["question_type"],
                    "question_text": d["question"]
                }
            })
            # q_types.add(ann["question_type"])

        if n_items == len(captions):
            break
        pos += 1

    q_file.close()
    a_file.close()

    # print(q_types)

    with open(OUT_PATH, 'w') as f:
        json.dump(output, f)


if __name__ == '__main__':
    main()
