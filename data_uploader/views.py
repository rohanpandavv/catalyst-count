from django.shortcuts import render, redirect
from .forms import UploadFileForm
from .models import CompanyData
import csv
import pandas as pd
import os
from django.conf import settings
from django.http import HttpResponse

CHUNK_SIZE = 5000 #5000 records per csv file
PATH = settings.BASE_DIR #imported base_dir from settings and assigned it to PATH constant

#this function accepts a csv_file in its request which we upload from a form
#the csv is split into chunks and I have also handled validation i.e. the process will start only of the file is a csv
def csv_read(request):
    try:
        batch_no = 1
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                uploaded_file = request.FILES.get('csv_file', None)
                file_extension = request.FILES['csv_file'].content_type
                
                if file_extension != 'text/csv':
                    return HttpResponse("Please upload a CSV file.", content_type="text/plain", status=400)
                
                if uploaded_file:
                    file_name = os.path.splitext(request.FILES['csv_file'].name)[0]
                    chunk_storage = os.path.join(PATH, 'data_uploader', 'temp', file_name)
                    os.makedirs(chunk_storage, exist_ok=True)
                    
                    for chunk in pd.read_csv(uploaded_file, chunksize=CHUNK_SIZE, skiprows=1):
                        chunk_file_name = f"{file_name}_{batch_no}.csv"
                        chunk_file_path = os.path.join(chunk_storage, chunk_file_name)
                        chunk.to_csv(chunk_file_path, index=False)
                        write_from_csv_to_db(chunk_file_path)
                        batch_no+=1

        else:
            form = UploadFileForm()

        return render(request, 'upload.html', {'form': form})
    except Exception as e:
        return HttpResponse(str(e), status=500)

def write_from_csv_to_db(file_path):
    print(file_path)
    try:
        if file_path == "":
            return
        df = pd.read_csv(file_path)

        df.columns = ['id', 'name', 'domain', 'year_founded', 'industry', 'size_range', 'locality', 'country', 'linkedin_url', 'cr_emp_est', 'tot_emp_est']
        insert_data = [
            CompanyData(
                id=row['id'],
                name=row['name'],
                domain=row['domain'],
                year_founded=int(row['year_founded']) if pd.notnull(row['year_founded']) else None,
                industry=row['industry'],
                size_range=row['size_range'],
                city = str(row['locality']).split(',')[0].strip() if pd.notnull(row['locality']) and str(row['locality']) != "" else '',
                state = str(row['locality']).split(',')[1].strip() if pd.notnull(row['locality']) and str(row['locality']) != "" and len(str(row['locality']).split(',')) > 1 else '',
                country=row['country'],
                linkedin_url=row['linkedin_url'],
                cr_emp_est=row['cr_emp_est'],
                tot_emp_est=row['tot_emp_est']
            )
            for _,row in df.iterrows()
        ]
        CompanyData.objects.bulk_create(insert_data)
        clear_temp(file_path) #internal function to clear temporary chunks of data
    except Exception as e:
        return print("Exception --- ",str(e))

def clear_temp(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)