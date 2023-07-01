
def float_fixer(sample):
    a = str(sample)

    if 'e' in a:
        negative = False
        if a.startswith("-"):
            negative = True
        a = a.replace("-", '')

        b = a.split("e")
        b[0] = b[0].replace('.', '')
        if b[1].startswith('0'):
            b[1] = b[1].replace('0', '', 1)

        zero_count = int(b[1]) - 1
        value_part = b[0]
        zero_wave = ''

        zero_wave = zero_wave.zfill(zero_count)
        abc = '0.' + zero_wave + value_part

        if negative is True:
            abc = '-' + abc

        return abc

    else:
        return a
