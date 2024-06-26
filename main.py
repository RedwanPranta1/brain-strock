import streamlit as st
import pandas as pd
import DecisionTree
# Title and Description
st.title("Brain Stroke App")
st.write("This app processes and visualizes your data.")

# Sidebar for User Inputs
st.sidebar.header("User Input Parameters")

def user_input_features():
    input_1 = st.sidebar.text_input("Input 1")
    input_2 = st.sidebar.number_input("Input 2")
    file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
    
    return {'input_1': input_1, 'input_2': input_2,'file': file}

user_inputs = user_input_features()

# Add a button to trigger processing
if st.button('Process and Display'):
    if user_inputs['file'] is not None:
        try:
            # Read the uploaded CSV file
            df = pd.read_csv(user_inputs['file'])
            st.write("Uploaded Data")
            st.write(df)

            # Validate CSV structure
            if 'existing_column' not in df.columns:
                st.error("The CSV file must contain a column named 'existing_column'.")
            else:
                try:
                    # Processing Data
                    processed_result = DecisionTree.process(df, user_inputs['input_1'], user_inputs['input_2'])
                    st.write("Processed Results:")
                    st.write(processed_result)

                    # Visualization
                    st.write("Visualization:")
                    fig, ax = plt.subplots()
                    ax.plot(processed_result['new_column'])  # Replace with your actual data column
                    st.pyplot(fig)
                except Exception as e:
                    st.error(f"An error occurred during processing: {e}")
        except Exception as e:
            st.error(f"Failed to read the uploaded CSV file: {e}")
    else:
        st.write("Please upload a CSV file to proceed.")
