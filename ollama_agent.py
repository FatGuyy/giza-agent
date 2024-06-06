import ollama

def create_message_history(history):
    return [{'role': 'user', 'content': message} if idx % 2 == 0 else {'role': 'assistant', 'content': message} for idx, message in enumerate(history)]

def main():
    # Initial context message to set the behavior of the model
    context_message = {
        'role': 'system',
        'content': (
            "You are a reputation managing agent for a dataDAO. Your job is to keep track of all the users and evaluate their reputation based on the interactions they have in the dao. "
            "Come up with a reputation system by yourself and use it manage the reputation of everyone in the dao"
        )
    }
    
    history = [context_message]
    
    options = dict(num_ctx=4096)
    
    while True:
        prompt = input("What do you want to ask? ")
        user_message = {'role': 'user', 'content': prompt}
        
        history.append(user_message)
        
        stream = ollama.chat(
            model='llama3',
            messages=history,
            stream=True,
            options=options
        )
        
        response_content = ""
        for chunk in stream:
            print(chunk['message']['content'], end='', flush=True)
            response_content += chunk['message']['content']
        
        # Add the model's response to the history
        assistant_message = {'role': 'assistant', 'content': response_content}
        history.append(assistant_message)
        print()

if __name__ == "__main__":
    main()
