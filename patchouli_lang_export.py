import os
import json

if __name__ == "__main__":
    lang = {}

    categories = "./memorizable_gensokyo/en_us/categories"
    for file in os.listdir(categories):
        path = "{}/{}".format(categories, file)
        with open(path, "r", encoding='utf-8') as f:
            o = json.load(f)
            lang["memorizable_gensokyo.categories.{}.name".format(
                file[:-5])] = o["name"]
            lang["memorizable_gensokyo.categories.{}.description".format(
                file[:-5])] = o["description"]

    entries = "./memorizable_gensokyo/en_us/entries"
    for folder in os.listdir(entries):
        folder_path = "{}/{}".format(entries, folder)
        for file in os.listdir(folder_path):
            path = "{}/{}".format(folder_path, file)
            with open(path, "r", encoding='utf-8') as f:
                o = json.load(f)
                lang["memorizable_gensokyo.entries.{}.{}.name".format(
                    folder, file[:-5])] = o["name"]
                pages = o["pages"]
                for i in range(0, len(pages)):
                    page = pages[i]
                    if "name" in page:
                        lang["memorizable_gensokyo.entries.{}.{}.pages.{}.name".format(
                            folder, file[:-5], i)] = page["name"]
                    if "title" in page:
                        lang["memorizable_gensokyo.entries.{}.{}.pages.{}.title".format(
                            folder, file[:-5], i)] = page["title"]
                    if "text" in page:
                        lang["memorizable_gensokyo.entries.{}.{}.pages.{}.text".format(
                            folder, file[:-5], i)] = page["text"]
                    if "url" in page:
                        lang["memorizable_gensokyo.entries.{}.{}.pages.{}.url".format(
                            folder, file[:-5], i)] = page["url"]
                    if "link_text" in page:
                        lang["memorizable_gensokyo.entries.{}.{}.pages.{}.link_text".format(
                            folder, file[:-5], i)] = page["link_text"]

    with open("./patchouli_lang.json", "w", encoding='utf-8') as f:
        json.dump(lang, f, ensure_ascii=False)
