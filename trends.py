from pytrends.request import TrendReq

def get_trends():
    pytrends = TrendReq(hl='id-ID', tz=360)
    
    trending = pytrends.trending_searches(pn='indonesia')
    
    return trending[0].tolist()[:10]
