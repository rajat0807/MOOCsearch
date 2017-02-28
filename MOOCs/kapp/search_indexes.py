import datetime
from haystack import indexes
from kapp.models import Courses


class CoursesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    author = indexes.CharField(model_attr='website')
    details = indexes.DateTimeField(model_attr='details')

    def get_model(self):
        return Courses