from haystack import indexes
from .models import HeroInfo, UserInfo


class HeroInfoIndex(indexes.SearchField, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return HeroInfo

    def index_queryset(self, using=None):
        return self.get_model().objects.all()






