import re

# # Define placeholders for dataset paths

LLAVA_ONE_VISION = {
    "annotation_path": "/home/work/.shared/data/mfm/json/llava-onevision/general_vqa_sampled.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}
ANDROID_CONTROL_CASE1 = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_2M/conversations_case1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE2 = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_2M/conversations_case2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE3 = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_2M/conversations_case3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE4 = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_2M/conversations_case4.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE1_1M = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_1M/conversations_case1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE2_1M = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_1M/conversations_case2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE3_1M = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_1M/conversations_case3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE4_1M = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_1M/conversations_case4.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}
ANDROID_CONTROL_CASE1_4M = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_4M/conversations_case1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE2_4M = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_4M/conversations_case2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE3_4M = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_4M/conversations_case3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE4_4M = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_4M/conversations_case4.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_IN_THE_ZOO = {
    "annotation_path": "/home/work/.shared/data/mfm/json/android_in_the_zoo/aitz_data_filtered.jsonl",
    "data_path": "/home/work/.shared/kyuseok/format_data",
}

AGENTRECK = {
    "annotation_path": "/home/work/.shared/data/mfm/json/arpo_sft/non_gui_agentic_task_arpo_sft.jsonl",
    "data_path": "",
}

ANDROID_IN_THE_WILD = {
    "annotation_path": "/home/work/.shared/data/mfm/json/AitW/train_2m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

AMEX = {
    "annotation_path": "/home/work/.shared/data/mfm/json/AMEX/train_2m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ARPO_SFT = {
    "annotation_path": "/home/work/.shared/data/mfm/json/arpo_sft/non_gui_agentic_task_arpo_sft.jsonl",
    "data_path": "",
}

UI_VISION = {
    "annotation_path": "/home/work/.shared/data/mfm/json/UI-Vision/ui_grounding_uivision_tasks_2m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}


UI_VISION_4MP = {
    "annotation_path": "/home/work/.shared/data/mfm/json/UI-Vision-4MP/ui_grounding_uivision_4mp_train_2m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}


ANDROID_IN_THE_WILD_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/AitW/train_1m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_IN_THE_WILD_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/AitW/train_4m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

AMEX_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/AMEX/train_1m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

AMEX_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/AMEX/train_4m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

UI_VISION_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/UI-Vision/ui_grounding_uivision_tasks_1m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

UI_VISION_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/UI-Vision/ui_grounding_uivision_tasks_4m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

UI_VISION_4MP_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/UI-Vision-4MP/ui_grounding_uivision_4mp_train_1m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

UI_VISION_4MP_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/UI-Vision-4MP/ui_grounding_uivision_4mp_train_4m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

GUI_R1 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/gui_r1_2M/gui_r1_train.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

GUI_R1_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/gui_r1_1M/gui_r1_train.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

GUI_R1_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/gui_r1_4M/gui_r1_train.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

GUI_ODYSSEY = {
    "annotation_path": "/home/work/.shared/data/mfm/json/gui_odyssey_2M/guiodyssey_action_prediction.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

GUI_ODYSSEY_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/gui_odyssey_1M/guiodyssey_action_prediction.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

GUI_ODYSSEY_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/gui_odyssey_4M/guiodyssey_action_prediction.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

# Jedi datasets
JEDI_AITW_L1 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_aitw-l1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AITW_L1_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_aitw-l1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AITW_L1_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_aitw-l1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AITW_L2 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_aitw-l2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AITW_L2_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_aitw-l2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AITW_L2_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_aitw-l2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AITW_L3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_aitw-l3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AITW_L3_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_aitw-l3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AITW_L3_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_aitw-l3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L1 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_amex-l1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L1_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_amex-l1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L1_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_amex-l1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L2 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_amex-l2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L2_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_amex-l2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L2_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_amex-l2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_amex-l3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L3_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_amex-l3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L3_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_amex-l3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ANDROID_CONTROL_V2 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_android_control-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ANDROID_CONTROL_V2_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_android_control-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ANDROID_CONTROL_V2_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_android_control-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COAT_V2 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_coat-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COAT_V2_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_coat-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COAT_V2_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_coat-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}
JEDI_COMPONENT_FINAL_1_5M_CLEANED_SPLIT = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_component_final_1.5m_cleaned_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_FINAL_1_5M_CLEANED_SPLIT_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_component_final_1.5m_cleaned_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_FINAL_1_5M_CLEANED_SPLIT_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_component_final_1.5m_cleaned_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_DESCRIPTION = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_component_library_snap_icon_data_description_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_DESCRIPTION_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_component_library_snap_icon_data_description_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_DESCRIPTION_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_component_library_snap_icon_data_description_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}
JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_component_library_snap_icon_data_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_component_library_snap_icon_data_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_component_library_snap_icon_data_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_V1_130K = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_component_v1_130k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_V1_130K_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_component_v1_130k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_V1_130K_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_component_v1_130k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_DOC_DATA_NEW = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_doc_data_new.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_DOC_DATA_NEW_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_doc_data_new.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_DOC_DATA_NEW_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_doc_data_new.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_DOC_SCROLL_DATA_NEW = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_doc_scroll_data_new.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_DOC_SCROLL_DATA_NEW_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_doc_scroll_data_new.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_DOC_SCROLL_DATA_NEW_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_doc_scroll_data_new.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ETHERCALC_V1 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_ethercalc_v1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ETHERCALC_V1_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_ethercalc_v1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ETHERCALC_V1_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_ethercalc_v1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIACT_WEB_MULTI = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_guiact-web-multi.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIACT_WEB_MULTI_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_guiact-web-multi.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIACT_WEB_MULTI_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_guiact-web-multi.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIACT_WEB_SINGLE_V2 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_guiact-web-single-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIACT_WEB_SINGLE_V2_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_guiact-web-single-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIACT_WEB_SINGLE_V2_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_guiact-web-single-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIDE_SI_10K_V2 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_guide_si_10k-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIDE_SI_10K_V2_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_guide_si_10k-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIDE_SI_10K_V2_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_guide_si_10k-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIENV = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_guienv.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIENV_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_guienv.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIENV_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_guienv.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ICON_V0222_DESCRIPTION = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_icon_v0222_description_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ICON_V0222_DESCRIPTION_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_icon_v0222_description_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ICON_V0222_DESCRIPTION_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_icon_v0222_description_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ICON_V0222_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_icon_v0222_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ICON_V0222_GROUNDING_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_icon_v0222_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ICON_V0222_GROUNDING_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_icon_v0222_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_IOS_APP_DATA = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_ios_app_data_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_IOS_APP_DATA_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_ios_app_data_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_IOS_APP_DATA_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_ios_app_data_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT200K_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_layout200k_grounding_training_data_qwen25.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT200K_GROUNDING_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_layout200k_grounding_training_data_qwen25.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT200K_GROUNDING_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_layout200k_grounding_training_data_qwen25.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT200K = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_layout200k_training_data_qwen25.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT200K_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_layout200k_training_data_qwen25.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT200K_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_layout200k_training_data_qwen25.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}
JEDI_LAYOUT400K_CLAUDE_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_layout400k_claude_grounding_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}



