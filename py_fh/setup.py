from setuptools import setup, find_packages

setup(
    name="py_fh",  # اسم المكتبة
    version="0.1",  # رقم الإصدار
    packages=find_packages(),  # حزم المشروع
    description="Maktabah for Prayer Times",  # وصف المكتبة
    long_description="This library provides prayer times for cities in Iraq.",  # وصف طويل
    long_description_content_type="text/markdown",
    author="hasneen",  # اسمك
    author_email="almhyuo@gmail.com",  # بريدك الإلكتروني
    url="https://github.com/hasneenai/py_fh",  # رابط المستودع على GitHub
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[],  # قائمة الحزم المطلوبة إذا كان هناك حزم أخرى تعتمد عليها
)
