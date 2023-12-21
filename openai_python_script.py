from openai import OpenAI
import sys

client = OpenAI(
    ##################################################
	# Insert your personal openai api key below
	api_key="... your awesome api key ..." # <- change me
    ##################################################
)

if len(sys.argv) < 2:
    print("Please provide a prompt as a command-line argument.")
    sys.exit(1)

prompt = " ".join(sys.argv[1:])

message_log = [
    {"role": "system", "content": "You are a very intelligent autoregressive language model that has been fine-tuned with instruction-tuning and RLHF. You carefully provide accurate, factual, thoughtful, nuanced answers, and are brilliant at reasoning. If you think there might not be a correct answer, you say so. You are a also an expert latex editor. You only return valid latex. Directly return the latex text without an explaination as  a pefix or suffix."}
]

def send_message(message_log):
    return client.chat.completions.create(
    #model="gpt-3.5-turbo",
    #model="gpt-3.5-turbo-1106",
    #model="gpt-4",
    model="gpt-4-1106-preview",
    messages=message_log,
    max_tokens=3000,
    stop=None,
    temperature=0.7,
    stream=True)

message_log.append({"role": "user", "content": prompt})
response = send_message(message_log)

for chunk in response:
    content = chunk.choices[0].delta.content
    if content is not None:    
        print(content, end='', flush=True)
print("\n")
