import requests
from django.shortcuts import render, redirect
from .forms import JobForm

FASTAPI_URL = "http://127.0.0.1:8001"

def dashboard(request):
    jobs_res = requests.get(f"{FASTAPI_URL}/jobs")
    stats_res = requests.get(f"{FASTAPI_URL}/jobs/stats")
    jobs = jobs_res.json().get("jobs", [])
    stats = stats_res.json()
    return render(request, 'dashboard.html', {
        'jobs': jobs,
        'total': stats.get("total", 0),
        'interviews': stats.get("interviews", 0),
        'offers': stats.get("offers", 0),
        'rejected': stats.get("rejected", 0),
    })

def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            requests.post(f"{FASTAPI_URL}/jobs", json={
                "company": data["company"],
                "role": data["role"],
                "applied_date": str(data["applied_date"]),
                "status": data["status"],
                "notes": data.get("notes", "")
            })
            return redirect('/')
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})

def edit_job(request, id):
    job_res = requests.get(f"{FASTAPI_URL}/jobs/{id}")
    job_data = job_res.json()

    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            requests.put(f"{FASTAPI_URL}/jobs/{id}", json={
                "company": data["company"],
                "role": data["role"],
                "applied_date": str(data["applied_date"]),
                "status": data["status"],
                "notes": data.get("notes", "")
            })
            return redirect('/')
    else:
        from .models import JobApplication
        from datetime import date
        job_obj = JobApplication(
            id=job_data["id"],
            company=job_data["company"],
            role=job_data["role"],
            applied_date=job_data["applied_date"],
            status=job_data["status"],
            notes=job_data["notes"]
        )
        form = JobForm(instance=job_obj)
    return render(request, 'edit_job.html', {'form': form})

def delete_job(request, id):
    requests.delete(f"{FASTAPI_URL}/jobs/{id}")
    return redirect('/')