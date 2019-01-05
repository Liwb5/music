# coding: utf-8

# 这个文件是用来转调的(inflexion)
from collections import OrderedDict
from pprint import pprint
import argparse

class Inflexion():
    def __init__(self):
        self.C = {11:'(1)', 12:'(2)', 13:'(3)', 14:'(4)', 15:'(5)', 16:'(6)', 17:'(7)',  # low C
                21:'1', 22: '2', 23:'3', 24:'4', 25:'5', 26:'6', 27:'7',                # normal C
                31:'[1]', 32:'[2]', 33:'[3]', 34:'[4]', 35:'[5]', 36:'[6]', 37:'[7]'}   # high  C

        self.D = {11:'(2)', 12:'(3)', 13:'(#4)', 14:'(5)', 15:'(6)', 16:'(7)', 17:'#1',  
                21:'2', 22: '3', 23:'#4', 24:'5', 25:'6', 26:'7', 27:'[#1]',            
                31:'[2]', 32:'[3]', 33:'[#4]', 34:'[5]', 35:'[6]', 36:'[7]', 37:'[[#1]]'}

        # bE/#D
        self.D_ = {11:'(#2)', 12:'(#3/4)', 13:'(5)', 14:'(#5)', 15:'(#6)', 16:'(#7)/1', 17:'2',  
                21:'#2', 22: '#3/4', 23:'5', 24:'#5', 25:'#6', 26:'#7/[1]', 27:'[2]',            
                31:'[#2]', 32:'[#3/4]', 33:'[5]', 34:'[#5]', 35:'[#6]', 36:'[#7]/[[1]]', 37:'[[2]]'}

        self.E = {11:'(3)', 12:'(#4)', 13:'(#5)', 14:'(6)', 15:'(7)', 16:'#1', 17:'#2',  
                21:'3', 22: '#4', 23:'#5', 24:'6', 25:'7', 26:'[#1]', 27:'[#2]',            
                31:'[3]', 32:'[#4]', 33:'[#5]', 34:'[6]', 35:'[7]', 36:'[[#1]]', 37:'[[#2]]'}

        self.F = {11:'(4)', 12:'(5)', 13:'(6)', 14:'(#6)', 15:'1', 16:'2', 17:'3',  
                21:'4', 22: '5', 23:'6', 24:'#6', 25:'[1]', 26:'[2]', 27:'[3]',            
                31:'[4]', 32:'[5]', 33:'[6]', 34:'[#6]', 35:'[[1]]', 36:'[[2]]', 37:'[[3]]'}

        # bG/#F
        self.F_ = {11:'(#4)', 12:'(#5)', 13:'(#6)', 14:'(7)', 15:'#1', 16:'#2', 17:'#3/4',  
                21:'#4', 22: '#5', 23:'#6', 24:'7', 25:'[#1]', 26:'[#2]', 27:'[#3/4]',            
                31:'[#4]', 32:'[#5]', 33:'[#6]', 34:'[7]', 35:'[[#1]]', 36:'[[#2]]', 37:'[[#3]]'}

        self.G = {11:'((5))', 12:'((6))', 13:'((7))', 14:'(1)', 15:'(2)', 16:'(3)', 17:'(#4)', 
                21:'(5)', 22:'(6)', 23:'(7)', 24:'1', 25:'2', 26:'3', 27:'#4', 
                31:'5', 32:'6', 33:'7', 34:'[1]', 35:'[2]', 36:'[3]', 37:'[#4]' }

        # bA/#G
        self.G_ = {11:'((#5))', 12:'((#6))', 13:'((#7))/(1)', 14:'(#1)', 15:'(#2)', 16:'(#3/4)', 17:'(5)', 
                21:'(#5)', 22:'(#6)', 23:'(#7)/1', 24:'#1', 25:'#2', 26:'#3/4', 27:'5', 
                31:'#5', 32:'#6', 33:'#7/[1]', 34:'[#1]', 35:'[#2]', 36:'[#3/4]', 37:'[5]' }

        self.A = {11:'((6))', 12:'((7))', 13:'(#1)', 14:'(2)', 15:'(3)', 16:'(#4)', 17:'(#5)', 
                21:'(6)', 22:'(7)', 23:'#1', 24:'2', 25:'3', 26:'#4', 27:'#5', 
                31:'6', 32:'7', 33:'[#1]', 34:'[2]', 35:'[3]', 36:'[#4]', 37:'[#5]' }

        # bB/#A
        self.A_ = {11:'((#6))', 12:'((#7))/(1)', 13:'(2)', 14:'(#2)', 15:'(#3/4)', 16:'(5)', 17:'(6)', 
                21:'(#6)', 22:'(#7)/1', 23:'2', 24:'#2', 25:'#3/4', 26:'5', 27:'6', 
                31:'#6', 32:'#7/[1]', 33:'[2]', 34:'[#2]', 35:'[#3/4]', 36:'[5]', 37:'[6]' }

        self.B = {11:'((7))', 12:'(#1)', 13:'(#2)', 14:'(3)', 15:'(#4)', 16:'(#5)', 17:'(#6)', 
                21:'(7)', 22:'#1', 23:'#2', 24:'3', 25:'#4', 26:'#5', 27:'#6', 
                31:'7', 32:'[#1]', 33:'[#2]', 34:'[3]', 35:'[#4]', 36:'[#5]', 37:'[#6]' }

    def change8du(self, song, X, direction=None):
        """
        change one octave(8 du). 

        Args:
            song(list): a list of string in which the string can be splited by space
            X(str): the tonality of the song.
            direction(str): reduce by one octave (8 du) if direction == 'down', 
                            Increase by one octave (8 du) if direction == 'up'
        """
        if direction is None:
            return song

        if direction != 'up' and direction != 'down':
            print('direction is not right, please check this parameter')
            exit(1)

        X = getattr(self, X)
        X_ = {v:k for k, v in X.items()}
        song_ = []
        for string in song:
            string = string.split()
            if direction == 'down':
                line = [X[X_[ch]-10] for ch in string]
            elif direction == 'up':
                line = [X[X_[ch]+10] for ch in string]

            song_.append(' '.join(line))

        return song_

    def X2C(self, X, C= 'C'):
        """
        Create an OrderedDict within which the key is C while the value is X 
        so that we can turn the tonality(调性) of X to C.

        Args:
            X(str): 调性. 'C', 'C_', 'D', 'D_'
            C(str): 调性. 'C', 'C_', 'D', 'D_'
        """
        X2C = OrderedDict()
        X = getattr(self, X)
        C = getattr(self, C)
        X_ = OrderedDict(sorted(X.items()))
        C_ = OrderedDict(sorted(C.items()))
        for x, c in zip(X_.items(), C_.items()):
            X2C[c[1]] = x[1] 
        return X2C

    def _inflex(self, string, X2C):
        """
        Args:
            string(str): the string that you want to inflex. e.g: '1 2 (2) [2]'
        """
        string = string.split()
        # print (string)
        res = []
        for ch in string:
            res.append(X2C[ch])
        return ' '.join(res)
        
    def inflex_song(self, song, X, C):
        """
        Inflex a song from the tonality of X to tonality of C.

        Args:
            song(list): a list of string in which the string can be splited by space
            for example: ['1 2 3 4', '(1) 2 [2] 4']
        """
        X2C = self.X2C(X, C)
        song_X = []
        for line in song:
            if line == '':
                song_X.append('')
            else:
                res = self._inflex(line, X2C)
                song_X.append(res)
        return song_X

