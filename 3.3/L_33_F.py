text = 'Мама мыла раму!'

print({key: text.lower().count(key) for key in text.lower() if key.isalpha()})
