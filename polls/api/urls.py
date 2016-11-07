from django.conf.urls import url
from .views import (
                   PresidentList ,
                   PresidentDetail ,
                   GovernorList ,
                   GovernorDetail,
                   SenatorList,
                   SenatorDetail,
                   WomenrepsList,
                   WomenrepsDetail,
                   ConstituencyList,
                   )

urlpatterns = [
url(r'^presidentlist/$' , PresidentList.as_view()),
url(r'^presidentdetail/(?P<country>\w+)/$' ,PresidentDetail.as_view()),
url(r'^governorlist/$' , GovernorList.as_view()),
url(r'^governordetail/(?P<county>\w+)/$' , GovernorDetail.as_view()),
url(r'^senatorlist/$' , SenatorList.as_view()),
url(r'^senatordetail/(?P<county>\w+)/$' , SenatorDetail.as_view()),
url(r'^womenrepslist/$' , WomenrepsList.as_view()),
url(r'^womenrepsdetail/(?P<county>\w+)/$' , WomenrepsDetail.as_view()),
url(r'^constituencylist/(?P<county>\w+)/$' , ConstituencyList.as_view()),
]
