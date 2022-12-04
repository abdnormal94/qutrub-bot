import pandas as pd
import json
import requests

def sample_responses(input_str):
    input_list = input_str.split()
    verb = input_list[0]
    req = 'https://qutrub.arabeyes.org/api?verb=' + verb

    r = requests.get(req)
    r = r.json()
    df = pd.DataFrame(r["result"])

    df = df[['0', '1', '2', '3', '4', '5', '6',
             '7', '8', '9', '10', '11', '12', "13", "14"]]
    df = df.reindex(['0', '1', '2', '3', '4', '5',
                     '6', '7', '8', '9', '10', '11', '12'])
    df = df.transpose()

    if len(input_list) == 3:
        if input_list[1:] =="في الماضي".split():
            return ((df["0"][1:] + " " + df["1"][1:]).to_string(index=False, header=False))
        if input_list[1:] =="في المضارع".split():
            return ((df["0"][1:] + " " + df["2"][1:]).to_string(index=False, header=False))
        if input_list[1:] =="في الأمر".split():
            return ((df["0"][3:8] + " " + df["6"][3:8]).to_string(index=False, header=False))

    if len(input_list) == 4:
        if input_list[1:] =="في الماضي المعلوم".split():
            return ((df["0"][1:] + " " + df["1"][1:]).to_string(index=False, header=False))
        if input_list[1:] =="في المضارع المعلوم".split():
            return ((df["0"][1:] + " " + df["2"][1:]).to_string(index=False, header=False))
        if input_list[1:] =="في الأمر المؤكد".split():
            return ((df["0"][3:8] + " " + df["6"][3:7]).to_string(index=False, header=False))
        if input_list[1:] =="في المضارع المجزوم".split():
            return ((df["0"][1:] + " " + df["3"][1:]).to_string(index=False, header=False))
        if input_list[1:] == "في المضارع المنصوب".split():
            return ((df["0"][1:] + " " + df["4"][1:]).to_string(index=False, header=False))
        if input_list[1:] == "في الماضي المجهول".split():
            return ((df["0"][1:] + " " + df["8"][1:]).to_string(index=False, header=False))
        if input_list[1:] == "في المضارع المجهول".split():
            return ((df["0"][1:] + " " + df["9"][1:]).to_string(index=False, header=False))

    if len(input_list) == 5:
        if input_list[1:] =="في المضارع المؤكد الثقيل".split():
            return ((df["0"][1:] + " " + df["5"][1:]).to_string(index=False, header=False))
        if input_list[1:] =="في المضارع المجهول المجزوم".split():
            return ((df["0"][1:] + " " + df["10"][1:]).to_string(index=False, header=False))
        if input_list[1:] =="في المضارع المجهول المنصوب".split():
            return (df["0"][1:] + " " + df["11"][1:])
