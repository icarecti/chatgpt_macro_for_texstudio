from openai import OpenAI
import argparse
import os
import sys

client = OpenAI(
    ##################################################
	# Insert your personal openai api key below
	api_key="... your awesome api key ..." # <- change me
    ##################################################
)

parser = argparse.ArgumentParser()
parser.add_argument(
    "--input-file",
    required=True,
    help="Path to a UTF-8 file containing the prompt.",
)
args = parser.parse_args()

try:
    with open(args.input_file, "r", encoding="utf-8") as input_file:
        prompt = input_file.read()
except Exception as e:
    print(f"Error reading prompt file: {e}", file=sys.stderr)
    sys.exit(1)

try:
    os.remove(args.input_file)
except OSError:
    pass

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
