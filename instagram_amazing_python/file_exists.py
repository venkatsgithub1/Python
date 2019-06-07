import os

# We have file test.txt, hence we get True
print(os.path.exists('./test.txt'))
# We don't have file text.txt, hence we get False
print(os.path.exists('./text.txt'))