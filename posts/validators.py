from django.core.exceptions import ValidationError

def validate_file_size(value):
    filesize = value.size

    if filesize > 21485760:
        raise ValidationError("The maximum file size that can be uploaded is 21 MB")
    else:
        return value