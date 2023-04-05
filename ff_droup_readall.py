import pandas as pd
from tqdm import tqdm
import os
import sys
import toolsets.ff_droup as ff
from toolsets.search import string_search, quick_search_sorted, quick_search_values, num_search
import glob

if __name__ == '__main__':
    mzml_master_folder = sys.argv[1]
    output_folder = sys.argv[2]
    if os.path.exists(output_folder)==False:
        os.mkdir(output_folder)
    os.chdir(mzml_master_folder)
    rt_max = 20 # please change this to appropriate rt_max
    print(rt_max)
    bad_files = []
    features = pd.DataFrame()
    os.chdir(mzml_master_folder)
    for file in glob.glob("*.mzml"):
        print(file)
        # break
        try:

            ms1, ms2 = ff.process_mzml(file, mzml_master_folder, if_mix=False, with_ms1=True, rt_max = rt_max)
            features_temp = ff.feature_finding(ms1, ms2)
            features = pd.concat([features, features_temp], ignore_index = True)
        except:
            bad_files.append(file)
    features.to_csv(os.path.join(output_folder, mzml_master_folder.split('/')[-1]+'_features.csv'), index= False)

