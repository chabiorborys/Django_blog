from django.test import TestCase
from posts.forms import ContactForm

class ContactFormTest(TestCase):
    def test_contact_form_name_field_label(self):
        form = ContactForm()
        self.assertTrue(form.fields['name'].label == None or form.fields['name'].label == 'Your name')

    def test_contact_form_name_max_length(self):
        form = ContactForm()
        self.assertTrue(form.fields['name'].max_length == None or form.fields['name'].max_length <= 500)
        
    def test_contact_form_email_field_label(self):
        form = ContactForm()
        self.assertTrue(form.fields['email'].label == None or form.fields['email'].label == 'Your email')

    def test_contact_form_email_max_length(self):
        form = ContactForm()
        self.assertTrue(form.fields['email'].max_length == None or form.fields['email'].max_length <= 500)

    def test_contact_form_comment_field_label(self):
        form = ContactForm()
        self.assertTrue(form.fields['comment'].label == None or form.fields['comment'].label == '')
