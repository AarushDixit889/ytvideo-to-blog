import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from groq import Groq

st.set_page_config("Youtube Video Summarization")
groq=Groq(api_key="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")
def get_transcript(video_id):
    transcript_list=YouTubeTranscriptApi.get_transcript(video_id=video_id)
    return " ".join([entry['text'] for entry in transcript_list])

st.title("Youtube Video Summarizer")
st.warning("After generating blog read the blog end-to-end.")
video_url=st.text_input("Enter the url of video")

if st.button("Generate Blog"):
    with st.spinner("Generating blog"):
        if video_url=="":
            st.error("Please provide input url.")
        if not video_url=="":
            transcript=get_transcript(video_url.split("?v=")[1])

            content=groq.chat.completions.create(
                messages=[
                    {
                        "role":"user",
                        "content":f""""
                        Generate a blog on this youtube video.Transcript is provided here'{transcript}'.Use markdowns if required.Use code markdown if needed.
                        Use this format in html convert it in markdown-
                        <h1>Title</h1><p>title</p>
                        <h1>Table of content</h1><table>Table of content</table>
                        <h1>Content</h1><p>Content</p>
                        <h1>FAQs</h1><li>FAQS</li>
                        <h1>Conclusion</h1><p>conclusion</p>
                        <h1>Facts</h1><p>FACTS</p>
                        <h1>Timestamps</h1><table>*(timing clickable and goes to video at that particular time) *(Topic name)</table>
                        Timestamps must be clickable and should be in table.Add code markdown if required.Only use available images.Automatically write the name of language in which code is coded in.Generate full blog end to end that is given in transcript.My persona is a blogger
                        """
                    }
                ],
                model="mixtral-8x7b-32768"
            ).choices[0].message.content
            st.markdown(content,unsafe_allow_html=True)
