import requests
from datetime import datetime

class PrayerTimes:
    def __init__(self, city, country='Iraq'):
        self.city = city
        self.country = country
        self.api_url = 'http://api.aladhan.com/v1/timingsByCity'
        self.api_key = 'YOUR_API_KEY'  # ضع هنا مفتاح الـ API الخاص بك
        self.timings = None

    def get_prayer_times(self):
        params = {
            'city': self.city,
            'country': self.country,
            'method': 2,  # طريقة حساب مواقيت الصلاة (2 هي الطريقة الخاصة بالعراق)
        }

        response = requests.get(self.api_url, params=params)
        data = response.json()

        if data['code'] == 200:
            self.timings = data['data']['timings']
        else:
            print("حدث خطأ في جلب البيانات")

    def display_prayer_times(self):
        if self.timings:
            print(f"مواقيت الصلاة لمدينة {self.city}, {self.country}:")
            for prayer, time in self.timings.items():
                # تنسيق الوقت بطريقة مريحة
                prayer_time = datetime.strptime(time, '%H:%M').strftime('%I:%M %p')
                print(f"{prayer}: {prayer_time}")
        else:
            print("لم يتم تحميل المواقيت بعد!")
