import argparse
import os
import sys

from openai import OpenAI

read_tool = {
	"type": "function",
	"function": {
		"name": "Read",
		"description": "Read and return contents of the file",
		"parameters": {
			"type": "object",
			"properties": {
				"file_path": {
					"type": "string",
					"description": "The path to the file to read."
				}
			},
			"required": ["file_path"]
		}
	}
}

def main():
    p = argparse.ArgumentParser()
    p.add_argument("-p", required=True)
    args = p.parse_args()

    client = OpenAI()

    chat = client.chat.completions.create(
        model="gpt-5.4-nano",
        messages=[{"role": "user", "content": args.p}]
    )

    if not chat.choices or len(chat.choices) == 0:
        raise RuntimeError("no choices in response")

    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!", file=sys.stderr)

    # TODO: Uncomment the following line to pass the first stage
    print(chat.choices[0].message.content)


if __name__ == "__main__":
    main()