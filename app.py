import gradio as gr

chat_history = []

def ask_question(question):
    answer = ask_question_with_chromadb(question)
    chat_history.append((question, answer))
    return answer

def show_history():
    return "\n".join([f"Q: {q}\nA: {a}\n" for q, a in chat_history])

with gr.Blocks() as demo:
    gr.Markdown("# Hotel Booking Query System")
    with gr.Row():
        query_input = gr.Textbox(label="Enter your question")
        submit_btn = gr.Button("Ask")
    answer_output = gr.Textbox(label="Answer")
    history_btn = gr.Button("Show History")
    history_output = gr.Textbox(label="Chat History")
    
    submit_btn.click(ask_question, inputs=query_input, outputs=answer_output)
    history_btn.click(show_history, outputs=history_output)

demo.launch()
