import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView


def notInRow(arr, row):
    # Set to store characters seen so far.
    st = set()

    for i in range(0, 9):

        # If already encountered before,
        # return false
        if arr[row][i] in st:
            return False

        # If it is not an empty cell, insert value
        # at the current cell in the set
        if arr[row][i] != '.':
            st.add(arr[row][i])

    return True


# Checks whether there is any
# duplicate in current column or not.
def notInCol(arr, col):
    st = set()

    for i in range(0, 9):

        # If already encountered before,
        # return false
        if arr[i][col] in st:
            return False

        # If it is not an empty cell, insert
        # value at the current cell in the set
        if arr[i][col] != '.':
            st.add(arr[i][col])

    return True




def notInBox(arr, startRow, startCol):
    st = set()

    for row in range(0, 3):
        for col in range(0, 3):
            curr = arr[row + startRow][col + startCol]

            # If already encountered before,
            # return false
            if curr in st:
                return False

            # If it is not an empty cell,
            # insert value at current cell in set
            if curr != '.':
                st.add(curr)

    return True


# Checks whether current row and current
# column and current 3x3 box is valid or not
def isValid(arr, row, col):
    return (notInRow(arr, row) and notInCol(arr, col) and
            notInBox(arr, row - row % 3, col - col % 3))




def isValidConfig(arr, n):
    for i in range(0, n):
        for j in range(0, n):

            # If current row or current column or
            # current 3x3 box is not valid, return false
            if not isValid(arr, i, j):
                return False

    return True







Window.softinput_mode = "below_target"
Window.keyboard_anim_args = {'d': 0.2, 't': 'in_out_expo'}

class invalid_popup(FloatLayout):
    popup_close = ObjectProperty(None)


def show_popup():
    show = invalid_popup()
    popupWindow = Popup(title='',content=show, size_hint = (1,0.3))
    popupWindow.open()
    show.popup_close.bind(on_press=popupWindow.dismiss)




x = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [
             0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0], [
             0, 0, 0, 0, 0, 0, 0, 0, 0]]

def find_empty(x):
    for i in range(0,9):
        for j in range(0,9):
            if x[i][j]==0:
                return (i,j)
    return None

