# here is our visits middleware
from django.utils import timezone
from .models import Visit, VisitHits
from .utils import get_visitor_info

from django.utils.deprecation import MiddlewareMixin


class VisitsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith("/admin"):
            return None
        try:
            ip_address, os, browser, device = get_visitor_info(request)
        except Exception as e:
            print("Error getting visitor info:")
            print(e)
            return None
        date = timezone.now()
        day = date.date()
        visit = Visit.objects.filter(ip_address=ip_address, day=day).first()
        if not visit:
            visit = Visit.objects.create(ip_address=ip_address, os=os, browser=browser, device=device, day=day, date=date)
        visit_hits, created = VisitHits.objects.get_or_create(visit=visit)
        visit_hits.increment_hits()
        return None

    def process_response(self, request, response):
        return response
