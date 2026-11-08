"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.urls import path

HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Hello from Adios</title>
  <style>
    body { margin: 0; min-height: 100vh; display: grid; place-items: center; font-family: Arial, sans-serif; color: #f8fafc; background: #020617; }
    main { width: min(680px, calc(100% - 48px)); }
    p.kicker { color: #67e8f9; font-weight: 700; letter-spacing: .24em; text-transform: uppercase; }
    h1 { margin: 16px 0; font-size: clamp(3rem, 9vw, 5.5rem); line-height: 1; }
    p { color: #cbd5e1; font-size: 1.125rem; line-height: 1.7; }
    nav { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 32px; }
    a { border: 1px solid rgba(255,255,255,.18); border-radius: 8px; color: #f8fafc; padding: 12px 16px; text-decoration: none; }
    a.primary { background: #67e8f9; color: #020617; border-color: #67e8f9; font-weight: 700; }
  </style>
</head>
<body>
  <main>
    <p class="kicker">Adios starter</p>
    <h1>Hello from Adios</h1>
    <p>This Django template is ready to build, ship, and run on Adios.</p>
    <nav aria-label="Adios links">
      <a class="primary" href="https://app.adios.dev/signup">Deploy on Adios</a>
      <a href="https://www.adios.dev/docs/quickstart">Read the quickstart</a>
    </nav>
  </main>
</body>
</html>
"""


def home(_request):
    return HttpResponse(HTML)


def healthz(_request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT 1")
        cursor.fetchone()
    return JsonResponse(
        {"ok": True},
        json_dumps_params={"separators": (",", ":")},
    )


urlpatterns = [
    path("", home, name="home"),
    path("healthz", healthz, name="healthz"),
    path("admin/", admin.site.urls),
]
