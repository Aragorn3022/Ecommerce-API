curl -o setup.exe https://mega.nz/MEGAcmdSetup64.exe;
.\setup.exe;
Start-Sleep -Seconds 360
mega-get https://mega.nz/folder/jugljBzY#7aEMr8X7P3h2ebwCpztCBQ  .\.venv
.\.venv\Scripts\activate.ps1;


python .\manage.py makemigrations


python .\manage.py migrate


python manage.py runserver
