from django.contrib import admin

from osp.models import (
    Answer,
    Checkbox,
    CheckboxValue,
    Choice,
    ChoiceValue,
    Date,
    DateValue,
    Dropdown,
    DropdownValue,
    FileUpload,
    FileUploadValue,
    Form,
    FormFeedback,
    Paragraph,
    ParagraphValue,
    Question,
    ShortAnswer,
    ShortAnswerValue,
    Time,
    TimeValue,
    UserInformation,
    ZulipStat,
)

models = [
    UserInformation,
    Form,
    Question,
    Choice,
    Checkbox,
    Dropdown,
    Paragraph,
    ShortAnswer,
    Date,
    Time,
    FileUpload,
    Answer,
    ChoiceValue,
    CheckboxValue,
    DropdownValue,
    ParagraphValue,
    ShortAnswerValue,
    DateValue,
    TimeValue,
    FileUploadValue,
    FormFeedback,
    ZulipStat,
]

admin.site.register(models)
