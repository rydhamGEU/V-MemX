from flask import Flask, render_template, request
from simulators.fifo_simulator import fifo_page_replacement
from simulators.lru_simulator import lru_page_replacement
from simulators.optimal_simulator import optimal_page_replacement

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            pages = list(map(int, request.form['pages'].split()))
            frames = int(request.form['frames'])
            algorithm = request.form['algorithm']

            if algorithm == 'FIFO':
                steps, faults = fifo_page_replacement(pages, frames)
            elif algorithm == 'LRU':
                steps, faults = lru_page_replacement(pages, frames)
            elif algorithm == 'Optimal':
                steps, faults = optimal_page_replacement(pages, frames)
            else:
                raise ValueError("Invalid algorithm")

            return render_template('result.html', steps=steps, faults=faults, algo=algorithm)

        except Exception as e:
            return render_template('index.html', error=str(e))

    return render_template('index.html', error=None)

if __name__ == '__main__':
    app.run(debug=True)