from setuptools import setup, find_packages

setup(
    name='py_fh',
    version='1.0',
    packages=find_packages(),
    description='مكتبة لعرض مواقيت الصلاة في العراق',
    author='hasneen',
    author_email='almhyuo@gmail.com',
    install_requires=[
        'requests',  # إضافة المكتبة المطلوبة
    ],
)
