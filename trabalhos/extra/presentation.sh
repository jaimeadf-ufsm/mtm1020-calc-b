set -o xtrace

python newton.py < examples/n01.txt
python newton.py < examples/n02.txt
python newton.py < examples/n03.txt
python newton.py < examples/n04.txt

python gradient_descent.py < examples/g01.txt
python gradient_descent.py < examples/g02.txt
python gradient_descent.py < examples/g03.txt
python gradient_descent.py < examples/g04.txt