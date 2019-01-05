# coding: utf-8

# 这个文件是用来转调的(inflexion)
from collections import OrderedDict
# from pprint import pprint

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

        # self.G2C = OrderedDict([
        #     ('((5))', '(1)'), ('((6))', '(2)'), ('((7))', '(3)'), ('(1)', '(4)'), ('(2)', '(5)'), ('(3)', '(6)'), ('(#4)', '(7)'),
        #     ('(5)', '1'), ('(6)', '2'), ('(7)', '3'), ('1', '4'), ('2', '5'), ('3', '6'), ('#4', '7'),
        #     ('5', '[1]'), ('6', '[2]'), ('7', '[3]'), ('[1]', '[4]'), ('[2]', '[5]'), ('[3]', '[6]'), ('[#4]', '[7]')])


    def up8du(self):
        pass

    def down8du(self):
        pass

    def C2X(self, C, X= 'X'):
        """
        Args:
            C(str): 调性. 'C', 'C_', 'D', 'D_'
            X(str): 调性. 'C', 'C_', 'D', 'D_'
        """
        C2X = OrderedDict()
        C = getattr(self, C)
        X = getattr(self, X)
        C_ = OrderedDict(sorted(C.items()))
        X_ = OrderedDict(sorted(X.items()))
        for c, x in zip(C_.items(), X_.items()):
            C2X[c[1]] = x[1]
        return C2X

    def _inflex(self, string, C2X):
        """
        Args:
            string(str): the string that you want to inflex. e.g: '1 2 (2) [2]'
        """
        string = string.split()
        # print (string)
        res = []
        for ch in string:
            res.append(C2X[ch])
        return ' '.join(res)
        
    def inflex_song(self, song, C, X):
        """
        inflex a song from C to X 

        Args:
            song(list): a list of string in which the string can be splited by space
            for example: ['1 2 3 4', '(1) 2 [2] 4']
        """
        C2X = self.C2X(C, X)
        song_X = []
        for line in song:
            if line == '':
                song_X.append('')
            else:
                res = self._inflex(line, C2X)
                song_X.append(res)
        return song_X

def getSongFromFile(file):
    song = []
    with open(file, 'r') as f:
        X, C = f.readline().split() # 把X调转成C调，这样我可以演奏
        for line in f:
            song.append(line.strip())

    return song, C, X

if __name__=='__main__':
    file = './tiankongzhicheng.txt'
    song, C, X = getSongFromFile(file)
    # print(song)
    # print(C)
    # print(X)
    tf  = Inflexion()
    song_X = tf.inflex_song(song, C, X)
    print (song_X)
    
    # C = 'C'
    # D = 'D'
    # G = 'G'
    # print(inflexion.X2C('G', 'C'))
    # huimengyouxian = '6 [1] [2] [3] [3] [5] [3] [1] [2] 6 [1] [3] [2] [1] 6 5 \
    #     6 [1] [2] [3] [5] [6] [5] [3] [1] [2] 6 [1] [3] [2] [1] 6'
    # s = input()
    # hongyan = '3 1 (6) (5) 5 6 [1] 6 6 5 3 1 2 5 3 2 2 2'
    # tiankongzhicheng = '6 7 [1] 7 [1] [3] 7 3 3 6 5 6 [1] 5 '
    # res = inflexion.inflex(C, D, tiankongzhicheng)
    # print(res)
