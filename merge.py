import json


def traverse_dict(now_source: dict, now_dict: dict):
    for key in now_dict:
        if isinstance(now_dict[key], dict):
            traverse_dict(now_source[key], now_dict[key])
        elif isinstance(now_dict[key], str):
            if key == 'name:8' or key == 'desc:8':
                now_source[key] = now_dict[key]


if __name__ == '__main__':
    with open('zh-CN/en_us.json', 'r', encoding='utf-8') as f:
        translated = json.load(f)
    with open('DefaultQuests.json', 'r', encoding='utf-8') as f:
        source = json.load(f)

    traverse_dict(source, translated)

    with open('DefaultQuests-zh-CN.json', 'w', encoding='utf-8') as f:
        json.dump(source, f, indent=4, ensure_ascii=False)

