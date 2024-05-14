"""
Stage data nicely
"""
import pandas as pd
import pathlib


def get_data() -> pd.DataFrame:
    """
    Load word data for processing
    """
    
    data_file = pathlib.Path("sgb-words.txt")
    file_p = pathlib.Path(__file__)
    data_path = file_p.parent.joinpath(data_file)
    data_added = []
    with open(data_path, "r") as words:
        for i in words:
            word = i.upper().strip()
            temp = [word]
            temp.extend(list(word))
            data_added.append(temp)

    index_key = "word"
    columns = [index_key]
    columns.extend(list(range(len(data_added[0])-1)))
    df = pd.DataFrame(data_added, columns=columns)
    df.set_index(index_key, inplace=True)
    return df

