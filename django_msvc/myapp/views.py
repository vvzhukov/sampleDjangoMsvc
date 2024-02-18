from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from .models import Book
from .serializers import BookSerializer


@csrf_exempt
@require_http_methods(["GET"])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return JsonResponse({"books": serializer.data})


@csrf_exempt
@require_http_methods(["GET"])
def get_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return JsonResponse({"book": serializer.data})
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)


@csrf_exempt
@require_http_methods(["POST"])
def create_book(request):
    data = request.POST
    serializer = BookSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return JsonResponse({"message": "Book created successfully", "book": serializer.data}, status=201)
    return JsonResponse({"error": "Invalid data"}, status=400)


@csrf_exempt
@require_http_methods(["PUT"])
def update_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        data = request.POST
        serializer = BookSerializer(book, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message": "Book updated successfully", "book": serializer.data})
        return JsonResponse({"error": "Invalid data"}, status=400)
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_book(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        book.delete()
        return JsonResponse({"message": "Book deleted successfully"})
    except ObjectDoesNotExist:
        return JsonResponse({"error": "Book not found"}, status=404)