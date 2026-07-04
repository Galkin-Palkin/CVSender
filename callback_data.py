class CallbackData:
    cv_letters = "cv_letters"

    cv_titles = "cv_titles"

    email_send = "email_send"

    letter_prefix = "letter:"
    def letter(letter_id: str):
        return f"{CallbackData.letter_prefix}{letter_id}"
    
    edit_letter_prefix = "edit_letter_pattern:"
    def edit_letter_pattern(letter_id: str):
        return f"{CallbackData.edit_letter_prefix}{letter_id}"
    
    delete_letter_prefix = "delete_letter_pattern:"
    def delete_letter_pattern(letter_id: str):
        return f"{CallbackData.delete_letter_prefix}{letter_id}"
    
    title_prefix = "title:"
    def title(title_id: str):
        return f"{CallbackData.title_prefix}{title_id}"
    
    edit_title_prefix = "edit_title_pattern:"
    def edit_title_pattern(title_id: str):
        return f"{CallbackData.edit_title_prefix}{title_id}"
    
    delete_title_prefix = "delete_title_pattern:"
    def delete_title_pattern(title_id: str):
        return f"{CallbackData.delete_title_prefix}{title_id}"
    
    edit_password_prefix = "edit_password:"
    def edit_password(email: str):
        return f"{CallbackData.edit_password_prefix}{email}"

    edit_files = "edit_files"
    
    edit_title = "edit_title"
    
    edit_letter = "edit_letter"
    
    edit_emails_to_send = "edit_emails_to_send"
    
    send_cv = "send_cv"
    
    file_selected_prefix = "file_selected:"
    def file_selected(file_id: str):
        return f"{CallbackData.file_selected_prefix}{file_id}"
    
    file_unselected_prefix = "file_unselected:"
    def file_unselected(file_id: str):
        return f"{CallbackData.file_unselected_prefix}{file_id}"
    
    create_new_letter = "create_new_letter"

    edit_letter_name_prefix = "edit_letter_name:"
    def edit_letter_name(letter_id):
        return f"{CallbackData.edit_letter_name_prefix}{letter_id}"