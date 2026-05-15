from openai import OpenAI
import sys
import base64

client = OpenAI(
    ##################################################
	# Insert your personal openai api key below
	api_key="... your awesome api key ..." # <- change me
    ##################################################
)

if len(sys.argv) < 2:
    print("Please provide a Base64-encoded prompt as a command-line argument.")
    sys.exit(1)

base64_input = sys.argv[1]
try:
    decoded_bytes = base64.b64decode(base64_input)
    prompt = decoded_bytes.decode('utf-8')
except Exception as e:
    print(f"Error decoding Base64: {e}")
    sys.exit(1)

message_log = [
    {"role": "developer", "content": "You are a very intelligent autoregressive language model that has been fine-tuned with instruction-tuning and RLHF. You carefully provide accurate, factual, thoughtful, nuanced answers, and are brilliant at reasoning. If you think there might not be a correct answer, you say so. You are also an expert LaTeX editor. You only return valid LaTeX. Directly return the LaTeX text without an explanation as a prefix or suffix."}
]

def send_message(message_log):
    return client.responses.create(
        model="gpt-5.4-mini",
        reasoning={"effort": "medium"},
        input=message_log,
        max_output_tokens=3000,
        stream=True,
    )

message_log.append({"role": "user", "content": prompt})
response = send_message(message_log)

for event in response:
    if event.type == "response.output_text.delta":
        print(event.delta, end='', flush=True)
    elif event.type == "response.error":
        print(f"\nError: {event.error}", file=sys.stderr)
        sys.exit(1)
print("\n")
