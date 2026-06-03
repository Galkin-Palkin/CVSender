class CallbackData:
    def extract_id(callback_data: str) -> str:
        return callback_data.split(':')[-1]
    
    cv_letters = "cv_letters"

    cv_titles = "cv_titles"

    email_credentials = "email_credentials"

    email_send = "email_send"

    letter_prefix = "letter:"
    def letter(letter_id):
        return f"{CallbackData.letter_prefix}{letter_id}"
    
    edit_letter_prefix = "edit_letter:"
    def edit_letter(letter_id):
        return f"{CallbackData.edit_letter_prefix}{letter_id}"
    
    delete_letter_prefix = "delete_letter:"
    def delete_letter(letter_id):
        return f"{CallbackData.delete_letter_prefix}{letter_id}"
    
    title_prefix = "title:"
    def title(title_id):
        return f"{CallbackData.title_prefix}{title_id}"
    
    edit_title_prefix = "edit_title:"
    def edit_title(title_id):
        return f"{CallbackData.edit_title_prefix}{title_id}"
    
    delete_title_prefix = "delete_title:"
    def delete_title(title_id):
        return f"{CallbackData.delete_title_prefix}{title_id}"
    
    mail_ru = "mail_ru"

    gmail_com = "gmail_com"

    edit_email_prefix = "edit_email:"
    def edit_email(email: str):
        return f"{CallbackData.edit_email_prefix}{email}"

    edit_password_prefix = "edit_password:"
    def edit_password(email: str):
        return f"{CallbackData.edit_password_prefix}{email}"
