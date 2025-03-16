# py_fh

مكتبة بايثون لعرض مواقيت الصلاة في العراق باستخدام API Aladhan.

## كيفية التثبيت

1. قم بتثبيت المكتبة باستخدام pip:
    ```bash
    pip install py_fh
    ```

## كيفية الاستخدام

```python
from py_fh import PrayerTimes

city_name = "Baghdad"  # اختر المدينة المطلوبة في العراق
prayer = PrayerTimes(city_name)
prayer.get_prayer_times()
prayer.display_prayer_times()
