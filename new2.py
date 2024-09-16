import streamlit as st
import pandas as pd
from io Bytes

st.title("Skill Assessment Form")   # Initialize session state
if 'proficiency_ratings' not in st.session_state:
    st.session_state.proficiency_ratings = {}
if 'custom_skill_ratings' not in st.session_state:
    st.session_state.custom_skill_ratings = {}
if 'custom_skills' not in st.session_state:
    st.session.custom_skills = []

# Personal Information
st.header("Personal Information")
col1, col2 = st(2)
first_name = col1.text_input("First Name")
last_name = col2.text_input("Last Name")

# Experience dropdowns
experience_options = ["Less than 1 year"] + [f"{i} years" for i in range(1, 51)]
overall_experience = st.selectbox("Overall Years Experience", experience_options)
data_science_experience = st.selectbox("Years of Experience in Data Science", experience_options)

# Predefined skills
predefined_skills = [
    "Tableau", "Azure ML", "Neural networks with TensorFlow and Keras",
    "Computer Vision", "Natural Language Processing",
    "Cloud Computing with AWS",Cloud Computing with Azure",
    "Gen AI", "ML Ops", "KNIME", "Rapidminer", "", "Prompt Engineering"
]

st.header("Skills Assessment")

def create_rating_buttons, key_prefix):
    cols = st.columns(5)
    for i, col in enumerate(cols, start=1           if col.button(str(i),=f"{key_prefix}_{skill}_{i}"):
            st.session_state.proficiency_ratings[skill] = i

# Display predefined skills
st.subheaderPredefined Skills")
num_cols = 3
rows = [predefined_skills[i:i+num_cols] for i in range(0,(predefined_skills), num_cols)]

for row in rows:
    cols = st.columns(num_cols)
    for skill, col in zip(row, cols):
with col:
            if st.checkbox(skill, key=f"checkbox_{skill}"):
                st.write(f"Rate your proficiency in {skill}:")
                create_rating_buttons, "predefined")

# Custom skills
st.subheader("Additional")

add_custom_skill():
    custom_skill = st.text_input(f"Custom Skill {len(st.session_state.custom_skills) + 1}")
    if custom_skill and custom_skill not in st.session_state.custom_skills:
        st.session_state.custom_skills.append(custom_skill)
        st.write(f"Rate your proficiency in {custom_skill}:")
        create_rating_buttons(custom_skill, "custom")

add_custom_skill()

if st.button("Add Another Skill"):
    add_custom_skill()

# Submit button
if st.button("Submit"):
    if not first_name or not last_name:
        st.error("Please fill in both First Name and Last Name       elif not st.session_state.proficiency_ratings and not st.session_state.custom_skill_ratings:
       .error("Please select at least one skill and provide a rating.")
    else:
        st.success("Form submitted successfully!")

        # Combine skills
        all_skills = {st.session_state.pro_ratings, **st.session_state.custom_skill_ratings}

        # Form data dictionary
       _data = {
            "First Name": first_name,
            "Last Name": last_name,
            "Overall Experience": overallperience,
"Data Science Experience": data_science_experience,
            "Skills and Proficiencies": all_skills
        }

        st.write("Form data:", form_data)

        # Save to
        df = pd.DataFrame([form_data])
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df.to_excel(writer, index=False, sheet_name='FormData')
            writer.save()
        processed_data = output.getvalue()

        # Download button
        st.download_button="Download Excel",
                           data=processed_data,
                           file_name="form_data.xlsx",
                           mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
