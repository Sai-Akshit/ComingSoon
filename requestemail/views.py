from django.shortcuts import render

def request_email(request):
    context = {}
    domains = ['HR, Admin and Communication', 'Marketing', 'UI/UX', 'Data & Analytics', 'Research and Business Analysis', 'Product Life Cycle', 'Creative Design and Content', 'Frontend Development', 'Backend Development']
    context['domains'] = domains

    if request.POST:
        print(f'\n{request.POST}\n')

    return render(request, 'requestemail/request.html', context)
