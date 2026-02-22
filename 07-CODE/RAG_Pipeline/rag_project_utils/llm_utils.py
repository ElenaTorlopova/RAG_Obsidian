'''
author: Patryk Gadziomski
updated: 16.02.2026
'''

from langsmith import traceable

@traceable(run_type="llm", name="KISSKI LLM Call")
def llm_call(system_prompt: str, user_prompt: str, client, ai_model):
    response = client.chat.completions.create(
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        model=ai_model,
        temperature=0,
        max_tokens=2000
    )
    return response.choices[0].message.content
