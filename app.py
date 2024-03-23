import streamlit as st
from groq import Groq

st.set_page_config(page_title="Story Book Generator")
st.title("Story Book Generator")
user_message=st.text_input("Title of the book")
groq=Groq(api_key="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")

if st.button('Generate Story'):
	with st.spinner("Generating Story"):
		prompt = f"""Generate a 10-20 pages kids story.Here are some of the info that you have to follow-
        - There will be no abuse word in kids story because kids read that
        - Use nothing else in the topic that is given
        - In story book there should least 5 pages of A4 size
        - Ensure to complete full story
        - Try to generate a very interesting story
        - Try to use heading markdown
		- Ensure that kids learn something from it
        - Try to use character introduction at the start
        Now the topic to generate story is "{user_message}",kids story book
        """
		content=groq.chat.completions.create(
			    messages=[
                        {
                            "role": "user",
                            "content": prompt,
                        }
                    ],
                    model="mixtral-8x7b-32768",
        ).choices[0].message.content
		st.write(content)
	