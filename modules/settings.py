import json
import modules.path

from modules.resolutions import get_resolution_string
from os.path import exists


def load_settings():
    settings = {}
    settings['advanced_mode'] = False
    settings['image_number'] = 2
    settings['save_metadata_json'] = False
    settings['save_metadata_png'] = False
    settings['seed_random'] = True
    settings['seed'] = 0
    settings['style'] = 'cinematic-default'
    settings['prompt'] = ''
    settings['negative_prompt'] = ''
    settings['performance'] = 'Speed'
    settings['custom_steps'] = 24
    settings['custom_switch'] = 0.75
    settings['img2img_mode'] = False
    settings['img2img_start_step'] = 0.06
    settings['img2img_denoise'] = 0.94
    settings['resolution'] = get_resolution_string(1152, 896)
    settings['sampler'] = 'dpmpp_2m_sde_gpu'
    settings['scheduler'] = 'karras'
    settings['cfg'] = 7.0
    settings['base_clip_skip'] = -2
    settings['refiner_clip_skip'] = -2
    settings['sharpness'] = 2.0
    settings['base_model'] = modules.path.default_base_model_name
    settings['refiner_model'] = modules.path.default_refiner_model_name
    settings['lora_1_model'] = modules.path.default_lora_name
    settings['lora_1_weight'] = modules.path.default_lora_weight
    settings['lora_2_model'] = 'None'
    settings['lora_2_weight'] = modules.path.default_lora_weight
    settings['lora_3_model'] = 'None'
    settings['lora_3_weight'] = modules.path.default_lora_weight
    settings['lora_4_model'] = 'None'
    settings['lora_4_weight'] = modules.path.default_lora_weight
    settings['lora_5_model'] = 'None'
    settings['lora_5_weight'] = modules.path.default_lora_weight

    if exists('settings.json'):
        with open('settings.json') as settings_file:
            try:
                settings_obj = json.load(settings_file)
                counter = 0;
                for k in settings.keys():
                    if k in settings_obj:
                        settings[k] = settings_obj[k]
            except Exception as e:
                print(e)
            finally:
                settings_file.close()

    return settings


default_settings = load_settings()
