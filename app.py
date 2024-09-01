import streamlit as st
import pandas as pd
import json
from io import BytesIO

def main():
    st.title("JSON to Excel Converter")

    uploaded_file = st.file_uploader("Upload your JSON file", type="json")

    if uploaded_file is not None:
        data = json.load(uploaded_file)

        for bond in data['data']:
            if 'meta' in bond:
                del bond['meta']

        df = pd.json_normalize(data['data'])

        output = BytesIO()

        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='Bond Data')

        output.seek(0)

        st.download_button(
            label="Download Excel file",
            data=output,
            file_name='bonds_data.xlsx',
            mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )

if __name__ == '__main__':
    main()
