import json

def convert_jsonl(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        with open(output_file, 'w', encoding='utf-8') as fout:
            for line in f:
                data = json.loads(line.strip())
                conversations = data['conversation']
                new_conversations = []
                for conv in conversations:
                    for key, value in conv.items():
                        if key == 'assistant':
                            key = 'gpt'
                        else:
                            key = 'human'
                            
                        new_conversations.append({'from': key, 'value': value})
                        
                new_data = {'conversations': new_conversations}
                fout.write(json.dumps(new_data, ensure_ascii=False) + '\n')

# 替换输入文件路径和输出文件路径
input_file = 'input.jsonl'
output_file = 'output.jsonl'

convert_jsonl(input_file, output_file)
