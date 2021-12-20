#!/home/love/miniconda3/envs/rasa/bin/python

import pandas as pd
import numpy as np

def merge_nlu():
    file = open('data/nlu.yml',"a")
    file.write("\n")
    df = pd.read_csv(r"{}".format("utils/intermediate.csv"))
    df = df.replace(np.nan, '', regex=True)
    # file = open('nlu_file_name'+'.yml',"w")
    df=df.drop('Unnamed: 0',axis=1)
    intents = list(df.columns)
    for item in intents:
        file.write("- intent: {intent_name}\n".format(intent_name=item))
        file.write("  examples: |"+'\n')
        for sent in df[item]:
            if sent != '':
                file.write("    - {}\n".format(sent))
    file.close()


    # Domain
    with open("domain.yml", 'r+') as fp:
        # read an store all lines into list
        lines = fp.readlines()
        # move file pointer to the beginning of a file
        fp.seek(0)
        # truncate the file
        fp.truncate()

        # start writing lines except the first line
        # lines[1:] from line 2 to last line
        fp.writelines(lines[:-3])


    # file = open('utils/'+create_files_path+domain_file_name+'.yml',"w")
    domfile = open('domain.yml',"a+")
    print("--------------")

    with open("utils/domain_29oct.yml", 'r+') as fp:
        data_to_write = fp.readlines()
        domfile.writelines(data_to_write)

#     for intent_name in intents:
#         domfile.write("  utter_{}:\n".format(intent_name))
#         domfile.write('  - text:\n')
        
#     domfile.write("""session_config:
# session_expiration_time: 60
# carry_over_slots_to_new_session: true""")

    domfile.close()


    print("Data Merged")


merge_nlu()