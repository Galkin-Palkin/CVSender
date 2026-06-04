MAIN_MENU = "Привет! Я бот для отправки резюме по электронной почте. Просто отправьте мне свое резюме в виде файла, и я отправлю его на указанный адрес."

def DOCUMENT_DOWNLOADED_SUCCESSFULLY(filename: str):
    return f"Документ {filename} успешно загружен!"

LETTER_PATTERNS_BUTTON = "Редактировать шаблоны письма"

TITLE_PATTERNS_BUTTON = "Редактировать шаблоны заголовка"

EMAIL_CREDENTIALS_BUTTON = "Редактировать email"

SEND_CV_BUTTON = "Отправить резюме работодателю"

UNSUPPORTED_FILE_EXTENSION = "Данный формат файлов не поддерживается, загрузите файлы с другим расширением"

LETTERS_MENU = "Выберите шаблон письма или создайте новый"

def CERTAIN_LETTER_MENU(letter: str):
    return f"Текущий шаблон письма:\n{letter}\nВыберите действия:"

TITLES_MENU = "Выберите шаблон заголовка письма или создайте новый"

def CERTAIN_TITLE_MENU(title: str):
    return f"Текущий шаблон заголовка письма:\n{title}\nВыберите действия:"

EMAIL_MENU = "Выберите, какую почту хотите настроить:"

MAIL_RU_BUTTON = "Mail.ru"

GMAIL_COM_BUTTON = "Gmail.com"

EDIT_EMAIL_BUTTON = "Редактировать почту"

EDIT_PASSWORD_BUTTON = "Редактировать пароль"

MAIL_RU_MENU = "Настройка почты Mail.ru"

GMAIL_COM_MENU = "Настройка почты Gmail.com"

EDIT_GMAIL_COM_MESSAGE = "Введите новый адрес электронной почты для Gmail.com:"

EDIT_GMAIL_COM_PASSWORD_MESSAGE = "Введите новый пароль для Gmail.com:"

EDIT_MAIL_RU_MESSAGE = "Введите новый адрес электронной почты для Mail.ru:"

EDIT_MAIL_RU_PASSWORD_MESSAGE = "Введите новый пароль для Mail.ru:"

SUCCESSFUL_MAIL_RU_EDIT = "Почта Mail.ru успешно изменена!"

UNSUCCESSFUL_MAIL_RU_EDIT = "Ошибка: изменение почты Mail.ru не удалось. Пожалуйста, попробуйте снова."

SUCCESSFUL_MAIL_RU_PASSWORD_EDIT = "Пароль для Mail.ru успешно изменен!"

UNSUCCESSFUL_MAIL_RU_PASSWORD_EDIT = "Ошибка: изменение пароля для Mail.ru не удалось. Пожалуйста, попробуйте снова."

SUCCESSFUL_GMAIL_COM_EDIT = "Почта Gmail.com успешно изменена!"

UNSUCCESSFUL_GMAIL_COM_EDIT = "Ошибка: изменение почты Gmail.com не удалось. Пожалуйста, попробуйте снова."

SUCCESSFUL_GMAIL_COM_PASSWORD_EDIT = "Пароль для Gmail.com успешно изменен!"

UNSUCCESSFUL_GMAIL_COM_PASSWORD_EDIT = "Ошибка: изменение пароля для Gmail.com не удалось. Пожалуйста, попробуйте снова."