JEDI_LAYOUT400K_CLAUDE_GROUNDING_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_layout400k_claude_grounding_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT400K_CLAUDE_GROUNDING_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_layout400k_claude_grounding_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}
JEDI_LAYOUT400K_CLAUDE = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_layout400k_claude_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT400K_CLAUDE_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_layout400k_claude_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT400K_CLAUDE_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_layout400k_claude_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}
JEDI_MAC_APP_DATA = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_mac_app_data_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_MAC_APP_DATA_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_mac_app_data_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_MAC_APP_DATA_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_mac_app_data_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_MIND2WEB_TRAIN = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_mind2web_train_v1.0.1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_MIND2WEB_TRAIN_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_mind2web_train_v1.0.1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_MIND2WEB_TRAIN_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_mind2web_train_v1.0.1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OMNIACT = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_omniact.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OMNIACT_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_omniact.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OMNIACT_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_omniact.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OS_LAYOUT_V1_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_os_layout_v1_grounding_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OS_LAYOUT_V1_GROUNDING_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_os_layout_v1_grounding_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OS_LAYOUT_V1_GROUNDING_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_os_layout_v1_grounding_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OS_LAYOUT_V1 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_os_layout_v1_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OS_LAYOUT_V1_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_os_layout_v1_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OS_LAYOUT_V1_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_os_layout_v1_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_FINAL_1_5M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_refusal_component_final_1.5m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_FINAL_1_5M_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_refusal_component_final_1.5m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_FINAL_1_5M_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_refusal_component_final_1.5m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_refusal_component_library_snap_icon_data_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_refusal_component_library_snap_icon_data_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_refusal_component_library_snap_icon_data_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_V1_130K = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_refusal_component_v1_130k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_V1_130K_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_refusal_component_v1_130k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_V1_130K_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_refusal_component_v1_130k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_GUIENV = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_refusal_guienv.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_GUIENV_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_refusal_guienv.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_GUIENV_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_refusal_guienv.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_ICON_V0222_GROUNDING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_refusal_icon_v0222_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_ICON_V0222_GROUNDING_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_refusal_icon_v0222_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_ICON_V0222_GROUNDING_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_refusal_icon_v0222_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_RICOSCA = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_refusal_ricosca.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_RICOSCA_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_refusal_ricosca.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_RICOSCA_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_refusal_ricosca.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_SEECLICK_MI_UI_TARS_CLEANED = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_refusal_seeclick_mi_ui_tars_cleaned.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_SEECLICK_MI_UI_TARS_CLEANED_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_refusal_seeclick_mi_ui_tars_cleaned.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_SEECLICK_MI_UI_TARS_CLEANED_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_refusal_seeclick_mi_ui_tars_cleaned.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_SEECLICK_UI_TARS_CLEANED_FIXED = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_refusal_seeclick_ui_tars_cleaned_fixed.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_SEECLICK_UI_TARS_CLEANED_FIXED_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_refusal_seeclick_ui_tars_cleaned_fixed.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_SEECLICK_UI_TARS_CLEANED_FIXED_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_refusal_seeclick_ui_tars_cleaned_fixed.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_TRAINING_DATA_ICON_GROUNDED_MERGED = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_refusal_training_data_icon_conversations-images_grounded_merged.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_TRAINING_DATA_ICON_GROUNDED_MERGED_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_refusal_training_data_icon_conversations-images_grounded_merged.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_TRAINING_DATA_ICON_GROUNDED_MERGED_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_refusal_training_data_icon_conversations-images_grounded_merged.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_RICOIG16K = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_ricoig16k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_RICOIG16K_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_ricoig16k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_RICOIG16K_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_ricoig16k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_RICOSCA = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_ricosca.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_RICOSCA_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_ricosca.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_RICOSCA_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_ricosca.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}
JEDI_SEECLICK_MI_UI_TARS_CLEANED = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_seeclick_mi_ui_tars_cleaned.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SEECLICK_MI_UI_TARS_CLEANED_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_seeclick_mi_ui_tars_cleaned.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SEECLICK_MI_UI_TARS_CLEANED_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_seeclick_mi_ui_tars_cleaned.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SEECLICK_UI_TARS_CLEANED_FIXED = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_seeclick_ui_tars_cleaned_fixed.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SEECLICK_UI_TARS_CLEANED_FIXED_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_seeclick_ui_tars_cleaned_fixed.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SEECLICK_UI_TARS_CLEANED_FIXED_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_seeclick_ui_tars_cleaned_fixed.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SLIDE_V1_17K = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_slide_v1_17k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SLIDE_V1_17K_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_slide_v1_17k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SLIDE_V1_17K_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_slide_v1_17k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_TRAINING_DATA_ICON_GROUNDED_MERGED = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_training_data_icon_conversations-images_grounded_merged.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_TRAINING_DATA_ICON_GROUNDED_MERGED_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_training_data_icon_conversations-images_grounded_merged.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_TRAINING_DATA_ICON_GROUNDED_MERGED_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_training_data_icon_conversations-images_grounded_merged.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_TRAINING_DATA_ICON_PURE_COLOR_BACKGROUND = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_training_data_icon_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_TRAINING_DATA_ICON_PURE_COLOR_BACKGROUND_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_training_data_icon_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_TRAINING_DATA_ICON_PURE_COLOR_BACKGROUND_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_training_data_icon_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_UI_REFEXP = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_ui_refexp.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_UI_REFEXP_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_ui_refexp.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_UI_REFEXP_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_ui_refexp.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_WEBUI350K = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_webui350k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_WEBUI350K_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_webui350k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_WEBUI350K_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_webui350k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_WIDGET_CAPTIONING = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_2M/jedi_widget_captioning.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_WIDGET_CAPTIONING_1M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_1M/jedi_widget_captioning.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_WIDGET_CAPTIONING_4M = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_4M/jedi_widget_captioning.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