def readSongFromFile(file):
    song = []
    with open(file, 'r') as f:
        # X, C = f.readline().split() # 把X调转成C调，这样我可以演奏
        for line in f:
            song.append(line.strip())

    return song

def saveSongToFile(song, file):
    with open(file, 'w') as f:
        for item in song:
            f.write(item+'\n')


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', default=None, type=str,
                           help='the path of the file of the song in tonality of X (default: None)')
    parser.add_argument('-s', '--save', default=None, type=str,
                           help='the path to save the song in tonality of C (default: None)')
    parser.add_argument('-x', '--X', default=None, type=str,
                           help='the tonality of the song before inflextion (default: None)')
    parser.add_argument('-c', '--C', default='C', type=str,
                           help='the tonality of the song after inflextion (default: C)')
    parser.add_argument('-d', '--direction', default=None, type=str,
                           help='to change one octave(8 du), the value of direction should be either up or down  (default: None)')
    args = parser.parse_args()

    song = readSongFromFile(args.file)
    tf  = Inflexion()
    song = tf.change8du(song, args.C, direction=args.direction)
    song_X = tf.inflex_song(song, args.X, args.C)
    saveSongToFile(song_X, args.save)
    
    # huimengyouxian = '6 [1] [2] [3] [3] [5] [3] [1] [2] 6 [1] [3] [2] [1] 6 5 \
    #     6 [1] [2] [3] [5] [6] [5] [3] [1] [2] 6 [1] [3] [2] [1] 6'
    # s = input()
    # hongyan = '3 1 (6) (5) 5 6 [1] 6 6 5 3 1 2 5 3 2 2 2'
    # tiankongzhicheng = '6 7 [1] 7 [1] [3] 7 3 3 6 5 6 [1] 5 '
    # res = inflexion.inflex(C, D, tiankongzhicheng)

