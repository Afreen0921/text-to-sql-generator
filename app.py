import json
import streamlit as st

from prompt import PROMPT_TEMPLATE
from model import generate_response

st.set_page_config(
    page_title="Text-to-SQL Generator",
    page_icon="💻",
    layout="centered"
)

st.title("💻 Text-to-SQL Generator")

st.markdown(
    "Convert natural language questions into SQL queries using Generative AI."
)

database_context = st.text_area(
    "Enter Database Context",
    placeholder="Example: Table users(id, name, age, city)",
    height=150
)

question = st.text_input(
    "Enter Question",
    placeholder="Example: Show all users older than 25"
)

if st.button("Generate SQL"):

    if not database_context or not question:
        st.warning("Please enter both schema and question.")

    else:

        final_prompt = PROMPT_TEMPLATE.format(
            database_context=database_context,
            question=question
        )

        result = generate_response(final_prompt)

        if result.startswith("Error"):
            st.error(result)

        else:

            try:
                parsed = json.loads(result)

                st.success("SQL Query Generated Successfully!")

                st.subheader("Generated SQL")
                st.code(parsed["sql_query"], language="sql")

                st.subheader("Explanation")
                st.write(parsed["explanation"])

                st.subheader("Tables Used")
                st.write(parsed["tables_used"])

                st.subheader("Conditions Applied")
                st.write(parsed["conditions_applied"])

            except Exception:
                st.error("Invalid JSON response")
                st.write(result)