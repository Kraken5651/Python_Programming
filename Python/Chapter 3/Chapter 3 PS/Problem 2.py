letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
            
print(letter.replace("<|Name|>,", "Sevrin").replace("<|Date|>", "5 August 2025"))