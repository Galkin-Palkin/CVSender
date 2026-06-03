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

EMAIL_MENU = "s"

MAIL_RU_BUTTON = "Mail.ru"

GMAIL_COM_BUTTON = "Gmail.com"

EDIT_EMAIL_BUTTON = "Редактировать почту"

EDIT_PASSWORD_BUTTON = "Редактировать пароль"

MAIL_RU_MENU = "s"

GMAIL_COM_MENU = "s"

EDIT_GMAIL_COM_MESSAGE = "s"

EDIT_GMAIL_COM_PASSWORD_MESSAGE = "s"

EDIT_MAIL_RU_MESSAGE = "s"

EDIT_MAIL_RU_PASSWORD_MESSAGE = "s"

SUCCESSFUL_MAIL_RU_EDIT = "s"

UNSUCCESSFUL_MAIL_RU_EDIT = "s"

SUCCESSFUL_MAIL_RU_PASSWORD_EDIT = "s"

UNSUCCESSFUL_MAIL_RU_PASSWORD_EDIT = "s"

SUCCESSFUL_GMAIL_COM_EDIT = "s"

UNSUCCESSFUL_GMAIL_COM_EDIT = "s"

SUCCESSFUL_GMAIL_COM_PASSWORD_EDIT = "s"

UNSUCCESSFUL_GMAIL_COM_PASSWORD_EDIT = "s"