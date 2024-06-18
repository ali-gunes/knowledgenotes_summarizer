import summarizer as s
import streamlit as st

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    st.title('YouTube video summarizer')
    link = st.text_input('Enter the link of the YouTube video you want to summarize:')

    if st.button('Start'):
        if link:
            try:
                progress = st.progress(0)
                status_text = st.empty()

                status_text.text('Loading the transcript...')
                progress.progress(25)

                # Getting both the transcript and language_code
                transcript, language_code = s.get_transcript(link)

                status_text.text(f'Creating summary...')
                progress.progress(75)

                model_name = 'gpt-3.5-turbo'
                summary = s.summarize_with_langchain_and_openai(transcript, language_code, model_name)

                status_text.text('Summary:')
                st.markdown(summary)
                progress.progress(100)
            except Exception as e:
                st.write(str(e))
        else:
            st.write('Please enter a valid YouTube link.')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