GUI_MID = {
    "annotation_path": "/home/work/.shared/data/mfm/json/gui_mid/gui_mid.jsonl",
    "data_path": "/home/work/.shared/sungjun/GUIMid",
}

ANDROID_CONTROL_CASE1_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/android_control_qwen3vl/conversations_case1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE2_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/android_control_qwen3vl/conversations_case2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE3_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/android_control_qwen3vl/conversations_case3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE4_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/android_control_qwen3vl/conversations_case4.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_CONTROL_CASE1_1M = {
    "annotation_path": "/home/work/.shared/kyuseok/format_data/processed_data/android_control_qwen_style_action_history_1M/conversations_case1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

ANDROID_IN_THE_WILD_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/AitW/train_qwen3vl.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

AMEX_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/AMEX/train_qwen3vl.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}


UI_VISION_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/UI-Vision/ui_grounding_uivision_tasks_qwen3vl.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

UI_VISION_4MP_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/UI-Vision-4MP/ui_grounding_uivision_4mp_train_qwen3vl.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

GUI_R1_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/gui_r1_qwen3/gui_r1_train.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

GUI_ODYSSEY_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/gui_odyssey_qwen3/guiodyssey_action_prediction.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

# Jedi Qwen3 datasets
JEDI_AITW_L1_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_aitw-l1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AITW_L2_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_aitw-l2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AITW_L3_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_aitw-l3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L1_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_amex-l1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L2_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_amex-l2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_AMEX_L3_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_amex-l3.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ANDROID_CONTROL_V2_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_android_control-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COAT_V2_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_coat-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_FINAL_1_5M_CLEANED_SPLIT_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_component_final_1.5m_cleaned_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_DESCRIPTION_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_component_library_snap_icon_data_description_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_component_library_snap_icon_data_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_COMPONENT_V1_130K_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_component_v1_130k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_DOC_DATA_NEW_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_doc_data_new.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_DOC_SCROLL_DATA_NEW_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_doc_scroll_data_new.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ETHERCALC_V1_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_ethercalc_v1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIACT_WEB_MULTI_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_guiact-web-multi.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIACT_WEB_SINGLE_V2_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_guiact-web-single-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIDE_SI_10K_V2_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_guide_si_10k-v2.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_GUIENV_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_guienv.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ICON_V0222_DESCRIPTION_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_icon_v0222_description_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_ICON_V0222_GROUNDING_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_icon_v0222_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_IOS_APP_DATA_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_ios_app_data_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT200K_GROUNDING_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_layout200k_grounding_training_data_qwen25.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT200K_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_layout200k_training_data_qwen25.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT400K_CLAUDE_GROUNDING_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_layout400k_claude_grounding_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_LAYOUT400K_CLAUDE_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_layout400k_claude_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_MAC_APP_DATA_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_mac_app_data_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_MIND2WEB_TRAIN_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_mind2web_train_v1.0.1.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OMNIACT_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_omniact.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OS_LAYOUT_V1_GROUNDING_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_os_layout_v1_grounding_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_OS_LAYOUT_V1_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_os_layout_v1_training_data_qwen25_split.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_FINAL_1_5M_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_refusal_component_final_1.5m.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_refusal_component_library_snap_icon_data_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_COMPONENT_V1_130K_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_refusal_component_v1_130k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_GUIENV_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_refusal_guienv.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_ICON_V0222_GROUNDING_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_refusal_icon_v0222_grounding_conversations.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_RICOSCA_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_refusal_ricosca.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_SEECLICK_MI_UI_TARS_CLEANED_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_refusal_seeclick_mi_ui_tars_cleaned.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_SEECLICK_UI_TARS_CLEANED_FIXED_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_refusal_seeclick_ui_tars_cleaned_fixed.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_REFUSAL_TRAINING_DATA_ICON_GROUNDED_MERGED_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_refusal_training_data_icon_conversations-images_grounded_merged.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_RICOIG16K_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_ricoig16k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_RICOSCA_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_ricosca.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SEECLICK_MI_UI_TARS_CLEANED_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_seeclick_mi_ui_tars_cleaned.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SEECLICK_UI_TARS_CLEANED_FIXED_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_seeclick_ui_tars_cleaned_fixed.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_SLIDE_V1_17K_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_slide_v1_17k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_TRAINING_DATA_ICON_GROUNDED_MERGED_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_training_data_icon_conversations-images_grounded_merged.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_TRAINING_DATA_ICON_PURE_COLOR_BACKGROUND_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_training_data_icon_conversations-images_pure_color_background.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_UI_REFEXP_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_ui_refexp.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_WEBUI350K_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_webui350k.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}

