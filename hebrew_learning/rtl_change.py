initial_text = "‫מִספָּר‬ ‫שֵם‬"

def rtl_text_parser(initial_text):
    list = initial_text.split(" ")
    list.reverse()
    return " ".join(list)

print(rtl_text_parser(initial_text))