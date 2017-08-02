
# running python -m mypy type_hinting_annotation.py would show x expects an str not an int
# mypy is only available fprm 3.2
x = 10 # type: str

#duck function: function that works for different types
def func(x,y):
    ''' works fo int or str ...'''
    return x+ y


# pyflakes check code for anomalies like variable assigned but never used

# hypothesis is capable of generating test cases
