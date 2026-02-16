from django.forms import (
    CharField, DateField, ModelForm, IntegerField, ModelChoiceField, Textarea
)
from first_app.models import Genre, Movie
import re
from django.core.exceptions import ValidationError
from datetime import date


def capitalized_validator(value):
    if value[0].islower():
        raise ValidationError('Value must be capitalized.')


class PastMonthField(DateField):

    def validate(self, value):
        super().validate(value)
        if value >= date.today():
            raise ValidationError('Only past dates allowed here.')

    def clean(self, value):
        result = super().clean(value)
        return date(year=result.year, month=result.month, day=1)


class MovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'

    title = CharField(max_length=128, validators=[capitalized_validator])
    genre = ModelChoiceField(queryset=Genre.objects)
    rating = IntegerField(min_value=1, max_value=10)
    released = DateField()
    description = CharField(widget=Textarea, required=False)

    def clean_description(self):
        initial = self.cleaned_data['description']
        sentences = re.sub(r's*.s*', '.', initial).split('.')
        return '. '.join(sentence.capitalize() for sentence in sentences)

    def clean(self):
        result = super().clean()
        if result['genre'].name.lower() == 'comedy' and result['rating'] > 5:
            self.add_error('genre', 'Modify this!')
            self.add_error('rating', 'Modify this!')
            raise ValidationError(
                "Commedies aren't so good to be rated over 5."
            )
        return result
