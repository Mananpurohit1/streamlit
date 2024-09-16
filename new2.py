import streamlit as st

st.title("Skill Assessment Form")

# Initialize session state
if 'proficiency_ratings' not in st.session_state:
    st.session_state.proficiency_ratings = {}
if 'custom_skill_ratings' not in st.session_state:
    st.session_state.custom_skill_ratings = {}
if 'custom_skills' not in st.session_state:
    st.session_state.custom_skills = []

# Personal Information
st.header("Personal Information")
col1, col2 = st.columns(2)
first_name = col1.text_input("First Name")
last_name = col2.text_input("Last Name")

# Experience dropdowns
experience_options = ["Less than 1 year"] + [f"{i} years" for i in range(1, 51)]
overall_experience = st.selectbox("Overall Years of Experience", experience_options)
data_science_experience = st.selectbox("Years of Experience in Data Science", experience_options)

# List of predefined skills
predefined_skills = [
    "Tableau", "Azure ML", "Neural networks with TensorFlow and Keras",
    "Computer Vision", "Natural Language Processing",
    "Cloud Computing with AWS", "Cloud Computing with Azure",
    "Gen AI", "ML Ops", "KNIME", "Rapidminer", "SQL", "Prompt Engineering"
]

st.header("Skills Assessment")

# Function to create rating buttons
def create_rating_buttons(skill, key_prefix):
    cols = st.columns(5)
    for i, col in enumerate(cols, start=1):
        if col.button(str(i), key=f"{key_prefix}_{skill}_{i}"):
            st.session_state.proficiency_ratings[skill] = i

# Display predefined skills in a grid
st.subheader("Predefined Skills")
num_cols = 3
rows = [predefined_skills[i:i+num_cols] for i in range(0, len(predefined_skills), num_cols)]

for row in rows:
    cols = st.columns(num_cols)
    for skill, col in zip(row, cols):
        with col:
            if st.checkbox(skill, key=f"checkbox_{skill}"):
                st.write(f"Rate your proficiency in {skill}:")
                create_rating_buttons(skill, "predefined")

# Custom skills section
st.subheader("Additional Skills")

# Function to add custom skill
def add_custom_skill():
    custom_skill = st.text_input(f"Custom Skill {len(st.session_state.custom_skills) + 1}")
    if custom_skill and custom_skill not in st.session_state.custom_skills:
        st.session_state.custom_skills.append(custom_skill)
        st.write(f"Rate your proficiency in {custom_skill}:")
        create_rating_buttons(custom_skill, "custom")

# Add first custom skill
add_custom_skill()

# Add more custom skills button
if st.button("Add Another Skill"):
    add_custom_skill()

# Submit button
if st.button("Submit"):
    # Validate that all required fields are filled
    if not first_name or not last_name:
        st.error("Please fill in both First Name and Last Name.")
    elif not st.session_state.proficiency_ratings and not st.session_state.custom_skill_ratings:
        st.error("Please select at least one skill and provide a rating.")
    else:
        # Process the form data
        st.success("Form submitted successfully!")
        
        # Combine predefined and custom skills
        all_skills = {**st.session_state.proficiency_ratings, **st.session_state.custom_skill_ratings}
        
        # Create a dictionary with all the form data
        form_data = {
            "First Name": first_name,
            "Last Name": last_name,
            "Overall Experience": overall_experience,
            "Data Science Experience": data_science_experience,
            "Skills and Proficiencies": all_skills
        }
        
        # Display the form data
        st.write("Form ", form_data)
