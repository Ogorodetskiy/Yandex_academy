string_with_tabs = "Python\tis\ta\tgreat\tlanguage."
string_without_tabs = " ".join(string_with_tabs.split())
print(string_without_tabs)