JEDI_WIDGET_CAPTIONING_QWEN3 = {
    "annotation_path": "/home/work/.shared/data/mfm/json/jedi_qwen3/jedi_widget_captioning.jsonl",
    "data_path": "/home/work/.shared/data/mfm/images",
}


MMMU_R1 = {
    "annotation_path": "/mnt/vast/trillion/hyungguk/Qwen3-VL/qwen-vl-finetune/data/mmmu_r1/train.jsonl",
    "data_path": "/mnt/vast/trillion/hyungguk/Qwen3-VL/qwen-vl-finetune/data/mmmu_r1/images",
}

data_dict = {
    "mmmu_r1": MMMU_R1,
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
    "android_control_case1_1m": ANDROID_CONTROL_CASE1_1M,
    "android_control_case2_1m": ANDROID_CONTROL_CASE2_1M,
    "android_control_case3_1m": ANDROID_CONTROL_CASE3_1M,
    "android_control_case4_1m": ANDROID_CONTROL_CASE4_1M,
    "android_control_case1_4m": ANDROID_CONTROL_CASE1_4M,
    "android_control_case2_4m": ANDROID_CONTROL_CASE2_4M,
    "android_control_case3_4m": ANDROID_CONTROL_CASE3_4M,
    "android_control_case4_4m": ANDROID_CONTROL_CASE4_4M,
    "android_in_the_wild_1m": ANDROID_IN_THE_WILD_1M,
    "android_in_the_wild_4m": ANDROID_IN_THE_WILD_4M,
    "amex_1m": AMEX_1M,
    "amex_4m": AMEX_4M,
    "ui_vision_1m": UI_VISION_1M,
    "ui_vision_4m": UI_VISION_4M,
    "ui_vision_4mp_1m": UI_VISION_4MP_1M,
    "ui_vision_4mp_4m": UI_VISION_4MP_4M,
    "gui_r1_1m": GUI_R1_1M,
    "gui_r1_4m": GUI_R1_4M,
    "gui_odyssey_1m": GUI_ODYSSEY_1M,
    "gui_odyssey_4m": GUI_ODYSSEY_4M,
    "jedi_aitw_l1_1m": JEDI_AITW_L1_1M,
    "jedi_aitw_l1_4m": JEDI_AITW_L1_4M,
    "jedi_aitw_l2_1m": JEDI_AITW_L2_1M,
    "jedi_aitw_l2_4m": JEDI_AITW_L2_4M,
    "jedi_aitw_l3_1m": JEDI_AITW_L3_1M,
    "jedi_aitw_l3_4m": JEDI_AITW_L3_4M,
    "jedi_amex_l1_1m": JEDI_AMEX_L1_1M,
    "jedi_amex_l1_4m": JEDI_AMEX_L1_4M,
    "jedi_amex_l2_1m": JEDI_AMEX_L2_1M,
    "jedi_amex_l2_4m": JEDI_AMEX_L2_4M,
    "jedi_amex_l3_1m": JEDI_AMEX_L3_1M,
    "jedi_amex_l3_4m": JEDI_AMEX_L3_4M,
    "jedi_android_control_v2_1m": JEDI_ANDROID_CONTROL_V2_1M,
    "jedi_android_control_v2_4m": JEDI_ANDROID_CONTROL_V2_4M,
    "jedi_coat_v2_1m": JEDI_COAT_V2_1M,
    "jedi_coat_v2_4m": JEDI_COAT_V2_4M,
    "jedi_component_final_1_5m_cleaned_split_1m": JEDI_COMPONENT_FINAL_1_5M_CLEANED_SPLIT_1M,
    "jedi_component_final_1_5m_cleaned_split_4m": JEDI_COMPONENT_FINAL_1_5M_CLEANED_SPLIT_4M,
    "jedi_component_library_snap_icon_data_description_1m": JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_DESCRIPTION_1M,
    "jedi_component_library_snap_icon_data_description_4m": JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_DESCRIPTION_4M,
    "jedi_component_library_snap_icon_data_grounding_1m": JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING_1M,
    "jedi_component_library_snap_icon_data_grounding_4m": JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING_4M,
    "jedi_component_v1_130k_1m": JEDI_COMPONENT_V1_130K_1M,
    "jedi_component_v1_130k_4m": JEDI_COMPONENT_V1_130K_4M,
    "jedi_doc_data_new_1m": JEDI_DOC_DATA_NEW_1M,
    "jedi_doc_data_new_4m": JEDI_DOC_DATA_NEW_4M,
    "jedi_doc_scroll_data_new_1m": JEDI_DOC_SCROLL_DATA_NEW_1M,
    "jedi_doc_scroll_data_new_4m": JEDI_DOC_SCROLL_DATA_NEW_4M,
    "jedi_ethercalc_v1_1m": JEDI_ETHERCALC_V1_1M,
    "jedi_ethercalc_v1_4m": JEDI_ETHERCALC_V1_4M,
    "jedi_guiact_web_multi_1m": JEDI_GUIACT_WEB_MULTI_1M,
    "jedi_guiact_web_multi_4m": JEDI_GUIACT_WEB_MULTI_4M,
    "jedi_guiact_web_single_v2_1m": JEDI_GUIACT_WEB_SINGLE_V2_1M,
    "jedi_guiact_web_single_v2_4m": JEDI_GUIACT_WEB_SINGLE_V2_4M,
    "jedi_guide_si_10k_v2_1m": JEDI_GUIDE_SI_10K_V2_1M,
    "jedi_guide_si_10k_v2_4m": JEDI_GUIDE_SI_10K_V2_4M,
    "jedi_guienv_1m": JEDI_GUIENV_1M,
    "jedi_guienv_4m": JEDI_GUIENV_4M,
    "jedi_icon_v0222_description_1m": JEDI_ICON_V0222_DESCRIPTION_1M,
    "jedi_icon_v0222_description_4m": JEDI_ICON_V0222_DESCRIPTION_4M,
    "jedi_icon_v0222_grounding_1m": JEDI_ICON_V0222_GROUNDING_1M,
    "jedi_icon_v0222_grounding_4m": JEDI_ICON_V0222_GROUNDING_4M,
    "jedi_ios_app_data_1m": JEDI_IOS_APP_DATA_1M,
    "jedi_ios_app_data_4m": JEDI_IOS_APP_DATA_4M,
    "jedi_layout200k_grounding_1m": JEDI_LAYOUT200K_GROUNDING_1M,
    "jedi_layout200k_grounding_4m": JEDI_LAYOUT200K_GROUNDING_4M,
    "jedi_layout200k_1m": JEDI_LAYOUT200K_1M,
    "jedi_layout200k_4m": JEDI_LAYOUT200K_4M,
    "jedi_layout400k_claude_grounding_1m": JEDI_LAYOUT400K_CLAUDE_GROUNDING_1M,
    "jedi_layout400k_claude_grounding_4m": JEDI_LAYOUT400K_CLAUDE_GROUNDING_4M,
    "jedi_layout400k_claude_1m": JEDI_LAYOUT400K_CLAUDE_1M,
    "jedi_layout400k_claude_4m": JEDI_LAYOUT400K_CLAUDE_4M,
    "jedi_mac_app_data_1m": JEDI_MAC_APP_DATA_1M,
    "jedi_mac_app_data_4m": JEDI_MAC_APP_DATA_4M,
    "jedi_mind2web_train_1m": JEDI_MIND2WEB_TRAIN_1M,
    "jedi_mind2web_train_4m": JEDI_MIND2WEB_TRAIN_4M,
    "jedi_omniact_1m": JEDI_OMNIACT_1M,
    "jedi_omniact_4m": JEDI_OMNIACT_4M,
    "jedi_os_layout_v1_grounding_1m": JEDI_OS_LAYOUT_V1_GROUNDING_1M,
    "jedi_os_layout_v1_grounding_4m": JEDI_OS_LAYOUT_V1_GROUNDING_4M,
    "jedi_os_layout_v1_1m": JEDI_OS_LAYOUT_V1_1M,
    "jedi_os_layout_v1_4m": JEDI_OS_LAYOUT_V1_4M,
    "jedi_refusal_component_final_1_5m_1m": JEDI_REFUSAL_COMPONENT_FINAL_1_5M_1M,
    "jedi_refusal_component_final_1_5m_4m": JEDI_REFUSAL_COMPONENT_FINAL_1_5M_4M,
    "jedi_refusal_component_library_snap_icon_data_grounding_1m": JEDI_REFUSAL_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING_1M,
    "jedi_refusal_component_library_snap_icon_data_grounding_4m": JEDI_REFUSAL_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING_4M,
    "jedi_refusal_component_v1_130k_1m": JEDI_REFUSAL_COMPONENT_V1_130K_1M,
    "jedi_refusal_component_v1_130k_4m": JEDI_REFUSAL_COMPONENT_V1_130K_4M,
    "jedi_refusal_guienv_1m": JEDI_REFUSAL_GUIENV_1M,
    "jedi_refusal_guienv_4m": JEDI_REFUSAL_GUIENV_4M,
    "jedi_refusal_icon_v0222_grounding_1m": JEDI_REFUSAL_ICON_V0222_GROUNDING_1M,
    "jedi_refusal_icon_v0222_grounding_4m": JEDI_REFUSAL_ICON_V0222_GROUNDING_4M,
    "jedi_refusal_ricosca_1m": JEDI_REFUSAL_RICOSCA_1M,
    "jedi_refusal_ricosca_4m": JEDI_REFUSAL_RICOSCA_4M,
    "jedi_refusal_seeclick_mi_ui_tars_cleaned_1m": JEDI_REFUSAL_SEECLICK_MI_UI_TARS_CLEANED_1M,
    "jedi_refusal_seeclick_mi_ui_tars_cleaned_4m": JEDI_REFUSAL_SEECLICK_MI_UI_TARS_CLEANED_4M,
    "jedi_refusal_seeclick_ui_tars_cleaned_fixed_1m": JEDI_REFUSAL_SEECLICK_UI_TARS_CLEANED_FIXED_1M,
    "jedi_refusal_seeclick_ui_tars_cleaned_fixed_4m": JEDI_REFUSAL_SEECLICK_UI_TARS_CLEANED_FIXED_4M,
    "jedi_refusal_training_data_icon_grounded_merged_1m": JEDI_REFUSAL_TRAINING_DATA_ICON_GROUNDED_MERGED_1M,
    "jedi_refusal_training_data_icon_grounded_merged_4m": JEDI_REFUSAL_TRAINING_DATA_ICON_GROUNDED_MERGED_4M,
    "jedi_ricoig16k_1m": JEDI_RICOIG16K_1M,
    "jedi_ricoig16k_4m": JEDI_RICOIG16K_4M,
    "jedi_ricosca_1m": JEDI_RICOSCA_1M,
    "jedi_ricosca_4m": JEDI_RICOSCA_4M,
    "jedi_seeclick_mi_ui_tars_cleaned_1m": JEDI_SEECLICK_MI_UI_TARS_CLEANED_1M,
    "jedi_seeclick_mi_ui_tars_cleaned_4m": JEDI_SEECLICK_MI_UI_TARS_CLEANED_4M,
    "jedi_seeclick_ui_tars_cleaned_fixed_1m": JEDI_SEECLICK_UI_TARS_CLEANED_FIXED_1M,
    "jedi_seeclick_ui_tars_cleaned_fixed_4m": JEDI_SEECLICK_UI_TARS_CLEANED_FIXED_4M,
    "jedi_slide_v1_17k_1m": JEDI_SLIDE_V1_17K_1M,
    "jedi_slide_v1_17k_4m": JEDI_SLIDE_V1_17K_4M,
    "jedi_training_data_icon_grounded_merged_1m": JEDI_TRAINING_DATA_ICON_GROUNDED_MERGED_1M,
    "jedi_training_data_icon_grounded_merged_4m": JEDI_TRAINING_DATA_ICON_GROUNDED_MERGED_4M,
    "jedi_training_data_icon_pure_color_background_1m": JEDI_TRAINING_DATA_ICON_PURE_COLOR_BACKGROUND_1M,
    "jedi_training_data_icon_pure_color_background_4m": JEDI_TRAINING_DATA_ICON_PURE_COLOR_BACKGROUND_4M,
    "jedi_ui_refexp_1m": JEDI_UI_REFEXP_1M,
    "jedi_ui_refexp_4m": JEDI_UI_REFEXP_4M,
    "jedi_webui350k_1m": JEDI_WEBUI350K_1M,
    "jedi_webui350k_4m": JEDI_WEBUI350K_4M,
    "jedi_widget_captioning_1m": JEDI_WIDGET_CAPTIONING_1M,
    "jedi_widget_captioning_4m": JEDI_WIDGET_CAPTIONING_4M,
    "android_control_case1_qwen3": ANDROID_CONTROL_CASE1_QWEN3,
    "android_control_case2_qwen3": ANDROID_CONTROL_CASE2_QWEN3,
    "android_control_case3_qwen3": ANDROID_CONTROL_CASE3_QWEN3,
    "android_control_case4_qwen3": ANDROID_CONTROL_CASE4_QWEN3,
    "android_in_the_wild_qwen3": ANDROID_IN_THE_WILD_QWEN3,
    "amex_qwen3": AMEX_QWEN3,
    "ui_vision_qwen3": UI_VISION_QWEN3,
    "ui_vision_4mp_qwen3": UI_VISION_4MP_QWEN3,
    "gui_r1_qwen3": GUI_R1_QWEN3,
    "gui_odyssey_qwen3": GUI_ODYSSEY_QWEN3,
    "jedi_aitw_l1_qwen3": JEDI_AITW_L1_QWEN3,
    "jedi_aitw_l2_qwen3": JEDI_AITW_L2_QWEN3,
    "jedi_aitw_l3_qwen3": JEDI_AITW_L3_QWEN3,
    "jedi_amex_l1_qwen3": JEDI_AMEX_L1_QWEN3,
    "jedi_amex_l2_qwen3": JEDI_AMEX_L2_QWEN3,
    "jedi_amex_l3_qwen3": JEDI_AMEX_L3_QWEN3,
    "jedi_android_control_v2_qwen3": JEDI_ANDROID_CONTROL_V2_QWEN3,
    "jedi_coat_v2_qwen3": JEDI_COAT_V2_QWEN3,
    "jedi_component_final_1_5m_cleaned_split_qwen3": JEDI_COMPONENT_FINAL_1_5M_CLEANED_SPLIT_QWEN3,
    "jedi_component_library_snap_icon_data_description_qwen3": JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_DESCRIPTION_QWEN3,
    "jedi_component_library_snap_icon_data_grounding_qwen3": JEDI_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING_QWEN3,
    "jedi_component_v1_130k_qwen3": JEDI_COMPONENT_V1_130K_QWEN3,
    "jedi_doc_data_new_qwen3": JEDI_DOC_DATA_NEW_QWEN3,
    "jedi_doc_scroll_data_new_qwen3": JEDI_DOC_SCROLL_DATA_NEW_QWEN3,
    "jedi_ethercalc_v1_qwen3": JEDI_ETHERCALC_V1_QWEN3,
    "jedi_guiact_web_multi_qwen3": JEDI_GUIACT_WEB_MULTI_QWEN3,
    "jedi_guiact_web_single_v2_qwen3": JEDI_GUIACT_WEB_SINGLE_V2_QWEN3,
    "jedi_guide_si_10k_v2_qwen3": JEDI_GUIDE_SI_10K_V2_QWEN3,
    "jedi_guienv_qwen3": JEDI_GUIENV_QWEN3,
    "jedi_icon_v0222_description_qwen3": JEDI_ICON_V0222_DESCRIPTION_QWEN3,
    "jedi_icon_v0222_grounding_qwen3": JEDI_ICON_V0222_GROUNDING_QWEN3,
    "jedi_ios_app_data_qwen3": JEDI_IOS_APP_DATA_QWEN3,
    "jedi_layout200k_grounding_qwen3": JEDI_LAYOUT200K_GROUNDING_QWEN3,
    "jedi_layout200k_qwen3": JEDI_LAYOUT200K_QWEN3,
    "jedi_layout400k_claude_grounding_qwen3": JEDI_LAYOUT400K_CLAUDE_GROUNDING_QWEN3,
    "jedi_layout400k_claude_qwen3": JEDI_LAYOUT400K_CLAUDE_QWEN3,
    "jedi_mac_app_data_qwen3": JEDI_MAC_APP_DATA_QWEN3,
    "jedi_mind2web_train_qwen3": JEDI_MIND2WEB_TRAIN_QWEN3,
    "jedi_omniact_qwen3": JEDI_OMNIACT_QWEN3,
    "jedi_os_layout_v1_grounding_qwen3": JEDI_OS_LAYOUT_V1_GROUNDING_QWEN3,
    "jedi_os_layout_v1_qwen3": JEDI_OS_LAYOUT_V1_QWEN3,
    "jedi_refusal_component_final_1_5m_qwen3": JEDI_REFUSAL_COMPONENT_FINAL_1_5M_QWEN3,
    "jedi_refusal_component_library_snap_icon_data_grounding_qwen3": JEDI_REFUSAL_COMPONENT_LIBRARY_SNAP_ICON_DATA_GROUNDING_QWEN3,
    "jedi_refusal_component_v1_130k_qwen3": JEDI_REFUSAL_COMPONENT_V1_130K_QWEN3,
    "jedi_refusal_guienv_qwen3": JEDI_REFUSAL_GUIENV_QWEN3,
    "jedi_refusal_icon_v0222_grounding_qwen3": JEDI_REFUSAL_ICON_V0222_GROUNDING_QWEN3,
    "jedi_refusal_ricosca_qwen3": JEDI_REFUSAL_RICOSCA_QWEN3,
    "jedi_refusal_seeclick_mi_ui_tars_cleaned_qwen3": JEDI_REFUSAL_SEECLICK_MI_UI_TARS_CLEANED_QWEN3,
    "jedi_refusal_seeclick_ui_tars_cleaned_fixed_qwen3": JEDI_REFUSAL_SEECLICK_UI_TARS_CLEANED_FIXED_QWEN3,
    "jedi_refusal_training_data_icon_grounded_merged_qwen3": JEDI_REFUSAL_TRAINING_DATA_ICON_GROUNDED_MERGED_QWEN3,
    "jedi_ricoig16k_qwen3": JEDI_RICOIG16K_QWEN3,
    "jedi_ricosca_qwen3": JEDI_RICOSCA_QWEN3,
    "jedi_seeclick_mi_ui_tars_cleaned_qwen3": JEDI_SEECLICK_MI_UI_TARS_CLEANED_QWEN3,
    "jedi_seeclick_ui_tars_cleaned_fixed_qwen3": JEDI_SEECLICK_UI_TARS_CLEANED_FIXED_QWEN3,
    "jedi_slide_v1_17k_qwen3": JEDI_SLIDE_V1_17K_QWEN3,
    "jedi_training_data_icon_grounded_merged_qwen3": JEDI_TRAINING_DATA_ICON_GROUNDED_MERGED_QWEN3,
    "jedi_training_data_icon_pure_color_background_qwen3": JEDI_TRAINING_DATA_ICON_PURE_COLOR_BACKGROUND_QWEN3,
    "jedi_ui_refexp_qwen3": JEDI_UI_REFEXP_QWEN3,
    "jedi_webui350k_qwen3": JEDI_WEBUI350K_QWEN3,
    "jedi_widget_captioning_qwen3": JEDI_WIDGET_CAPTIONING_QWEN3,
    "llava_one_vision": LLAVA_ONE_VISION,
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