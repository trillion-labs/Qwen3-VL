import re

# # Define placeholders for dataset paths

ANDROID_CONTROL_CASE1 = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_fixed/conversations_case1.jsonl",
    "data_path": "/home/work/.shared/kyuseok/format_data",
}

ANDROID_CONTROL_CASE2 = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_fixed/conversations_case2.jsonl",
    "data_path": "/home/work/.shared/kyuseok/format_data",
}

ANDROID_CONTROL_CASE3 = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_fixed/conversations_case3.jsonl",
    "data_path": "/home/work/.shared/kyuseok/format_data",
}

ANDROID_CONTROL_CASE4 = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_fixed/conversations_case4.jsonl",
    "data_path": "/home/work/.shared/kyuseok/format_data",
}

ANDROID_IN_THE_ZOO = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_in_the_zoo/aitz_merged_data_v2.json",
    "data_path": "/home/work/.shared/kyuseok/format_data",
}

AGENTRECK = {
    "annotation_path": "/home/work/.shared/data/mfm/json/arpo_sft/non_gui_agentic_task_arpo_sft.jsonl",
    "data_path": "",
}

ANDROID_IN_THE_WILD = {
    "annotation_path": "/home/work/.shared/data/mfm/json/AitW/train.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

AMEX = {
    "annotation_path": "/home/work/.shared/data/mfm/json/AMEX/train.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ARPO_SFT = {
    "annotation_path": "/home/work/.shared/data/mfm/json/arpo_sft/non_gui_agentic_task_arpo_sft.jsonl",
    "data_path": "",
}

UI_VISION = {
    "annotation_path": "/home/work/.shared/data/mfm/json/UI-Vision/ui_grounding_uivision_tasks.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

UI_VISION_4MP = {
    "annotation_path": "/home/work/.shared/data/mfm/json/UI-Vision-4MP/ui_grounding_uivision_4mp_train.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

GUI_R1 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/gui_r1/gui_r1_train.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

GUI_ODYSSEY = {
    "annotation_path": "/home/work/.shared/data/mfm/json/gui_odyssey/guiodyssey_action_prediction.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

# Jedi datasets
JEDI_AITW_L1 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_aitw-l1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AITW_L2 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_aitw-l2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AITW_L3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_aitw-l3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L1 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_amex-l1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L2 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_amex-l2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_amex-l3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ANDROID_CONTROL_V2 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_android_control-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COAT_V2 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_coat-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_FINAL_1_5M_CLEANED_SPLIT = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_component_final_1.5m_cleaned_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_DESCRIPTION = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_component_library_snap_icon_data_description_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_component_library_snap_icon_data_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_V1_130K = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_component_v1_130k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_DOC_DATA_NEW = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_doc_data_new.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_DOC_SCROLL_DATA_NEW = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_doc_scroll_data_new.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ETHERCALC_V1 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_ethercalc_v1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIACT_WEB_MULTI = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_guiact-web-multi.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIACT_WEB_SINGLE_V2 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_guiact-web-single-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIDE_SI_10K_V2 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_guide_si_10k-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIENV = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_guienv.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ICON_V0222_DESCRIPTION = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_icon_v0222_description_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ICON_V0222_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_icon_v0222_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_IOS_APP_DATA = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_ios_app_data_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT200K_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_layout200k_grounding_training_data_qwen25.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT200K = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_layout200k_training_data_qwen25.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT400K_CLAUDE_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_layout400k_claude_grounding_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT400K_CLAUDE = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_layout400k_claude_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_MAC_APP_DATA = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_mac_app_data_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_MIND2WEB_TRAIN = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_mind2web_train_v1.0.1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OMNIACT = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_omniact.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OS_LAYOUT_V1_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_os_layout_v1_grounding_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OS_LAYOUT_V1 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_os_layout_v1_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_FINAL_1_5M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_refusal_component_final_1.5m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_refusal_component_library_snap_icon_data_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_V1_130K = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_refusal_component_v1_130k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_GUIENV = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_refusal_guienv.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_ICON_V0222_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_refusal_icon_v0222_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_RICOSCA = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_refusal_ricosca.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_SEECLICK_MI_UI_TARS_CLEANED = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_refusal_seeclick_mi_ui_tars_cleaned.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_SEECLICK_UI_TARS_CLEANED_FIXED = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_refusal_seeclick_ui_tars_cleaned_fixed.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_TRAINING_DATA_ICON_GROUNDED_MERGED = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_refusal_training_data_icon_conversations-images_grounded_merged.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_RICOIG16K = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_ricoig16k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_RICOSCA = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_ricosca.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SEECLICK_MI_UI_TARS_CLEANED = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_seeclick_mi_ui_tars_cleaned.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SEECLICK_UI_TARS_CLEANED_FIXED = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_seeclick_ui_tars_cleaned_fixed.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SLIDE_V1_17K = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_slide_v1_17k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_TRAINING_DATA_ICON_GROUNDED_MERGED = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_training_data_icon_conversations-images_grounded_merged.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_TRAINING_DATA_ICON_PURE_COLOR_BACKGROUND = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_training_data_icon_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_UI_REFEXP = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_ui_refexp.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_WEBUI350K = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_webui350k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_WIDGET_CAPTIONING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi/jedi_widget_captioning.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

GUI_MID = {
    "annotation_path": "/home/work/.shared/data/GUIMid/GUIMid_fixed.json",
    "data_path": "/home/work/.shared/data/GUIMid",
}

data_dict = {
    "android_in_the_zoo": ANDROID_IN_THE_ZOO,
    "android_control_case1": ANDROID_CONTROL_CASE1,
    "android_control_case2": ANDROID_CONTROL_CASE2,
    "android_control_case3": ANDROID_CONTROL_CASE3,
    "android_control_case4": ANDROID_CONTROL_CASE4,
    "android_in_the_wild": ANDROID_IN_THE_WILD,
    "agentreck": AGENTRECK,
    "amex": AMEX,
    "arpo_sft": ARPO_SFT,
    "ui_vision": UI_VISION,
    "ui_vision_4mp": UI_VISION_4MP,
    "gui_r1": GUI_R1,
    "gui_odyssey": GUI_ODYSSEY,
    "jedi_aitw_l1": JEDI_AITW_L1,
    "jedi_aitw_l2": JEDI_AITW_L2,
    "jedi_aitw_l3": JEDI_AITW_L3,
    "jedi_amex_l1": JEDI_AMEX_L1,
    "jedi_amex_l2": JEDI_AMEX_L2,
    "jedi_amex_l3": JEDI_AMEX_L3,
    "jedi_android_control_v2": JEDI_ANDROID_CONTROL_V2,
    "jedi_coat_v2": JEDI_COAT_V2,
    "jedi_component_final_1_5m_cleaned_split": JEDI_COMPONENT_FINAL_1_5M_CLEANED_SPLIT,
    "jedi_component_library_snap_icon_data_description": JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_DESCRIPTION,
    "jedi_component_library_snap_icon_data_grounding": JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING,
    "jedi_component_v1_130k": JEDI_COMPONENT_V1_130K,
    "jedi_doc_data_new": JEDI_DOC_DATA_NEW,
    "jedi_doc_scroll_data_new": JEDI_DOC_SCROLL_DATA_NEW,
    "jedi_ethercalc_v1": JEDI_ETHERCALC_V1,
    "jedi_guiact_web_multi": JEDI_GUIACT_WEB_MULTI,
    "jedi_guiact_web_single_v2": JEDI_GUIACT_WEB_SINGLE_V2,
    "jedi_guide_si_10k_v2": JEDI_GUIDE_SI_10K_V2,
    "jedi_guienv": JEDI_GUIENV,
    "jedi_icon_v0222_description": JEDI_ICON_V0222_DESCRIPTION,
    "jedi_icon_v0222_grounding": JEDI_ICON_V0222_GROUNDING,
    "jedi_ios_app_data": JEDI_IOS_APP_DATA,
    "jedi_layout200k_grounding": JEDI_LAYOUT200K_GROUNDING,
    "jedi_layout200k": JEDI_LAYOUT200K,
    "jedi_layout400k_claude_grounding": JEDI_LAYOUT400K_CLAUDE_GROUNDING,
    "jedi_layout400k_claude": JEDI_LAYOUT400K_CLAUDE,
    "jedi_mac_app_data": JEDI_MAC_APP_DATA,
    "jedi_mind2web_train": JEDI_MIND2WEB_TRAIN,
    "jedi_omniact": JEDI_OMNIACT,
    "jedi_os_layout_v1_grounding": JEDI_OS_LAYOUT_V1_GROUNDING,
    "jedi_os_layout_v1": JEDI_OS_LAYOUT_V1,
    "jedi_refusal_component_final_1_5m": JEDI_REFUSAL_COMPONENT_FINAL_1_5M,
    "jedi_refusal_component_library_snap_icon_data_grounding": JEDI_REFUSAL_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING,
    "jedi_refusal_component_v1_130k": JEDI_REFUSAL_COMPONENT_V1_130K,
    "jedi_refusal_guienv": JEDI_REFUSAL_GUIENV,
    "jedi_refusal_icon_v0222_grounding": JEDI_REFUSAL_ICON_V0222_GROUNDING,
    "jedi_refusal_ricosca": JEDI_REFUSAL_RICOSCA,
    "jedi_refusal_seeclick_mi_ui_tars_cleaned": JEDI_REFUSAL_SEECLICK_MI_UI_TARS_CLEANED,
    "jedi_refusal_seeclick_ui_tars_cleaned_fixed": JEDI_REFUSAL_SEECLICK_UI_TARS_CLEANED_FIXED,
    "jedi_refusal_training_data_icon_grounded_merged": JEDI_REFUSAL_TRAINING_DATA_ICON_GROUNDED_MERGED,
    "jedi_ricoig16k": JEDI_RICOIG16K,
    "jedi_ricosca": JEDI_RICOSCA,
    "jedi_seeclick_mi_ui_tars_cleaned": JEDI_SEECLICK_MI_UI_TARS_CLEANED,
    "jedi_seeclick_ui_tars_cleaned_fixed": JEDI_SEECLICK_UI_TARS_CLEANED_FIXED,
    "jedi_slide_v1_17k": JEDI_SLIDE_V1_17K,
    "jedi_training_data_icon_grounded_merged": JEDI_TRAINING_DATA_ICON_GROUNDED_MERGED,
    "jedi_training_data_icon_pure_color_background": JEDI_TRAINING_DATA_ICON_PURE_COLOR_BACKGROUND,
    "jedi_ui_refexp": JEDI_UI_REFEXP,
    "jedi_webui350k": JEDI_WEBUI350K,
    "jedi_widget_captioning": JEDI_WIDGET_CAPTIONING,
    "gui_mid": GUI_MID,
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