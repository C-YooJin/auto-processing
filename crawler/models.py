from django.db import models

TEAMS = (
    ('', 'Choose your team...'),
    ('NSML', 'NSML'),
    ('AI Production', 'AI Production'),
    ('AI Research', 'AI Research'),
    ('Biz AI', 'Biz AI'),
    ('OCR', 'OCR'),
    ('Speech', 'Speech'),
    ('Voice', 'Voice'),
    ('Vision', 'Vision'),
    ('Data & Connection', 'Data & Connection'),
    ('NSML Competition TF', 'NSML Competition TF'),
    ('DUET TF', 'DUET TF'),
    ('Pasha TF', 'Pasha TF')
)


JPG_YN = (
    ('0', 'JPG_ONLY'),
    ('1', 'URL+Meta')
)

class Google_crawl(models.Model):
    request_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    employee_number = models.CharField(max_length=12, help_text='ex) KR62111')
    team_name = models.CharField(max_length=20, help_text='- TEAM NAME -', choices=TEAMS)
    download_type = models.CharField(max_length=20, choices=JPG_YN)       # Image only -> 0 / url + meta info -> 1
    crawl_info = models.TextField(max_length=200, help_text='데이터가 어떤 연구 / 프로젝트에 사용 될지 말씀해주세요')
    keyword = models.CharField(max_length=20, help_text='keyword to crawl images from google ex) dog')
    max_num = models.IntegerField(help_text='Maximum number of images to download ex) 10000')
    request_date = models.DateTimeField(auto_now_add=True)

