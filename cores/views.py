from django.shortcuts import render


# Create your views here.
def index(request):
    students = [
        {
        'name': 'Sadiqul Islam',
        'age': 28,
        },
        {
        'name': 'Rohan Reza',
        'age': 48,
        },
        {
        'name': 'Kamrul Islam',
        'age': 21,
        },
        {
        'name': 'Jubayer Mahmud',
        'age': 30,
        },
    ]
    return render(request, 'cores/index.html', {'students': students})