def board_valid(x,num, pos):
    # check row
    for i in range(0,9):
        if x[pos[0]][i]==num and pos[1] !=i:
            return False

    # check column
    for j in range(0,9):
        if x[j][pos[1]]==num and pos[0]!=j:
            return False

    # check box
    box_x = pos[1]//3
    box_y = pos[0]//3
    for i in range(box_y*3 , box_y*3 +3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if x[i][j] == num and (i,j)!= pos:
                return False

    return True

def puzzler(x):
    find = find_empty(x)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if board_valid(x,i,(row,col)):
            x[row][col]=i

            if puzzler(x):
                return True

            x[row][col] = 0


class WindowManager(ScreenManager):
    pass

class Menu(Screen):
    pass

class Htps(Screen):
    pass

class Suggestion(Screen):
    pass

class Solver(Screen):
    a00 = ObjectProperty(None)
    a10 = ObjectProperty(None)
    a20 = ObjectProperty(None)
    a30 = ObjectProperty(None)
    a40 = ObjectProperty(None)
    a50 = ObjectProperty(None)
    a60 = ObjectProperty(None)
    a70 = ObjectProperty(None)
    a80 = ObjectProperty(None)

    a01 = ObjectProperty(None)
    a11 = ObjectProperty(None)
    a21 = ObjectProperty(None)
    a31 = ObjectProperty(None)
    a41 = ObjectProperty(None)
    a51 = ObjectProperty(None)
    a61 = ObjectProperty(None)
    a71 = ObjectProperty(None)
    a81 = ObjectProperty(None)

    a02 = ObjectProperty(None)
    a12 = ObjectProperty(None)
    a22 = ObjectProperty(None)
    a32 = ObjectProperty(None)
    a42 = ObjectProperty(None)
    a52 = ObjectProperty(None)
    a62 = ObjectProperty(None)
    a72 = ObjectProperty(None)
    a82 = ObjectProperty(None)

    a03 = ObjectProperty(None)
    a13 = ObjectProperty(None)
    a23 = ObjectProperty(None)
    a33 = ObjectProperty(None)
    a43 = ObjectProperty(None)
    a53 = ObjectProperty(None)
    a63 = ObjectProperty(None)
    a73 = ObjectProperty(None)
    a83 = ObjectProperty(None)

    a04 = ObjectProperty(None)
    a14 = ObjectProperty(None)
    a24 = ObjectProperty(None)
    a34 = ObjectProperty(None)
    a44 = ObjectProperty(None)
    a54 = ObjectProperty(None)
    a64 = ObjectProperty(None)
    a74 = ObjectProperty(None)
    a84 = ObjectProperty(None)

    a05 = ObjectProperty(None)
    a15 = ObjectProperty(None)
    a25 = ObjectProperty(None)
    a35 = ObjectProperty(None)
    a45 = ObjectProperty(None)
    a55 = ObjectProperty(None)
    a65 = ObjectProperty(None)
    a75 = ObjectProperty(None)
    a85 = ObjectProperty(None)

    a06 = ObjectProperty(None)
    a16 = ObjectProperty(None)
    a26 = ObjectProperty(None)
    a36 = ObjectProperty(None)
    a46 = ObjectProperty(None)
    a56 = ObjectProperty(None)
    a66 = ObjectProperty(None)
    a76 = ObjectProperty(None)
    a86 = ObjectProperty(None)

    a07 = ObjectProperty(None)
    a17 = ObjectProperty(None)
    a27 = ObjectProperty(None)
    a37 = ObjectProperty(None)
    a47 = ObjectProperty(None)
    a57 = ObjectProperty(None)
    a67 = ObjectProperty(None)
    a77 = ObjectProperty(None)
    a87 = ObjectProperty(None)

    a08 = ObjectProperty(None)
    a18 = ObjectProperty(None)
    a28 = ObjectProperty(None)
    a38 = ObjectProperty(None)
    a48 = ObjectProperty(None)
    a58 = ObjectProperty(None)
    a68 = ObjectProperty(None)
    a78 = ObjectProperty(None)
    a88 = ObjectProperty(None)



    def solve(self):
        valid = True
        global x
        x[0][0] = self.a00.text
        x[1][0] = self.a10.text
        x[2][0] = self.a20.text
        x[3][0] = self.a30.text
        x[4][0] = self.a40.text
        x[5][0] = self.a50.text
        x[6][0] = self.a60.text
        x[7][0] = self.a70.text
        x[8][0] = self.a80.text

        x[0][1] = self.a01.text
        x[1][1] = self.a11.text
        x[2][1] = self.a21.text
        x[3][1] = self.a31.text
        x[4][1] = self.a41.text
        x[5][1] = self.a51.text
        x[6][1] = self.a61.text
        x[7][1] = self.a71.text
        x[8][1] = self.a81.text

        x[0][2] = self.a02.text
        x[1][2] = self.a12.text
        x[2][2] = self.a22.text
        x[3][2] = self.a32.text
        x[4][2] = self.a42.text
        x[5][2] = self.a52.text
        x[6][2] = self.a62.text
        x[7][2] = self.a72.text
        x[8][2] = self.a82.text

        x[0][3] = self.a03.text
        x[1][3] = self.a13.text
        x[2][3] = self.a23.text
        x[3][3] = self.a33.text
        x[4][3] = self.a43.text
        x[5][3] = self.a53.text
        x[6][3] = self.a63.text
        x[7][3] = self.a73.text
        x[8][3] = self.a83.text

        x[0][4] = self.a04.text
        x[1][4] = self.a14.text
        x[2][4] = self.a24.text
        x[3][4] = self.a34.text
        x[4][4] = self.a44.text
        x[5][4] = self.a54.text
        x[6][4] = self.a64.text
        x[7][4] = self.a74.text
        x[8][4] = self.a84.text

        x[0][5] = self.a05.text
        x[1][5] = self.a15.text
        x[2][5] = self.a25.text
        x[3][5] = self.a35.text
        x[4][5] = self.a45.text
        x[5][5] = self.a55.text
        x[6][5] = self.a65.text
        x[7][5] = self.a75.text
        x[8][5] = self.a85.text

        x[0][6] = self.a06.text
        x[1][6] = self.a16.text
        x[2][6] = self.a26.text
        x[3][6] = self.a36.text
        x[4][6] = self.a46.text
        x[5][6] = self.a56.text
        x[6][6] = self.a66.text
        x[7][6] = self.a76.text
        x[8][6] = self.a86.text

        x[0][7] = self.a07.text
        x[1][7] = self.a17.text
        x[2][7] = self.a27.text
        x[3][7] = self.a37.text
        x[4][7] = self.a47.text
        x[5][7] = self.a57.text
        x[6][7] = self.a67.text
        x[7][7] = self.a77.text
        x[8][7] = self.a87.text

        x[0][8] = self.a08.text
        x[1][8] = self.a18.text
        x[2][8] = self.a28.text
        x[3][8] = self.a38.text
        x[4][8] = self.a48.text
        x[5][8] = self.a58.text
        x[6][8] = self.a68.text
        x[7][8] = self.a78.text
        x[8][8] = self.a88.text

        for i in range(0,9):
            for j in range(0,9):
                if x[i][j] not in ['1','2','3','4','5','6','7','8','9','']:
                    valid = False

        #if isValidConfig(x, 9)==False:
            #valid = False


        if valid==True:
            for i in range(0, 9):
                for j in range(0, 9):
                    if x[i][j] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                        x[i][j] = int(x[i][j])
                    elif x[i][j] == '':
                        x[i][j] = 0


            puzzler(x)

            print('been here!')

            for i in range(0,9):
                for j in range(0,9):
                    x[i][j]= str(x[i][j])

            self.a00.text = x[0][0]
            self.a10.text = x[1][0]
            self.a20.text = x[2][0]
            self.a30.text = x[3][0]
            self.a40.text = x[4][0]
            self.a50.text = x[5][0]
            self.a60.text = x[6][0]
            self.a70.text = x[7][0]
            self.a80.text = x[8][0]

            self.a01.text = x[0][1]
            self.a11.text = x[1][1]
            self.a21.text = x[2][1]
            self.a31.text = x[3][1]
            self.a41.text = x[4][1]
            self.a51.text = x[5][1]
            self.a61.text = x[6][1]
            self.a71.text = x[7][1]
            self.a81.text = x[8][1]

            self.a02.text = x[0][2]
            self.a12.text = x[1][2]
            self.a22.text = x[2][2]
            self.a32.text = x[3][2]
            self.a42.text = x[4][2]
            self.a52.text = x[5][2]
            self.a62.text = x[6][2]
            self.a72.text = x[7][2]
            self.a82.text = x[8][2]

            self.a03.text = x[0][3]
            self.a13.text = x[1][3]
            self.a23.text = x[2][3]
            self.a33.text = x[3][3]
            self.a43.text = x[4][3]
            self.a53.text = x[5][3]
            self.a63.text = x[6][3]
            self.a73.text = x[7][3]
            self.a83.text = x[8][3]

            self.a04.text = x[0][4]
            self.a14.text = x[1][4]
            self.a24.text = x[2][4]
            self.a34.text = x[3][4]
            self.a44.text = x[4][4]
            self.a54.text = x[5][4]
            self.a64.text = x[6][4]
            self.a74.text = x[7][4]
            self.a84.text = x[8][4]

            self.a05.text = x[0][5]
            self.a15.text = x[1][5]
            self.a25.text = x[2][5]
            self.a35.text = x[3][5]
            self.a45.text = x[4][5]
            self.a55.text = x[5][5]
            self.a65.text = x[6][5]
            self.a75.text = x[7][5]
            self.a85.text = x[8][5]

            self.a06.text = x[0][6]
            self.a16.text = x[1][6]
            self.a26.text = x[2][6]
            self.a36.text = x[3][6]
            self.a46.text = x[4][6]
            self.a56.text = x[5][6]
            self.a66.text = x[6][6]
            self.a76.text = x[7][6]
            self.a86.text = x[8][6]

            self.a07.text = x[0][7]
            self.a17.text = x[1][7]
            self.a27.text = x[2][7]
            self.a37.text = x[3][7]
            self.a47.text = x[4][7]
            self.a57.text = x[5][7]
            self.a67.text = x[6][7]
            self.a77.text = x[7][7]
            self.a87.text = x[8][7]

            self.a08.text = x[0][8]
            self.a18.text = x[1][8]
            self.a28.text = (x[2][8])
            self.a38.text = (x[3][8])
            self.a48.text = (x[4][8])
            self.a58.text = (x[5][8])
            self.a68.text = (x[6][8])
            self.a78.text = (x[7][8])
            self.a88.text = (x[8][8])


        else:
            show_popup()

    def reset(self):
        global s_a_count
        s_a_count = 0
        self.a00.text = ''
        self.a10.text = ''
        self.a20.text = ''
        self.a30.text = ''
        self.a40.text = ''
        self.a50.text = ''
        self.a60.text = ''
        self.a70.text = ''
        self.a80.text = ''

        self.a01.text = ''
        self.a11.text = ''
        self.a21.text = ''
        self.a31.text = ''
        self.a41.text = ''
        self.a51.text = ''
        self.a61.text = ''
        self.a71.text = ''
        self.a81.text = ''

        self.a02.text = ''
        self.a12.text = ''
        self.a22.text = ''
        self.a32.text = ''
        self.a42.text = ''
        self.a52.text = ''
        self.a62.text = ''
        self.a72.text = ''
        self.a82.text = ''

        self.a03.text = ''
        self.a13.text = ''
        self.a23.text = ''
        self.a33.text = ''
        self.a43.text = ''
        self.a53.text = ''
        self.a63.text = ''
        self.a73.text = ''
        self.a83.text = ''

        self.a04.text = ''
        self.a14.text = ''
        self.a24.text = ''
        self.a34.text = ''
        self.a44.text = ''
        self.a54.text = ''
        self.a64.text = ''
        self.a74.text = ''
        self.a84.text = ''

        self.a05.text = ''
        self.a15.text = ''
        self.a25.text = ''
        self.a35.text = ''
        self.a45.text = ''
        self.a55.text = ''
        self.a65.text = ''
        self.a75.text = ''
        self.a85.text = ''

        self.a06.text = ''
        self.a16.text = ''
        self.a26.text = ''
        self.a36.text = ''
        self.a46.text = ''
        self.a56.text = ''
        self.a66.text = ''
        self.a76.text = ''
        self.a86.text = ''

        self.a07.text = ''
        self.a17.text = ''
        self.a27.text = ''
        self.a37.text = ''
        self.a47.text = ''
        self.a57.text = ''
        self.a67.text = ''
        self.a77.text = ''
        self.a87.text = ''

        self.a08.text = ''
        self.a18.text = ''
        self.a28.text = ''
        self.a38.text = ''
        self.a48.text = ''
        self.a58.text = ''
        self.a68.text = ''
        self.a78.text = ''
        self.a88.text = ''


kv = Builder.load_file('solver.kv')

class SudokuSolver(App):
    def build(self):
        self.icon = 'icon.PNG'
        return kv

if __name__ =="__main__":
    SudokuSolver().run()
