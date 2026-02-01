FROM python
RUN git clone "https://github.com/venomkobain/test.git"
CMD ["python3","test/correct_test.py"]
CMD ["python3","test/incorrect_test.py"]
