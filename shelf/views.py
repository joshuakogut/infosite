from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from .models import Tbproductwarehouse, Tbwhlocation


def shelf_index(request):
    locations = list(
        Tbwhlocation.objects.order_by("description")
        .filter(active=True)
        .values_list("description", flat=True)
        .distinct()
    )
    return render(
        request,
        "shelf/barcode_scanner.html",
        {
            "location_descriptions": locations,
        },
    )


@csrf_exempt
def wipe(request):
    """Endpoint expected by the scanner UI. Receives POST with form field
    `shelf` and performs server-side wipe logic. Currently a no-op (placeholder).
    """
    if request.method != "POST":
        return HttpResponseBadRequest("Only POST allowed")

    shelf = request.POST.get("shelf")
    if not shelf:
        return HttpResponseBadRequest("Missing shelf parameter")

    # TODO: implement wiping logic here. For now, just accept and return OK.
    # e.g. perform any server-side clearing or state changes for `shelf`.
    print(f"Received wipe request for shelf: {shelf}")
    location = Tbwhlocation.objects.filter(description=shelf).first()
    if location:
        print("Found location:", shelf, location.guidwhlocation)
        # clear all Tbproductwarehouse entries for this location
        Tbproductwarehouse.objects.filter(
            guidwhlocation=location.guidwhlocation
        ).delete()
    else:
        print("No location found for shelf:", shelf)

    return HttpResponse("OK")
