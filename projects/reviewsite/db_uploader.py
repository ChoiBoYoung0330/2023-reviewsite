import csv
from pybo.models import review_info
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

with open('review_info.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        review = review_info(review1=row['review1'], review2=row['review2'], review_score=row['score'], id=row['id'], title_id=row['title_id'])
        review.save()