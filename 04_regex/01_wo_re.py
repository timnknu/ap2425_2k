inpstr = '5 hello 1257 world 32'

prev_is_num = False
prev_digits = ''
for ich, ch in enumerate(inpstr):
    if ch.isalnum():
        if not prev_is_num:
            prev_is_num = True
            if len(prev_digits) > 0:
                print(prev_digits)
            prev_digits = ch
        else:
            prev_digits += ch
    if not ch.isalnum() or ich == len(inpstr)-1:
        if len(prev_digits) > 0:
            print(prev_digits)
            prev_digits = ''
        prev_is_num = False


