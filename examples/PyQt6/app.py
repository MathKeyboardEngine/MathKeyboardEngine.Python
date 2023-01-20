from functools import partial
from typing import Callable, List, Optional, Union

from KatexView import KatexView
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QComboBox, QGridLayout, QMainWindow, QPushButton, QTextEdit, QWidget

from mathkeyboardengine import *

app = QApplication([])


class ExampleWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('MathKeyboardEngine with Katex in a QWebEngineView - unstyled example')

        self.k = KeyboardMemory()
        self.c = LatexConfiguration()

        self.selection_mode_keys: List[QPushButton] = []
        self.gridLayout = QGridLayout()
        widget = QWidget()
        widget.setLayout(self.gridLayout)
        self.setCentralWidget(widget)

        initial_latex = get_edit_mode_latex(self.k, self.c)
        self.output_KatexView = KatexView(latex=initial_latex)
        self.output_view_mode_latex = QTextEdit()
        self.output_view_mode_latex.setText(initial_latex)
        self.output_view_mode_latex.setFixedHeight(30)
        self.output_view_mode_latex.setReadOnly(True)
        self.gridLayout.addWidget(self.output_KatexView, 0, 0, 1, 14)
        self.gridLayout.addWidget(self.output_view_mode_latex, 1, 0, 1, 11)

        selection_mode_toggle_key = QPushButton()
        selection_mode_toggle_key.setStyleSheet('background-color: #add8e6')
        selection_mode_toggle_key.clicked.connect(self.toggle_selection_mode)
        self.gridLayout.addWidget(selection_mode_toggle_key, 2, 0)

        self.multiplication_sign_setting = QPushButton(text=r'\times')
        self.multiplication_sign_setting.clicked.connect(self.multiplication_sign_setting_clicked)
        self.gridLayout.addWidget(self.multiplication_sign_setting, 1, 13)

        self.register_key('flame', 2, 2, delete_current, delete_selection)
        self.register_key('uparrow', 2, 1, move_up)
        self.register_key('leftarrow', 3, 0, move_left, select_left, should_leave_selection_mode=False)
        self.register_key('downarrow', 3, 1, move_down)
        self.register_key('rightarrow', 3, 2, move_right, select_right, should_leave_selection_mode=False)

        for i in range(0, 10):
            self.register_node_key(row=2, col=3 + i, img_name=str(i), node_getter=partial(DigitNode, str(i)))

        self.decimal_separator_setting = QPushButton(text='decimal point')
        self.decimal_separator_setting.clicked.connect(self.decimal_separator_setting_clicked)
        self.gridLayout.addWidget(self.decimal_separator_setting, 1, 11, 1, 2)

        self.decimal_separator_key = QPushButton(text='.')
        self.decimal_separator_key.setStyleSheet('font-size: 15px')
        self.decimal_separator_key.clicked.connect(lambda: self.node_key_clicked(lambda: DecimalSeparatorNode(lambda: '.' if self.decimal_separator_setting.text() == 'decimal point' else '{,}')))
        self.gridLayout.addWidget(self.decimal_separator_key, 2, 13)

        letters = ['a', 'b', 'x', 'y', 'z']
        for i in range(0, len(letters)):
            self.register_node_key(row=3, col=i + 3, img_name=letters[i], node_getter=partial(StandardLeafNode, letters[i]))

        greek_letters = ['alpha', 'beta', 'gamma', 'lambda', 'mu', 'pi']
        for i in range(0, len(greek_letters)):
            self.register_node_key(row=3, col=i + 8, img_name=greek_letters[i], node_getter=partial(StandardLeafNode, '\\' + greek_letters[i]))

        self.register_node_key(row=4, col=0, img_name='binom', node_getter=lambda: DescendingBranchingNode(r'\binom{', '}{', '}'), onclick_selection_mode_func_for_keyboardmemory_and_node=insert_with_encapsulate_selection)
        self.register_node_key(row=4, col=1, img_name='frac', node_getter=lambda: DescendingBranchingNode(r'\frac{', '}{', '}'), onclick_selection_mode_func_for_keyboardmemory_and_node=insert_with_encapsulate_selection)
        self.register_node_key(row=4, col=2, img_name='power', node_getter=lambda: AscendingBranchingNode('', '^{', '}'), onclick_func_for_keyboardmemory_and_node=insert_with_encapsulate_current, onclick_selection_mode_func_for_keyboardmemory_and_node=insert_with_encapsulate_selection_and_previous)
        self.register_node_key(row=4, col=3, img_name='subscript', node_getter=lambda: DescendingBranchingNode('', '_{', '}'), onclick_func_for_keyboardmemory_and_node=insert_with_encapsulate_current, onclick_selection_mode_func_for_keyboardmemory_and_node=insert_with_encapsulate_selection_and_previous)
        self.register_node_key(row=4, col=4, img_name='sqrt', node_getter=lambda: StandardBranchingNode(r'\sqrt{', '}'), onclick_selection_mode_func_for_keyboardmemory_and_node=insert_with_encapsulate_selection)
        self.register_node_key(row=4, col=5, img_name='nthroot', node_getter=lambda: StandardBranchingNode(r'\sqrt[', ']{', '}'))

        self.register_node_key(row=4, col=7, img_name='pm', node_getter=lambda: StandardLeafNode(r'\pm'))
        self.register_node_key(row=4, col=8, img_name='plus', node_getter=lambda: StandardLeafNode('+'))
        self.register_node_key(row=4, col=9, img_name='minus', node_getter=lambda: StandardLeafNode('-'))
        self.register_node_key(row=4, col=10, img_name='times', node_getter=lambda: StandardLeafNode(lambda: r'\cdot' if 'dot' in self.multiplication_sign_setting.text() else r'\times'))
        self.register_node_key(row=4, col=11, img_name='ratio', node_getter=lambda: StandardLeafNode(':'))
        self.register_node_key(row=4, col=12, img_name='div', node_getter=lambda: StandardLeafNode(r'\div'))
        self.register_node_key(row=4, col=13, img_name='faculty', node_getter=lambda: StandardLeafNode('!'))

        self.register_node_key(row=5, col=0, img_name='roundbrackets', node_getter=lambda: RoundBracketsNode(), onclick_selection_mode_func_for_keyboardmemory_and_node=insert_with_encapsulate_selection)
        self.register_node_key(row=5, col=1, img_name='squarebrackets', node_getter=lambda: StandardBranchingNode(r'\left[', r'\right]'))
        self.register_node_key(row=5, col=2, img_name='curlybraces', node_getter=lambda: StandardBranchingNode(r'\left\{', r'\right\}'))
        self.register_node_key(row=5, col=3, img_name='pipes', node_getter=lambda: StandardBranchingNode(r'\left|', r'\right|'))
        self.register_node_key(row=5, col=4, img_name='doublepipes', node_getter=lambda: StandardBranchingNode(r'\left\|', r'\right\|'))

        self.matrix_height = QComboBox()
        self.matrix_height.addItems(['1', '2', '3', '4', '5'])
        self.matrix_height.setCurrentIndex(1)
        self.matrix_height.setStyleSheet('background-color: #FFF')

        self.matrix_width = QComboBox()
        self.matrix_width.addItems(['1', '2', '3', '4', '5'])
        self.matrix_width.setCurrentIndex(1)
        self.matrix_width.setStyleSheet('background-color: #FFF')

        self.register_node_key(row=4, col=6, img_name='pmatrix', node_getter=lambda: MatrixNode('pmatrix', self.matrix_width.currentIndex() + 1, self.matrix_height.currentIndex() + 1), hex_color='#FFF')
        self.gridLayout.addWidget(self.matrix_width, 5, 5)
        self.gridLayout.addWidget(self.matrix_height, 5, 6)

        self.register_node_key(row=5, col=7, img_name='approx', node_getter=lambda: StandardLeafNode(r'\approx'))
        self.register_node_key(row=5, col=8, img_name='equal', node_getter=lambda: StandardLeafNode('='))
        self.register_node_key(row=5, col=9, img_name='neq', node_getter=lambda: StandardLeafNode(r'\neq'))
        self.register_node_key(row=5, col=10, img_name='leq', node_getter=lambda: StandardLeafNode(r'\leq'))
        self.register_node_key(row=5, col=11, img_name='geq', node_getter=lambda: StandardLeafNode(r'\geq'))
        self.register_node_key(row=5, col=12, img_name='less', node_getter=lambda: StandardLeafNode('<'))
        self.register_node_key(row=5, col=13, img_name='greater', node_getter=lambda: StandardLeafNode('>'))

        self.register_node_key(row=6, col=0, img_name='natural', node_getter=lambda: StandardLeafNode(r'\mathbb{N}'))
        self.register_node_key(row=6, col=1, img_name='integers', node_getter=lambda: StandardLeafNode(r'\mathbb{Z}'))
        self.register_node_key(row=6, col=2, img_name='real', node_getter=lambda: StandardLeafNode(r'\mathbb{R}'))
        self.register_node_key(row=6, col=3, img_name='in', node_getter=lambda: StandardLeafNode(r'\in'))
        self.register_node_key(row=6, col=4, img_name='subset', node_getter=lambda: StandardLeafNode(r'\subset'))
        self.register_node_key(row=6, col=5, img_name='subseteq', node_getter=lambda: StandardLeafNode(r'\subseteq'))
        self.register_node_key(row=6, col=6, img_name='setminus', node_getter=lambda: StandardLeafNode(r'\setminus'))
        self.register_node_key(row=6, col=7, img_name='exists', node_getter=lambda: StandardLeafNode(r'\exists'))
        self.register_node_key(row=6, col=8, img_name='forall', node_getter=lambda: StandardLeafNode(r'\forall'))
        self.register_node_key(row=6, col=9, img_name='neg', node_getter=lambda: StandardLeafNode(r'\neg'))
        self.register_node_key(row=6, col=10, img_name='lor', node_getter=lambda: StandardLeafNode(r'\lor'))
        self.register_node_key(row=6, col=11, img_name='land', node_getter=lambda: StandardLeafNode(r'\land'))
        self.register_node_key(row=6, col=12, img_name='leftarrow2', node_getter=lambda: StandardLeafNode(r'\Leftarrow'))
        self.register_node_key(row=6, col=13, img_name='rightarrow2', node_getter=lambda: StandardLeafNode(r'\Rightarrow'))

        self.register_node_key(row=7, col=0, img_name='infty', node_getter=lambda: StandardLeafNode(r'\infty'))
        self.register_node_key(row=7, col=1, img_name='integral', node_getter=lambda: AscendingBranchingNode(r'\int_{', '}^{', '}'))
        self.register_node_key(row=7, col=2, img_name='sum', node_getter=lambda: AscendingBranchingNode(r'\sum_{', '}^{', '}'))
        self.register_node_key(row=7, col=3, img_name='prod', node_getter=lambda: DescendingBranchingNode(r'\prod_{', '}^{', '}'))
        self.register_node_key(row=7, col=4, img_name='lim', node_getter=lambda: DescendingBranchingNode(r'\lim_{', '}'))
        self.register_node_key(row=7, col=5, img_name='rightarrow', node_getter=lambda: StandardLeafNode(r'\rightarrow'))
        self.register_node_key(row=7, col=6, img_name='uparrow', node_getter=lambda: StandardLeafNode(r'\uparrow'))
        self.register_node_key(row=7, col=7, img_name='downarrow', node_getter=lambda: StandardLeafNode(r'\downarrow'))
        self.register_node_key(row=7, col=8, img_name='sin', node_getter=lambda: StandardLeafNode(r'\sin'))
        self.register_node_key(row=7, col=9, img_name='cos', node_getter=lambda: StandardLeafNode(r'\cos'))
        self.register_node_key(row=7, col=10, img_name='tan', node_getter=lambda: StandardLeafNode(r'\tan'))
        self.register_node_key(row=7, col=11, img_name='arcsin', node_getter=lambda: StandardLeafNode(r'\arcsin'))
        self.register_node_key(row=7, col=12, img_name='cosminus1', node_getter=lambda: StandardLeafNode(r'\cos^{-1}'))
        self.register_node_key(row=7, col=13, img_name='taninv', node_getter=lambda: StandardLeafNode(r'\tan^{inv}'))

    def register_node_key(self, row, col, img_name, node_getter, onclick_func_for_keyboardmemory_and_node=insert, onclick_selection_mode_func_for_keyboardmemory_and_node=None, hex_color: Optional[str] = None):
        key = QPushButton()
        if onclick_selection_mode_func_for_keyboardmemory_and_node is not None:
            self.selection_mode_keys.append(key)
        key.setIcon(QIcon('img/' + img_name + '.png'))
        key.setIconSize(QSize(35, 20))
        if hex_color is not None:
            key.setStyleSheet('background-color: ' + hex_color)
        key.clicked.connect(partial(self.node_key_clicked, node_getter, onclick_func_for_keyboardmemory_and_node, onclick_selection_mode_func_for_keyboardmemory_and_node))
        self.gridLayout.addWidget(key, row, col)

    def node_key_clicked(self, node_getter, onclick_func_for_keyboardmemory_and_node=insert, onclick_selection_mode_arrow_func_for_keyboardmemory_and_node=None):
        if in_selection_mode(self.k):
            if onclick_selection_mode_arrow_func_for_keyboardmemory_and_node is not None:
                onclick_selection_mode_arrow_func_for_keyboardmemory_and_node(self.k, node_getter())
            else:
                onclick_func_for_keyboardmemory_and_node(self.k, node_getter())
            self.my_leave_selection_mode(self.k)
        else:
            onclick_func_for_keyboardmemory_and_node(self.k, node_getter())
        self.display_result()

    def register_key(self, key_or_imgname: Union[QPushButton, str], row, col, onclick_func_for_keyboardmemory, onclick_selection_mode_func_for_keyboardmemory=None, should_leave_selection_mode=True):
        key = key if isinstance(key_or_imgname, QPushButton) else QPushButton()
        if isinstance(key_or_imgname, str):
            key.setIcon(QIcon('img/' + key_or_imgname + '.png'))
            key.setIconSize(QSize(35, 20))
        if onclick_selection_mode_func_for_keyboardmemory is not None:
            self.selection_mode_keys.append(key)
        self.gridLayout.addWidget(key, row, col)
        key.clicked.connect(partial(self.key_clicked, onclick_func_for_keyboardmemory, onclick_selection_mode_func_for_keyboardmemory, should_leave_selection_mode))

    def key_clicked(self, onclick_func_for_keyboardmemory: Callable[[KeyboardMemory], None], onclick_selection_mode_func_for_keyboardmemory, should_leave_selection_mode):
        if in_selection_mode(self.k):
            if onclick_selection_mode_func_for_keyboardmemory is not None:
                onclick_selection_mode_func_for_keyboardmemory(self.k)
            if should_leave_selection_mode:
                self.my_leave_selection_mode(self.k)
        else:
            onclick_func_for_keyboardmemory(self.k)
        self.display_result()

    def my_enter_selection_mode(self, k: KeyboardMemory):
        enter_selection_mode(k)
        for key in self.selection_mode_keys:
            key.setStyleSheet('background-color: #add8e6')

    def my_leave_selection_mode(self, k: KeyboardMemory):
        leave_selection_mode(self.k)
        for key in self.selection_mode_keys:
            key.setStyleSheet('')

    def toggle_selection_mode(self):
        if in_selection_mode(self.k):
            self.my_leave_selection_mode(self.k)
        else:
            self.my_enter_selection_mode(self.k)

    def display_result(self):
        if isinstance(self.k.current, Placeholder) and len(self.k.current.nodes) == 0:
            self.c.active_placeholder_shape = r'\blacksquare'
        else:
            self.c.active_placeholder_shape = '|'
        self.output_KatexView.render(r'\displaystyle ' + get_edit_mode_latex(self.k, self.c))
        self.output_view_mode_latex.setText(get_view_mode_latex(self.k, self.c))

    def multiplication_sign_setting_clicked(self):
        self.multiplication_sign_setting.setText(r'\times' if r'\cdot' == self.multiplication_sign_setting.text() else r'\cdot')
        self.display_result()

    def decimal_separator_setting_clicked(self):
        should_become_point = 'decimal comma' == self.decimal_separator_setting.text()
        self.decimal_separator_setting.setText('decimal point' if should_become_point else 'decimal comma')
        self.decimal_separator_key.setText('.' if should_become_point else ',')
        self.display_result()


window = ExampleWindow()
window.show()
app.exec()
