import chainlit as cl


@cl.on_chat_start
async def start():
    txt_file = await cl.AskFileMessage(
        content="Please upload a text file to begin!", accept=["text/plain"]
    ).send()
    # Decode the file
    text = txt_file.content.decode("utf-8")

    await cl.Message(
        content=f"`Text file {txt_file.name}` uploaded, it contains {len(text)} characters!"
    ).send()

    py_file = await cl.AskFileMessage(
        content="Please upload a python file to begin!", accept={"text/plain": [".py"]}
    ).send()
    # Decode the file
    text = py_file.content.decode("utf-8")

    await cl.Message(
        content=f"`Python file {py_file.name}` uploaded, it contains {len(text)} characters!"
    ).send()
