def minimum_excluded_value(S):
    ''' S is a well-ordered set '''
    mex = 0
    for element in S:
        if element == mex:
            mex = element + 1
        else:
            break
    return mex
