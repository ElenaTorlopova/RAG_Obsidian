'''
author: Patryk Gadziomski
updated: 16.02.2026
'''

def read_system_prompt(path):
    with open(path, mode='r', encoding='utf-8') as f:
        system_prompt = f.read()
        return system_prompt
