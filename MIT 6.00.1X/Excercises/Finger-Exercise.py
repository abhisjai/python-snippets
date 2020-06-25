# Source: https://courses.edx.org/courses/course-v1:MITx+6.00.1x+2T2020/courseware/530b7f9a82784d0cb57de334828e3050/8a590293a22e46dd9760ec917d122ec1/?activate_block_id=block-v1%3AMITx%2B6.00.1x%2B2T2020%2Btype%40sequential%2Bblock%408a590293a22e46dd9760ec917d122ec1

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.
    returns: int, how many values are in the dictionary.
    '''
    # Your Code Here
    length = 0

    for i in aDict.keys():
        length += len(aDict[i])

    return length

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

print(how_many(animals))