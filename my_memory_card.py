#создай приложение для запоминания информации
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton,QButtonGroup, QHBoxLayout, QVBoxLayout, QRadioButton,QGroupBox, QWidget, QMessageBox
from random import shuffle
app = QApplication([])
window = QWidget()
window.setWindowTitle("Memory Card")
window.resize(800,600)
question = QLabel("Численность населения в мире?")
answers = QGroupBox("Варианты ответов")
check = QGroupBox("Правильный ответ")
result = QLabel("Правильно или нет?")
correct = QLabel("Ответ будет тут")


answer1 = QRadioButton("1")
answer2 = QRadioButton("0")
answer3 = QRadioButton("8млрд")
answer4 = QRadioButton("1000-7")
button = QPushButton("Ответить")

RadioGroup = QButtonGroup()
RadioGroup.addButton(answer1)
RadioGroup.addButton(answer2)
RadioGroup.addButton(answer3)
RadioGroup.addButton(answer4)

answers_main = QHBoxLayout()
col_left = QVBoxLayout()
col_right = QVBoxLayout()

col_left.addWidget(answer1)
col_left.addWidget(answer2)
col_right.addWidget(answer3)
col_right.addWidget(answer4)

result_line = QVBoxLayout()
result_line.addWidget(result)
result_line.addWidget(correct)

check.setLayout(result_line)

answers_main.addLayout(col_left)
answers_main.addLayout(col_right)

answers.setLayout(answers_main)

main_line = QVBoxLayout()
main_line.addWidget(question)
main_line.addWidget(answers)
main_line.addWidget(check)
check.hide()
main_line.addWidget(button)

window.setLayout(main_line)
class Question():
    def __init__(self, new_question, right_answer, wrong1, wrong2, wrong3):
        self.new_question = new_question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

def show_result():
    """показать панель вопросов"""
    answers.hide()
    check.show()
    button.setText("Следующий вопрос")

def show_question():
    """ показать панель вопрос """
    answers.show()
    check.hide()
    button.setText("Ответить")
    RadioGroup.setExclusive(False)
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroup.setExclusive(True)


answers_list = [answer1, answer2, answer3, answer4]    


def ask(q: Question):
    """ функция записывает значения и ответов в соответсвующие виджеты, при этом варианты ответов распределяются случайным образом"""
    shuffle(answers_list)
    answers_list[0].setText(q.right_answer)
    answers_list[1].setText(q.wrong1)
    answers_list[2].setText(q.wrong2)
    answers_list[3].setText(q.wrong3)
    question.setText(q.new_question)
    correct.setText(q.right_answer)
    show_question()

def show_correct(res):
    """показать результат - установим переданный текст в надпись "результат" и покажем нужную панель"""
    result.setText(res)
    show_result()


def check_answer():
    """ если выбран какой-то вариант ответа, то надо проверить и показать панель ответов"""
    if answers_list[0].isChecked():
        show_correct("Правильно!")
        window.score += 1
    else:
        if answers_list[1].isChecked() or answers_list[2].isChecked() or answers_list[3].isChecked():
            show_correct("Неверно!")

def next_question():
    window.cur_question = window.cur_question + 1
    if window.cur_question >= len(questions_list):
        window.cur_question = 0
        message = QMessageBox()
        message.setText(f'Вы ответили правильно на {window.score} вопросов из {window.total}')
        message.exec()
        window.score = 0
        
    q = questions_list[window.cur_question]
    ask(q)


def click_OK():
    '''определяет, надо ли показывать другой вопрос либо проверить ответ'''
    if button.text() == 'Ответить':
        check_answer()
    else:
        next_question()



questions_list = []
questions_list.append(Question('Население Ботсваны', '6 млн', "три с половиной калеки", "15млн", "нет"))
questions_list.append(Question('Что такое осень?', 'это осень','это зима','это что то','нет'))
questions_list.append(Question('Пирожки с чем?', 'с чаем', 'с грибами', 'с мясом','с картошкой'))
questions_list.append(Question('какая птица сидела на плече капитана Флинта?', 'Попугай','Сокол','Пингвин','Дятел'))
questions_list.append(Question('Как назыввется автомобиль с откидным сиденьем вдоль бортов?', 'Пикап','Хэчбек','Купе','Кабриолет'))
questions_list.append(Question('Какой океан Земли занимает наименьшую площадь?','Северный Ледовитый','Индийский','Атлантический', 'Тихий'))
questions_list.append(Question('В какой стране расположен город Антверпен?','Бельгия','Нидерланды','Дания','Германия'))
questions_list.append(Question('В какой стране есть город Аллахабад?','Индия','Пакистан','Бангладеш','Афганистан'))
questions_list.append(Question('Какая наука изучает вышедшие из употребления бумажные деньги?','Бонистика','Геральдика','нумизматика','Фалеристика'))
questions_list.append(Question('Какую заметку принёс почтальон Печкин в Простоквашино?','Про мальчика','Про Матроскина','Про Шарика','Про корову'))



window.cur_question = -1
window.score = 0
window.total = len(questions_list)
button.clicked.connect(click_OK)

next_question()

window.setStyleSheet('font-size: 22px; background-color: red; color: lime;')
button.setStyleSheet('background-color: blue; color: red;')
question.setStyleSheet('color: turquoise')
window.show()
app.exec()






