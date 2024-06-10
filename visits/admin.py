from django.contrib import admin
from .models import Visit, VisitHits
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.urls import path
from django.db import models
from django.shortcuts import render


# Register your models here.


class VisitAdmin(admin.ModelAdmin):
    list_display = ("ip_address", "os", "browser", "device", "day", "date", "hits")
    search_fields = ("ip_address", "os", "browser", "device")
    list_filter = ("os", "browser", "device", "day")
    readonly_fields = ("ip_address", "os", "browser", "device", "day", "date", "hits")
    date_hierarchy = "day"
    ordering = ("-day", "-date")

    def hits(self, obj):
        return obj.visit_hits.hits

    hits.short_description = "Hits"

    def get_queryset(self, request):
        return super().get_queryset(request).select_related("visit_hits")

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context["total_hits"] = VisitHits.objects.aggregate(total_hits=models.Sum("hits"))["total_hits"]
        return super().changelist_view(request, extra_context=extra_context)

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                "stats/",
                self.admin_site.admin_view(self.stats_view),
                name="visits_stats",
            )
        ]
        return custom_urls + urls

    def stats_view(self, request):
        total_hits = VisitHits.objects.aggregate(total_hits=models.Sum("hits"))["total_hits"]
        total_visits = Visit.objects.count()
        return render(
            request,
            "admin/visits/stats.html",
            {
                "total_hits": total_hits,
                "total_visits": total_visits,
            },
        )

    def view_on_site(self, obj):
        return mark_safe(f'<a href="https://ahmedsaied.info/visits/{obj.id}/">View on site</a>')

    def get_view_on_site_url(self, obj=None):
        if obj:
            return reverse("visits:visit_detail", args=[obj.id])
        return super().get_view_on_site_url(obj)

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

    def has_module_permission(self, request):
        return True


admin.site.register(Visit, VisitAdmin)
