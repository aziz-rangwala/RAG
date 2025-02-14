import streamlit as st
from utils import read_pdf, create_vector_store, create_conversation_chain

st.set_page_config(page_title="Chat with PDF", layout="wide")

def initialize_session_state():
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "vector_store" not in st.session_state:
        st.session_state.vector_store = None

def main():
    initialize_session_state()
    
    st.title("📚 Chat with Your PDF")
    
    # Sidebar for PDF upload
    with st.sidebar:
        st.header("Upload Document")
        pdf_file = st.file_uploader("Upload your PDF", type="pdf")
        
        if pdf_file and st.button("Process PDF"):
            with st.spinner("Processing PDF..."):
                # Read PDF and create vector store
                raw_text = read_pdf(pdf_file)
                st.session_state.vector_store = create_vector_store(raw_text)
                st.session_state.conversation = create_conversation_chain(
                    st.session_state.vector_store
                )
                st.success("PDF processed successfully!")

    # Main chat interface
    if st.session_state.conversation is None:
        st.info("Please upload a PDF document to start chatting!")
    else:
        # Display chat messages
        for message in st.session_state.chat_history:
            if message["role"] == "user":
                st.chat_message("user").write(message["content"])
            else:
                st.chat_message("assistant").write(message["content"])
        
        # Chat input
        user_question = st.chat_input("Ask a question about your PDF...")
        if user_question:
            st.chat_message("user").write(user_question)
            
            with st.spinner("Thinking..."):
                response = st.session_state.conversation({
                    "question": user_question
                })
                
                st.session_state.chat_history.append({
                    "role": "user",
                    "content": user_question
                })
                st.session_state.chat_history.append({
                    "role": "assistant",
                    "content": response["answer"]
                })
                
                st.chat_message("assistant").write(response["answer"])

if __name__ == "__main__":
    main() 