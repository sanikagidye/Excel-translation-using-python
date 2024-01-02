import pandas as pd
from deep_translator import GoogleTranslator
import time
import numpy as np

def translate_text(text):
    if pd.notna(text):
        if isinstance(text, str):
            translation = GoogleTranslator(source='auto', target='en').translate(text)
            print(translation)
            return translation
        else:
            return str(text)
    else:
        return np.nan

def translate_excel(input_file, output_file):
    start_time = time.time()

    df = pd.read_excel(input_file, header=None)


    df_translated = df.map(translate_text)
    df_translated.to_excel(output_file, index=False, header=None, engine='openpyxl')

    elapsed_time = time.time() - start_time
    print(f"Translation and save completed in {elapsed_time:.2f} seconds.")

if __name__ == "__main__":
    translate_excel('Order_Export.xls', 'output_file.xlsx')

