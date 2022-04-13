

from django.urls import path
from . import views




urlpatterns = [
    path('', views.home, name="home"),
    path('how/', views.how, name="how"),
    path('white/', views.white, name="white"),
    path('projects/', views.projects, name="projects"),
    path('liquiditypools/', views.liquiditypools, name="liquiditypools"),
    path('development/', views.development, name="development"),
    path('rental/', views.rental, name="rental"),
    path('venue/', views.venue, name="venue"),
  	path('liquidity/', views.liquidity, name="liquidity"),
  	path('buildings/', views.buildings, name="buildings"),
    path('plan/', views.plan, name="plan"),
    path('stand/', views.stand, name="stand"),
    path('token/', views.token, name="token"),
    path('guest/', views.guest, name="guest"),
    path('information1/', views.information1, name="information1"),
    path('information2/', views.information2, name="information2"),
    path('hostingrules/', views.hostingrules, name="hostingrules"),
    path('vaccineprotocol1/', views.vaccineprotocol1, name="vaccineprotocol1"),
    path('vaccineprotocol12/', views.vaccineprotocol2, name="vaccineprotocol2"),
    path('rentreduction/', views.rentreduction, name="rentreduction"),
    path('tokenprogram1/', views.tokenprogram1, name="tokenprogram1"),
    path('tokenprogram2/', views.tokenprogram2, name="tokenprogram2"),
    path('rentopportunity/', views.rentopportunity, name="rentopportunity"),
    path('ourcommunity1/', views.ourcommunity1, name="ourcommunity1"),
    path('ourcommunity2/', views.ourcommunity2, name="ourcommunity2"),
    path('development1/', views.development1, name="development1"),
    path('overview1/', views.overview1, name="overview1"),
    path('overview2/', views.overview2, name="overview2"),
    path('guestrules/', views.guestrules, name="guestrules"),
    path('costtrasparency/', views.costtrasparency, name="costtrasparency"),
    path('guestopportunity/', views.guestopportunity, name="guestopportunity"),
    path('reservation/', views.reservation, name="reservation"),
    path('payment1/', views.payment1, name="payment1"),
    path('payment2/', views.payment2, name="payment2"),
    path('trading/', views.trading, name="trading"),
    path('investorsrules/', views.investorsrules, name="investorsrules"),
    path('tradingclarity/', views.tradingclarity, name="tradingclarity"),
    path('tokenprogram3/', views.tokenprogram3, name="tokenprogram3"),
    path('tradingdesk/', views.tradingdesk, name="tradingdesk"),
    path('ourcommunity3/', views.ourcommunity3, name="ourcommunity3"),
    path('report/', views.report, name="report"),
    path('news/', views.news, name="news"),
    path('collateral/', views.collateral, name="collateral"),
    path('gov/', views.gov, name="gov"),
    path('fbm/', views.fbm, name="fbm"),
    path('owner/', views.owner, name="owner"),
    path('gin/', views.gin, name="gin"),
    path('pro/', views.pro, name="pro"),
    path('ten/', views.ten, name="ten"),
    path('sub/', views.sub, name="sub"),
    path('impressum/', views.impressum, name="impressum"),
    path('vigna/', views.vigna, name="vigna"),
    path('apts/', views.apts, name="apts"),
  




]
