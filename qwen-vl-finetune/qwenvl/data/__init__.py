import re

# # Define placeholders for dataset paths

ANDROID_IN_THE_ZOO = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_in_the_zoo/aitz_merged_data_v2.json",
    "data_path": "/home/work/.shared/kyuseok/format_data",
}

AGENTRECK = {
    "annotation_path": "/home/work/.shared/data/mfm/json/arpo_sft/non_gui_agentic_task_arpo_sft.jsonl",
    "data_path": "",
}

data_dict = {
    "android_in_the_zoo": ANDROID_IN_THE_ZOO,
    "agentreck": AGENTRECK,
}


def parse_sampling_rate(dataset_name):
    match = re.search(r"%(\d+)$", dataset_name)
    if match:
        return int(match.group(1)) / 100.0
    return 1.0


def data_list(dataset_names):
    config_list = []
    for dataset_name in dataset_names:
        sampling_rate = parse_sampling_rate(dataset_name)
        dataset_name = re.sub(r"%(\d+)$", "", dataset_name)
        if dataset_name in data_dict.keys():
            config = data_dict[dataset_name].copy()
            config["sampling_rate"] = sampling_rate
            config_list.append(config)
        else:
            raise ValueError(f"do not find {dataset_name}")
    return config_list


if __name__ == "__main__":
    dataset_names = ["android_in_the_zoo"]
    configs = data_list(dataset_names)
    for config in configs:
        print(config)
