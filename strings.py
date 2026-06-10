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

EDIT_LETTER_PATTERN_BUTTON = "Изменить шаблон письма"

DELETE_LETTER_PATTERN_BUTTON = "Удалить шаблон письма"

EDIT_LETTER_PATTERN_MESSAGE = "Введите новый текст шаблона письма:"

SUCCESSFUL_LETTER_PATTERN_EDIT_MESSAGE = "Шаблон письма успешно изменен!"

UNSUCCESSFUL_LETTER_PATTERN_EDIT_MESSAGE = "Ошибка: изменение шаблона письма не удалось. Пожалуйста, попробуйте снова."

LETTER_PATTERN_DELETED_SUCCESSFULLY = "Шаблон письма успешно удален!"

TITLES_MENU = "Выберите шаблон заголовка письма или создайте новый"

def CERTAIN_TITLE_MENU(title: str = "<заголовок не выбран>"):
    return f"Текущий шаблон заголовка письма:\n{title}\nВыберите действия:"

EDIT_TITLE_PATTERN_BUTTON = "Изменить шаблон заголовка письма"

DELETE_TITLE_PATTERN_BUTTON = "Удалить шаблон заголовка письма"

EDIT_TITLE_PATTERN_MESSAGE = "Введите новый текст шаблона заголовка:"

SUCCESSFUL_TITLE_PATTERN_EDIT_MESSAGE = "Шаблон заголовка письма успешно изменен!"

UNSUCCESSFUL_TITLE_PATTERN_EDIT_MESSAGE = "Ошибка: изменение шаблона заголовка письма не удалось. Пожалуйста, попробуйте снова."

TITLE_PATTERN_DELETED_SUCCESSFULLY = "Шаблон заголовка письма успешно удален!"

EDIT_FILES_BUTTON = "Редактировать файлы резюме"

EDIT_TITLE_BUTTON = "Редактировать заголовок письма"

EDIT_LETTER_BUTTON = "Редактировать письмо"

EDIT_EMAILS_TO_SEND_BUTTON = "Редактировать адреса электронной почты для отправки"

EMAIL_SEND_MENU = "Выберите, что вы хотите отредактировать, или отправьте резюме работодателю:"

EDIT_FILES_MENU = "Выберите файлы, которые хотите отправить"

def FILE_SELECTED(filename: str) -> str:
    return f"✅ {filename}"

def FILE_NOT_SELECTED(filename: str) -> str:
    return filename
