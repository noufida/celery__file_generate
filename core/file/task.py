from celery import shared_task
import csv
from faker import Faker
import shutil


#celery task to generate file
@shared_task(bind=True)
def generate_file(self,file_name,data_count):

    print(file_name,data_count,generate_file.request.id)

    #to generate sample csv with some sample datas
    fake = Faker()  #for random datas
    number_of_records = data_count

    with open(f'{file_name}.csv', mode='w') as file:
        file_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        file_writer.writerow(['first_name', 'last_name', 'age'])

        for _ in range(number_of_records):
            file_writer.writerow([fake.first_name(), fake.last_name(), fake.numerify("@#")])

    #to copy above generated file into folder called "data"
    shutil.copy(f'{file_name}.csv','data')
    
    return 'Done'