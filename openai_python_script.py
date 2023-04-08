import openai
import sys

###################################################
# Insert your personal openai api key below
openai.api_key = "*** your awesome api key ***"  # <- change me
##################################################


if len(sys.argv) < 2:
    print("Please provide a prompt as a command-line argument.")
    sys.exit(1)

promt = sys.argv[1]

message_log = [
    {"role": "system", "content": "You are a expert latex editor. You only return valid latex. Everything you return is directly inserted into a latex document and intepreted as latex code."}
]

def send_message(message_log):
    return openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_log,
        max_tokens=3000,
        stop=None,
        temperature=0.7,
        stream=True,
    )

message_log.append({"role": "user", "content": promt})
response = send_message(message_log)
for chunk in response:
    delta = chunk['choices'][0]['delta']
    if 'content' in delta:
        content = delta['content']    
        print(content, end='', flush=True)

