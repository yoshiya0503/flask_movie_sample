#! /usr/bin/env python3
# -*- encoding: utf-8 -*-
"""
flask movie app
sample
"""
__author__ = 'Yoshiya Ito <myon53@gmail.com>'
__version__ = '0.0.1'
__date__ = '13 Nov 2015'

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/movie')
def show_movie():
    return render_template('movie.html')


@app.route('/hls')
def show_hls():
    return render_template('hls.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0');
