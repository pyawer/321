from PyQt5.QtCore import Qt
from random import shuffle
from random import randint
from PyQt5.QtWidgets import QApplication,QWidget,QGroupBox, QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton,QButtonGroup
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memorry Card')
qwr = QLabel('123')
button = QPushButton('Ответить')
RadioGroupBox = QGroupBox('Варианты ответов')
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Смурфы')
rbtn_3 = QRadioButton('Чулымцы')    
rbtn_4 = QRadioButton('Алеуты')
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
answers = [rbtn_1,rbtn_2,rbtn_3,rbtn_4]
class Question():
    def __init__(
        self,question,right_answer,wrong1,wrong2,wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
def show_result():
    RadioGroupBox.hide()
    RadioGroupBox_2.show()
    button.setText('Следующий вопрос')
def show_question():
    RadioGroupBox_2.hide() 
    RadioGroupBox.show()
    button.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
def click_ok():
    if 'Ответить'== button.text():
        check_answer()
    elif 'Следующий вопрос' == button.text():
        next_question()
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    qwr.setText(q.question)
    qr2.setText(q.right_answer)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correсt('Правильно')
        main_win.score += 1
    elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
        show_correсt('Неверно')
    ewq = main_win.score / main_win.total * 100
    print('Статистика')
    print('Всего вопросов:',main_win.total)
    print('Правильных ответов:',main_win.score)
    print('Рейтинг:',ewq)
def show_correсt(res):
    qr.setText(res)
    show_result()
def next_question():
    cur_question = randint(0, len(question_list) - 1)
    qe = question_list[cur_question]
    ask(qe)
    main_win.total += 1
RadioGroupBox_2 = QGroupBox('Результат теста')
layout_gr = QVBoxLayout()
qr = QLabel('прав ты или нет?')
qr2 = QLabel('ответ будет тут!')
layout_gr.addWidget(qr,alignment = Qt.AlignLeft)
layout_gr.addWidget(qr2,alignment = Qt.AlignHCenter)
RadioGroupBox_2.setLayout(layout_gr)

main_win.score = 0
main_win.total = 0 

question_list = []
question_list.append(Question('Государственный язык португалии','Португальский','Английский','Иcпанский','Французкий'))
question_list.append(Question('1234','1','2','3','4'))
question_list.append(Question('абвг','а','б','в','г'))

layout_main = QVBoxLayout()
layout1 = QHBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()
layout1.addWidget(qwr, alignment = Qt.AlignHCenter)
layout2.addWidget(RadioGroupBox, alignment = Qt.AlignHCenter)
layout3.addWidget(button, alignment = Qt.AlignHCenter)
layout2.addWidget(RadioGroupBox_2, alignment = Qt.AlignHCenter)
RadioGroupBox_2.hide()
layout_main.addLayout(layout1)
layout_main.addLayout(layout2)
layout_main.addLayout(layout3)
main_win.setLayout(layout_main)
button.clicked.connect(click_ok)
next_question()
main_win.show()
app.exec_()