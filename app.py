import streamlit as st
from src.helper import voice_input, llm_model, text_to_speech

def main():
    st.title("Multilingual AI Assistant with Chatbox & Voice Input")

    # Chatbox input
    user_input = st.text_input("Type your message here:")
    
    # Voice input button
    if st.button("🎤 Use Voice Input"):
        with st.spinner("Listening..."):
            user_input = voice_input()
            st.write(f"🎤 Recognized Text: {user_input}")  # Debug log
    
    # Process input if user types or speaks
    if user_input:
        with st.spinner("Processing..."):
            response = llm_model(user_input)
            st.write(f"🤖 AI Response: {response}")  # Display response
            
            # Convert AI response to speech
            text_to_speech(response)

            # Play and download the generated speech
            with open("speech.mp3", "rb") as audio_file:
                audio_bytes = audio_file.read()

            st.audio(audio_bytes)
            st.download_button(label="Download Speech",
                               data=audio_bytes,
                               file_name="speech.mp3",
                               mime="audio/mp3")

if __name__ == '__main__':
    main()
